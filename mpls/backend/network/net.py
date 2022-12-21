import backend.network.devices as netdev
import backend.network.packet as netpac

MASK = {
    0 : '0.0.0.0',
    1 : '128.0.0.0',
    2 : '192.0.0.0',
    3 : '224.0.0.0',
    4 : '240.0.0.0',
    5 : '248.0.0.0',
    6 : '252.0.0.0',
    7 : '254.0.0.0',
    8 : '255.0.0.0',
    9 : '255.128.0.0',
    10 : '255.192.0.0',
    11 : '255.224.0.0',
    12 : '255.240.0.0',
    13 : '255.248.0.0',
    14 : '255.252.0.0',
    15 : '255.254.0.0',
    16 : '255.255.0.0',
    17 : '255.255.128.0',
    18 : '255.255.192.0',
    19 : '255.255.224.0',
    20 : '255.255.240.0',
    21 : '255.255.248.0',
    22 : '255.255.252.0',
    23 : '255.255.254.0',
    24 : '255.255.255.0',
    25 : '255.255.255.128',
    26 : '255.255.255.192',
    27 : '255.255.255.224',
    28 : '255.255.255.240',
    29 : '255.255.255.248',
    30 : '255.255.255.252',
    31 : '255.255.255.254',
    32 : '255.255.255.255'
}


# ********** class <Net> **********
class Net:
    networks = []
    
    def __init__(self, address : str, mask : str, broadcast : str):
        self.address = address
        self.mask = mask
        self.broadcast = broadcast
        
        self.devices_addresses = []
        
        Net.networks.append(self)
        
    def __repr__(self):
        return f'Network [{self.address} : {self.mask} : {self.broadcast}]'
    
    
    # Add device IP address to network's devices_list
    def add_device(self, dev_addr : str):
        if not self.devices_addresses.__contains__(dev_addr):
            self.devices_addresses.append(dev_addr)
    
    # Remove device IP address from network's devices_list
    def remove_device(self, dev_addr : str):
        if self.devices_addresses.__contains__(dev_addr):
            self.devices_addresses.remove(dev_addr)
            
        if len(self.devices_addresses) == 0:
            Net.remove_network(self)
    
    # Check if network's devices_list contains specified IP address
    def is_host_available(self, address : str):
        if address in self.devices_addresses:
            return False
        return True
    
    # Print all networks
    @staticmethod
    def show_networks():
        print('Networks:')
        if len(Net.networks) > 0:
            for i in range(len(Net.networks)):
                print(f'[{i+1}]. {Net.networks[i]}')
            return
        print('-')
    
    # Calculate network and broadcast addresses
    @staticmethod
    def compute_network_address(addr : str, mask : str):
        addr_octets = addr.split('.')
        mask_octets = mask.split('.')
        
        wildcard_octets = []
        for octet in mask_octets:
            wildcard_octets.append(255 - int(octet))

        broadcast = []
        net_addr = []
        
        for ao, wo in zip(addr_octets, wildcard_octets):
            if wo == 0:
                net_addr.append(ao)
                broadcast.append(ao)
            else:
                interval = wo + 1
                a = 0
                while a < 257:
                    a += interval
                    if int(ao) < a:
                        break
                net_addr.append(str(a - interval))
                broadcast.append(str(a - 1))
        
        net_addr = '.'.join(net_addr)
        broadcast = '.'.join(broadcast)
        
        return net_addr, broadcast
    
    # Remove <Net>'net' from networks_list
    @staticmethod
    def remove_network(net):
        if Net.networks.__contains__(net):
            Net.networks.remove(net)
    
    # Get (or if not existed - create new) network to specified IP address
    @staticmethod
    def assign_network(address : str, mask : str, device):
        
        # Compute network and broadcast addresses
        net_addr, broadcast = Net.compute_network_address(address, mask)
        
        if address == net_addr or address == broadcast:
            raise ValueError(f'Invalid device IP address [{address}]!')
        
        # if there are no networks
        if len(Net.networks) == 0:
            net = Net(net_addr, mask, broadcast)
            net.add_device(address)
            return net

        # check existing networks
        for network in Net.networks:
            
            # if specified network already exists
            if network.address == net_addr:
                
                # if address is valid and available
                if network.is_host_available(address):
                    return network

                # if address is not valid or is unavailable
                else:
                    raise ValueError(f'IP address [{address}] is not available in network [{network.address}]!')
        
        # if specified network does not exists
        net = Net(net_addr, mask, broadcast)
        net.add_device(address)
        return net


    def deliver_packet(self, packet, next_hop = None):
        print(f'\tDELIVERING in {self.address} ...')
        
        if next_hop is None:
            # to PC
            device = netdev.Device.get_device_by_address(packet.addr_to)
            
        else:
            # to another router
            device = netdev.Device.get_device_by_address(next_hop)
            
        if device is None:
            raise ValueError(f'Cannot find device in net {self.address}')
        
        else:
            device._receive_packet(packet)
