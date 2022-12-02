from network.packet import Packet
from network.interface import Interface
from network.net import (Net, MASK)

# ********** class <Device> **********
class Device:
    device_list = []
    
    def __init__(self, name = None):
        if name:
            self._name = name
        else:
            self._name = f'Device{len(Device.device_list) + 1}'
        
        self.interfaces = []
        
        Device.device_list.append(self)
        
    def __repr__(self) -> str:
        return f'''[Name]: {self._name}
    [Interfaces]: {self.interfaces}'''
    
    def _add_interface(self, int_name : str, int_address : str, int_mask : str):
        # Check if interface with specified name already exists
        for interface in self.interfaces:
            if int_name == interface.name:
                raise KeyError(f'Interface {int_name} already exists on this device!')
            
        # Create instance of class <Interface>
        obj = Interface(int_name, int_address, int_mask, self)
        
        self.interfaces.append(obj)

    def _receive_packet(self, packet : Packet):
        print(f'{self._name} : Received packet :\n{packet}')

# ********** class <PC> **********
class PC(Device):
    pc_list = []
    
    def __init__(self, name = None, gateway = None):
        if not name:
            name = f'PC{len(PC.pc_list) + 1}'
        
        super().__init__(name)
        self.gateway = gateway
        
        PC.pc_list.append(self)
        
    def __repr__(self) -> str:
        return f'''[Name]: {self._name}:
    [Interfaces]: {self.interfaces}
    [Gateway]: {self.gateway}'''
    

# ********** class <Router> **********
class Router(Device):
    router_list = []
    
    def __init__(self, name = None):
        if not name:
            name = f'Router{len(Router.router_list)+1}'
        
        super().__init__(name)
        
        self.route_table = []
        
        Router.router_list.append(self)
    
    def __repr__(self) -> str:
        # route_table_repr = []
        # for record in self.route_table:
        #     route_table_repr.append(f'{record["state"]} : {record["address"]}')
            
        return f'''[Name]: {self._name}: 
    [Interfaces]: {self.interfaces} 
    [Route Table]: {self.route_table}'''

    def _add_interface(self, int_name : str, int_address : str, int_mask : str):
        # Check if interface with specified name already exists
        for interface in self.interfaces:
            if int_name == interface.name:
                raise KeyError(f'Interface {int_name} already exists on this device!')
            
        # Create instance of class <Interface>
        interface = Interface(int_name, int_address, int_mask, self)
        
        self.interfaces.append(interface)
        
        if not interface.network in self.route_table:
            record = {"state" : 'C', "address": interface.network.address}
            self.route_table.append(record["address"])
    
    
    def _send_packet(self, packet):
        dest_net_addr = Net.compute_network_address(packet.addr_to, MASK[packet.mask_bits_to])[0]
        if dest_net_addr in self.route_table:
            print(f'{self._name} : Sending packet to NET[{dest_net_addr}] ...')
            
            return
        print('Error Sending')
    
    
    def _receive_packet(self, packet: Packet):
        print(f'{self._name} : Received packet :\n{packet}')
