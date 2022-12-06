import network.packet as netpac
import network.devices as netdev
import network.interface as netint

class Controller:
    PCs = []
    Routers = []
    
    @staticmethod
    def add_router(name = None):
        router = netdev.Router(name)
        Controller.Routers.append(router)
        
    @staticmethod
    def add_pc(name = None):
        pc = netdev.PC(name)
        Controller.PCs.append(pc)
    
    @staticmethod
    def show_routers():
        for router in Controller.Routers:
            print(router)
            
    @staticmethod
    def show_pcs():
        for pc in Controller.PCs:
            print(pc)