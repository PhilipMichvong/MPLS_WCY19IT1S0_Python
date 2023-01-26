from enum import Enum
from backend.network.net import MASK

class PACKET_TYPE(Enum):
    RIP = 0
    LDP = 1
    ICMP = 2
    

class Packet:
    def __init__(self, addr_from : str, addr_to : str, mask_bits_from : int, mask_bits_to : int, type : PACKET_TYPE, data : str):
        self.addr_from = addr_from
        self.mask_bits_from = mask_bits_from
        self.addr_to = addr_to
        self.mask_bits_to = mask_bits_from
        self.type = type
        self.label = -1
        self.data = data
        
    def __repr__(self) -> str:
        return f'''Packet:
    [address_from]: {self.addr_from} /{self.mask_bits_from}
    [address_to]:   {self.addr_to} /{self.mask_bits_to}
    [type]:         {self.type.name}
    [data]:         {self.data}'''
