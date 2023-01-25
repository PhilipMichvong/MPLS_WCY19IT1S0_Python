import backend.network.packet as netpac
import backend.network.interface as netint
import backend.network.net as netnet

# ********** class <Device> **********
class Device:
    DEVICES = []
    
    def __init__(self, name = None):
        if name:
            self._name = name
        else:
            self._name = f'Device{len(Device.device_list) + 1}'
        
        self.interfaces = []
        
        Device.DEVICES.append(self)
        
    def __repr__(self) -> str:
        return f'''[Name]: {self._name}
    [Interfaces]: {self.interfaces}'''
    
    # Config
    def add_interface(self, int_name : str, int_address : str, int_mask : str):
        # Check if interface with specified name already exists
        for interface in self.interfaces:
            if int_name == interface.name:
                raise KeyError(f'Interface {int_name} already exists on this device!')
            
        # Create instance of class <Interface>
        obj = netint.Interface(int_name, int_address, int_mask)
        
        self.interfaces.append(obj)

    # Packets
    def receive_packet(self, packet):
        print(f'{self._name} : Received packet :\n\t{packet.type = }\n{packet.data = }')
        
    # Interface get
    #   -- Name
    def _get_interface_by_name(self, intf_name : str):
        for interface in self.interfaces:
            if interface.name == intf_name:
                return interface
            
        return None
    
    #   -- Address
    def _get_interface_by_address(self, intf_address : str):
        for interface in self.interfaces:
            if interface.address == intf_address:
                return interface
            
        return None
    
    
    # Devices
    @staticmethod
    def get_device_by_address(address : str):
        for device in Device.DEVICES:
            for interface in device.interfaces:
                if address == interface.address:
                    return device
        
        return None
                
    @staticmethod
    def clear_devices():
        Device.DEVICES = []


# ********** class <PC> **********
class PC(Device):
    def __init__(self, name = None, gateway = None):
        if not name:
            name = f'PC{len(PC.pc_list) + 1}'
        
        super().__init__(name)
        self.gateway = gateway
        
    def __repr__(self) -> str:
        return f'''[Name]: {self._name}:
    [Interfaces]: {self.interfaces}
    [Gateway]: {self.gateway}'''
    
    # Config
    def add_gateway(self, gateway_address : str):
        if len(self.interfaces) > 0:
            for interface in self.interfaces:
                net_addr = netnet.Net.compute_network_address(interface.address, interface.mask)[0]
                netgateway_addr = netnet.Net.compute_network_address(gateway_address, interface.mask)[0]

                if net_addr == netgateway_addr:
                    self.gateway = gateway_address
                    return
                
            raise ValueError(f'{gateway_address} : Gateway address is not valid!')
        
        else:
            raise ValueError('This PC has no interfaces!')

    # Packets
    def send_packet(self, packet):
        print(f'{self._name} : Sending packet :\n\t{packet.type}')
        
        if self.gateway is None:
            raise AttributeError('Gateway is not specified!')
        
        interface = self._get_interface_by_gateway(self.gateway)
        
        if interface is None:
            raise ValueError(f'Device has no interface with address {self.gateway}')

        interface.network.deliver_packet(packet, next_hop=self.gateway)

    # Interface get
    def _get_interface_by_gateway(self, gateway : str):
        for interface in self.interfaces:
            mask = interface.mask
            address = interface.address
            
            net_addr_1 = netnet.Net.compute_network_address(address, mask)[0]
            net_addr_2 = netnet.Net.compute_network_address(gateway, mask)[0]
            
            if net_addr_1.__eq__(net_addr_2):
                return interface
            
        return None

