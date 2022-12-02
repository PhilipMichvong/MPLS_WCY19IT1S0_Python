from network.net import Net

# ********** class <Interface> **********
class Interface:
    def __init__(self, name : str, address : str, mask : str, device = None):
        self.name = name
        self.address = address
        self.mask = mask
        
        if device:
            self.network = Net.assign_network(address, mask, device)
    
    def __repr__(self) -> str:
        return f'{self.name} : {self.address}'