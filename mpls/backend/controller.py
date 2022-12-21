import backend.network.packet as netpac
import backend.network.devices as netdev
import backend.network.interface as netint
import backend.network.net as netnet


class Controller:

    @staticmethod
    def add_router(name=None) -> netdev.Router:
        router = netdev.Router(name)
        return router

    @staticmethod
    def add_pc(name=None) -> netdev.PC:
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
    
    @staticmethod
    def test_simulation():
        '''
            [PC1] -- [R1] --- [R2] -- [PC2]
            
            1)  R1 -> R2        Done
            2)  PC1 -> R2       Done
            3)  PC1 -> PC2      R1 cannot delivered packet - RIP is needed
        '''
        
        '''
            *** Configuration ***
        '''
        # Create 2 routers
        r1 = Controller.add_router('R1')
        r2 = Controller.add_router('R2')
        
        # Create 2 pcs
        pc1 = Controller.add_pc('PC1')
        pc2 = Controller.add_pc('PC2')
        
        # Add interfaces
        r1 = Controller.add_interface(r1, 'Fe0/0', '172.16.0.1', '255.255.255.252')
        r1 = Controller.add_interface(r1, 'Fe0/1', '192.168.1.1', '255.255.255.0')
        
        r2 = Controller.add_interface(r2, 'Fe0/0', '172.16.0.2', '255.255.255.252')
        r2 = Controller.add_interface(r2, 'Fe0/1', '192.168.2.1', '255.255.255.0')
        
        pc1 = Controller.add_interface(pc1, 'Fe0/0', '192.168.1.10', '255.255.255.0')
        
        pc2 = Controller.add_interface(pc2, 'Fe0/0', '192.168.2.10', '255.255.255.0')
        
        # Add gateways
        pc1 = Controller.add_gateway(pc1, '192.168.1.1')
        pc2 = Controller.add_gateway(pc2, '192.168.2.1')
        
        # ---------------------------------------------------------------------------------
       
        
        # ---------------------------------------------------------------------------------
        '''
            *** SHOWCASE ***
        '''
        netnet.Net.show_networks()
        print()
        print(40 * '-')
        
        print(pc1)
        print(pc2)
        print(r1)
        print(r2)
        
        # ---------------------------------------------------------------------------------
        '''
            *** Scenario 1 ***
        '''
        packet = netpac.Packet(addr_from='172.16.0.1', addr_to='172.16.0.2', mask_bits_from=30, mask_bits_to=30, type=netpac.PACKET_TYPE.MPLS, data='TEST MPLS')
        
        print()
        print(40 * '-')
        
        r1.send_packet(packet)
        
        # ---------------------------------------------------------------------------------
        '''
            *** Scenario 2 ***
        '''
        packet = netpac.Packet(addr_from='192.168.1.10', addr_to='172.16.0.2', mask_bits_from=24, mask_bits_to=24, type=netpac.PACKET_TYPE.MPLS, data='TEST MPLS')
        
        # ---------------------------------------------------------------------------------
        print()
        print(40 * '-')
        
        pc1.send_packet(packet)
        
        # ---------------------------------------------------------------------------------
        '''
            *** Scenario 3 ***
        '''
        packet = netpac.Packet(addr_from='192.168.1.10', addr_to='192.168.2.10', mask_bits_from=24, mask_bits_to=24, type=netpac.PACKET_TYPE.MPLS, data='TEST MPLS')
        
        # ---------------------------------------------------------------------------------
        print()
        print(40 * '-')
        
        try:
            pc1.send_packet(packet)
        except ValueError as e:
            print(e)