# ********** class <Router> **********
class Router(Device):
    def __init__(self, name = None):
        if not name:
            name = f'Router{len(Router.router_list)+1}'
        
        super().__init__(name)
        
        self.route_table = []
    
    def __repr__(self) -> str:
        # route_table_repr = []
        # for record in self.route_table:
        #     route_table_repr.append(f'{record["state"]} : {record["address"]}')
            
        return f'''[Name]: {self._name}: 
    [Interfaces]: {self.interfaces} 
    [Route Table]:\n{self._repr_route_table()}'''


    # Config
    def add_interface(self, int_name : str, int_address : str, int_mask : str) -> None:
        # Check if interface with specified name already exists
        for interface in self.interfaces:
            if int_name == interface.name:
                raise KeyError(f'Interface {int_name} already exists on this device!')
            
        # Create instance of class <Interface>
        interface = netint.Interface(int_name, int_address, int_mask)
        
        self.interfaces.append(interface)
        
        if not interface.network in self.route_table:
            record = {"protocol" : 'C', "address": interface.network.address, "next_hop" : None, "interface" : interface.name, 'metric' : 0}
            self.route_table.append(record)
    
    # Route Table
    def _repr_route_table(self) -> str:
        result = '\tProt\tAddr\t\tIntf\tMetric\tNext hop\n'
        for record in self.route_table:
            result += f'\t{record["protocol"]}\t{record["address"]}\t{record["interface"]}\t{record["metric"]}\t{record["next_hop"]}\n'
            
        return result
            
    
    # Packets
    def send_packet(self, packet) -> None:
        print(f'{self._name} : Sending packet :\n\t{packet.type}')
        
        dest_net_addr, dest_net_broadcast = netnet.Net.compute_network_address(packet.addr_to, netnet.MASK[packet.mask_bits_to])
        for record in self.route_table:            
            if record["address"] == dest_net_addr:
                intf_name = record["interface"]
                interface = self._get_interface_by_name(intf_name)
                
                if packet.addr_to == dest_net_broadcast:
                    # Send to all in network
                    interface.network.deliver_packet_broadcast(packet=packet, router_addr=interface.address)
                    
                else:
                    # Send to specified device in network
                    interface.network.deliver_packet(packet=packet, next_hop=record["next_hop"])
                    
                return
                
        raise ValueError(f'{dest_net_addr} is not accesibble!')
    
    def receive_packet(self, packet) -> None:
        print(f'{self._name} : Received packet :\n\t{packet.type}')
        
        if packet.type == netpac.PACKET_TYPE.RIP:
            self._handle_rip_packet(packet)
            
        elif packet.type == netpac.PACKET_TYPE.MPLS:
            self._handle_mpls_packet(packet)
        
        # If packet is to its device
        for interface in self.interfaces:
            if interface.address == packet.addr_to:
                print(f'{self._name} : Packet delivered!')
                return
        
        self.send_packet(packet)
    
        
    # Packets interpreter funcs
    def _handle_rip_packet(self, packet) -> None:
        print(f'\t{self._name}: RIP Data:')
        # print(f'\t{packet.data.split("|")}')
        # [protocol][address][next_hop][interface][metrics]
        data = packet.data.split('|')
        protocol = 'R'
        address = data[1]
        next_hop = packet.addr_from
        metrics = int(data[4]) + 1

        for interface in self.interfaces:
            if interface.address == packet.addr_to:
                intf_name = interface.name
        
        new_record = {  "protocol" : protocol, 
                        "address": address, 
                        "next_hop" : next_hop,
                        "interface" : intf_name, 
                        "metric" : metrics}
        
        # Check existing route table
        for record in self.route_table:
            # if specified network route is already stored
            if record['address'] == new_record['address']:
                # compare metrics
                if record['metric'] > new_record['metric']:
                    self.route_table.remove(record)
                    self.route_table.append(new_record)
                return

        # If there is no specified network route in route table
        #   then add new route
        self.route_table.append(new_record)
    
    
    def _handle_mpls_packet(self, packet) -> None:
        pass
    
    
    # RIP Distribution
    def rip_distribute(self) -> None:
        '''
            RIP Packet
                addr_to -> broadcast
                data -> route_table record
        '''
                
        for interface in self.interfaces:
            addr_from = interface.address
            addr_to = interface.network.broadcast
            mask_bits = netnet.Net.get_mask_bits(interface.mask)
            
            for record in self.route_table:
                data = ''
                for key, value in record.items():
                    data += str(value)
                    data += '|'
            
                packet = netpac.Packet(addr_from=addr_from, 
                                       addr_to=addr_to, 
                                       mask_bits_from=mask_bits, 
                                       mask_bits_to=mask_bits, 
                                       type=netpac.PACKET_TYPE.RIP, 
                                       data=data)

                self.send_packet(packet)