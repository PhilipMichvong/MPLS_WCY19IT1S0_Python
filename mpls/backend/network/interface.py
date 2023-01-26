import backend.network.net as netnet

# ********** class <Interface> **********
class Interface:
    def __init__(self, name : str, address : str, mask : str):
        self.name = name
        self.address = address
        self.mask = mask
        
        self.network = netnet.Net.assign_network(address, mask)
    
    def __repr__(self) -> str:
        return f'{self.name} : {self.address}'
    
    def __del__(self):
        self.network.remove_device(self.address)
        