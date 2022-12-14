import backend.network.packet as netpac
import backend.network.devices as netdev
import backend.network.interface as netint


class Controller:
    @staticmethod
    def add_router(name=None):
        router = netdev.Router(name)
        return router

    @staticmethod
    def add_pc(name=None):
        pc = netdev.PC(name)
        return pc

    @staticmethod
    def add_interface(device: netdev.Device, intf_name: str, intf_ip_addr: str, intf_mask: str):
        device._add_interface(intf_name, intf_ip_addr, intf_mask)
        return device

    @staticmethod
    def add_gateway(pc: netdev.PC, ip_addr: str):
        pc.add_gateway(ip_addr)
        return pc

    @staticmethod
    def start_simulation():
        pass
