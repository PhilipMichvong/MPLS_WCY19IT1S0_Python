# ************** class Packet **************
class Packet:
    def __init__(self, addr_from : str, addr_to : str, p_type : str, data : str):
        self.addr_from = addr_from
        self.addr_to = addr_to
        self.p_type = p_type
        self.data = data
        
    def __repr__(self) -> str:
        return f'Packet:\n\t\taddress_from: {self.addr_from}\n\t\taddress_to:   {self.addr_to}\n\t\ttype: {self.p_type}\n\t\tdata: {self.data}'

# ************** class Interface **************
class Interface:
    def __init__(self, name : str, address : str):
        self.name = name
        self.address = address
    
    def __repr__(self) -> str:
        return f'{self.name} : {self.address}'

# ************** class Router **************
class Router:
    router_list = []
    
    def __init__(self, interfaces = list, name = None):
        if name:
            self.name = name
        else:
            self.name = f'Router{len(Router.router_list)+1}'
            
        self.interfaces = interfaces
        self.route_table = []
        
        Router.router_list.append(self)
        
    def __repr__(self) -> str:
        return f'{self.name}: Interfaces={self.interfaces}'
        
    @staticmethod
    def get_router(addr : str):
        for router in Router.router_list:
            for interface in router.interfaces:
                if interface.address == addr:
                    return router
        return None
        
    def send_packet(self, packet : Packet):
        print(f'{self.name} : Sending packet:\n\t{packet}')
        if packet.addr_to in self.route_table:
            dest_router = Router.get_router(packet.addr_to)
            if dest_router:
                dest_router.get_packet(packet)
                return True
            return False
        return False
    
    def get_packet(self, packet : Packet):
        print(f'{self.name} : Got packet:\n\t{packet}')