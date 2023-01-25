import backend.network.packet as netpac
import backend.network.devices as netdev
import backend.network.interface as netint
import backend.network.net as netnet


class Controller:

    # OPERATIONS
    # -- Create new router
    @staticmethod
    def add_router(name=None) -> netdev.Router:
        router = netdev.Router(name)
        return router

    # -- Create new PC
    @staticmethod
    def add_pc(name=None, gateway=None) -> netdev.PC:
        pc = netdev.PC(name, gateway)
        return pc

    # -- Add interface to `device`
    @staticmethod
    def add_interface(device: netdev.Device, intf_name: str, intf_ip_addr: str, intf_mask: str) -> netdev.Device:
        device.add_interface(intf_name, intf_ip_addr, intf_mask)
        return device

    # -- Add gateway to `pc`
    @staticmethod
    def add_gateway(pc: netdev.PC, ip_addr: str) -> netdev.PC:
        pc.add_gateway(ip_addr)
        return pc

    # -- Remove all created networks and devices
    @staticmethod
    def clear() -> None:
        netnet.Net.clear_networks()
        netdev.Device.clear_devices()

    # --------------------------------------------

    # -- SIMULATION --
    @staticmethod
    def start_simulation():
        # TODO
        #   [1]: TOPOLOGY
        #   [2]: Configuration
        #   [3]: RIP Distribution
        #   [4]: MPLS packet track
        pass
    
    # --------------------------------------------
    
    # -- TESTS --
    # -- RIP Protocol test
    @staticmethod
    def test_rip():
        '''
            TOPOLOGY:
                [PC1] -- [R1] --- [R2] -- [PC2]
                           |        |
                           |        |
                [PC4] -- [R4] --- [R3] -- [PC3]
            
            ADDRESS TABLE:
                LANs:
                    192.168.1.0 /24 | pc 10 | router 1
                    192.168.2.0 /24 | pc 10 | router 1
                    192.168.3.0 /24 | pc 10 | router 1
                    192.168.4.0 /24 | pc 10 | router 1
                    
                WANs:
                    172.16.0.0  /30
                    172.16.0.4  /30
                    172.16.0.8  /30
                    172.16.0.12 /30
            
            SCENARIOS:
                1) PC1 -> PC2
                2) PC1 -> PC4
                3) PC1 -> PC3
        '''

        '''
            *** Configuration ***
        '''
        try:
            r1 = Controller.add_router('R1')
            r2 = Controller.add_router('R2')
            r3 = Controller.add_router('R3')
            r4 = Controller.add_router('R4')
        
            pc1 = Controller.add_pc('PC1', gateway='192.168.1.1')
            pc2 = Controller.add_pc('PC2', gateway='192.168.2.1')
            pc3 = Controller.add_pc('PC3', gateway='192.168.3.1')
            pc4 = Controller.add_pc('PC4', gateway='192.168.4.1')

            pc1 = Controller.add_interface(pc1, 'Fe0/0', '192.168.1.10', '255.255.255.0')
            pc2 = Controller.add_interface(pc2, 'Fe0/0', '192.168.2.10', '255.255.255.0')
            pc3 = Controller.add_interface(pc3, 'Fe0/0', '192.168.3.10', '255.255.255.0')
            pc4 = Controller.add_interface(pc4, 'Fe0/0', '192.168.4.10', '255.255.255.0')

            r1 = Controller.add_interface(r1, 'Fe0/0', '172.16.0.1', '255.255.255.252')
            r1 = Controller.add_interface(r1, 'Fe0/1', '172.16.0.14', '255.255.255.252')
            r1 = Controller.add_interface(r1, 'Fe0/2', '192.168.1.1', '255.255.255.0')

            r2 = Controller.add_interface(r2, 'Fe0/0', '172.16.0.2', '255.255.255.252')
            r2 = Controller.add_interface(r2, 'Fe0/1', '172.16.0.5', '255.255.255.252')
            r2 = Controller.add_interface(r2, 'Fe0/2', '192.168.2.1', '255.255.255.0')

            r3 = Controller.add_interface(r3, 'Fe0/0', '172.16.0.6', '255.255.255.252')
            r3 = Controller.add_interface(r3, 'Fe0/1', '172.16.0.9', '255.255.255.252')
            r3 = Controller.add_interface(r3, 'Fe0/2', '192.168.3.1', '255.255.255.0')

            r4 = Controller.add_interface(r4, 'Fe0/0', '172.16.0.10', '255.255.255.252')
            r4 = Controller.add_interface(r4, 'Fe0/1', '172.16.0.13', '255.255.255.252')
            r4 = Controller.add_interface(r4, 'Fe0/2', '192.168.4.1', '255.255.255.0')
        except Exception as e:
            print('test_rip : Configuration error')
            print(type(e))
            print(e)
            return False
        
        # ---------------------------------------------------------------------------------
        '''
            *** SHOWCASE ***
        '''
        try:
            print('\nSHOWCASE:\n')
            netnet.Net.show_networks()
            print()
            print(40 * '-')

            print('DEVICES:\n')
            print(pc1)
            print(pc2)
            print(pc3)
            print(pc4)
            
            print(40 * '-')
        
            print(r1)
            print(r2)
            print(r3)
            print(r4)
            
            print(40 * '-')
        except Exception as e:
            print('test_rip : Showcase error')
            print(type(e))
            print(e)
            return False
        
        
        '''
            *** RIP DISTRIBUTION ***
        '''
        try:
            print('RIP DISTRIBUTION:\n')
            routers = [r1, r2, r3, r4]
            for _ in range(2):
                for router in routers:
                    router.rip_distribute()
                    
        except Exception as e:
            print('test_rip : RIP distribution Error')
            print(type(e))
            print(e)
            return False
        
        # ---------------------------------------------------------------------------------
        '''
            *** Scenario 1 ***
                PC1 -> PC2
        '''
        try:
            print('\nSCENARIO 1:')
            packet = netpac.Packet(addr_from='192.168.1.10', addr_to='192.168.2.10', mask_bits_from=24, mask_bits_to=24, type=netpac.PACKET_TYPE.MPLS, data='TEST MPLS')

            print(40 * '-')

            pc1.send_packet(packet)
            
        except Exception as e:
            print('test_rip : Scenario 1 error')
            print(type(e))
            print(e)
            return False
        
        # ---------------------------------------------------------------------------------
        
        '''
            *** Scenario 2 ***
                PC1 -> PC4
        '''
        try:
            print('\nSCENARIO 2:')
            packet = netpac.Packet(addr_from='192.168.1.10', addr_to='192.168.4.10', mask_bits_from=24, mask_bits_to=24, type=netpac.PACKET_TYPE.MPLS, data='TEST MPLS')

            print(40 * '-')

            pc1.send_packet(packet)
            
        except Exception as e:
            print('test_rip : Scenario 2 error')
            print(type(e))
            print(e)
            return False
        
        # ---------------------------------------------------------------------------------
        
        '''
            *** Scenario 3 ***
                PC1 -> PC3
        '''
        try:
            print('\nSCENARIO 3:')
            packet = netpac.Packet(addr_from='192.168.1.10', addr_to='192.168.3.10', mask_bits_from=24, mask_bits_to=24, type=netpac.PACKET_TYPE.MPLS, data='TEST MPLS')

            print(40 * '-')

            pc1.send_packet(packet)
            
        except Exception as e:
            print('test_rip : Scenario 3 error')
            print(type(e))
            print(e)
            return False
        
        # ---------------------------------------------------------------------------------
        
        '''
            *** AFTER RIP SHOWCASE ***
        '''
        try:
            print('\nAFTER RIP SHOWCASE:\n')
            print('ROUTERS - ROUTE TABLES:')
            for router in routers:
                print(router)
            
            print(40 * '-')
        except Exception as e:
            print('test_rip : After RIP Showcase error')
            print(type(e))
            print(e)
            return False
        
        return True
    
    # -- Broadcast packet test
    @staticmethod
    def test_broadcast() -> bool:
        '''
            TOPOLOGY:
                [PC1] - |
                [PC2] - + --- [R1]
                [PC3] - |
        '''
        
        '''
            *** Configuration ***
        '''
        try:
            # Router
            r1 = Controller.add_router('R1')
            r1 = Controller.add_interface(r1, 'Fe0/0', '192.168.1.1', '255.255.255.0')

            # PCs
            pc1 = Controller.add_pc('PC1', gateway='192.168.1.1')
            pc2 = Controller.add_pc('PC2', gateway='192.168.1.1')
            pc3 = Controller.add_pc('PC3', gateway='192.168.1.1')

            pc1 = Controller.add_interface(pc1, 'Fe0/0', '192.168.1.11', '255.255.255.0')
            pc2 = Controller.add_interface(pc2, 'Fe0/0', '192.168.1.12', '255.255.255.0')
            pc3 = Controller.add_interface(pc3, 'Fe0/0', '192.168.1.13', '255.255.255.0')
        except Exception as e:
            print('test_broadcast : Configuration error')
            print(type(e))
            print(e)
            return False
        # ---------------------------------------------------------------------------------
        '''
            *** SHOWCASE ***
        '''
        try:
            print('SHOWCASE:\n')
            netnet.Net.show_networks()
            print()
            print(40 * '-')

            print('DEVICES:\n')
            print(pc1)
            print(pc2)
            print(pc3)
            print(r1)
            print()
            print(40 * '-')
        except Exception as e:
            print('test_broadcast : Showcase error')
            print(type(e))
            print(e)
            return False
        
        # ---------------------------------------------------------------------------------
        '''
            *** SCENARIO 1 ***
        '''
        try:
            print('SCENARIO 1:\n')
            packet = netpac.Packet(addr_from='192.168.1.10', addr_to='192.168.1.255', mask_bits_from=24, mask_bits_to=24, type=netpac.PACKET_TYPE.MPLS, data='TEST BROADCAST')

            pc1.send_packet(packet)
        except Exception as e:
            print('test_broadcast : Scenario 1 error')
            print(type(e))
            print(e)
            return False
        
        return True
            
    # -- Simple communication test
    @staticmethod
    def test_simple_1() -> bool:
        '''
            TOPOLOGY:
                [PC1] -- [R1] --- [R2] -- [PC2]
            
            SCENARIOS:
                1)  R1 -> R2        SUCCESS
                2)  PC1 -> R2       SUCCESS
        '''
        
        '''
            *** Configuration ***
        '''
        try:
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
        except Exception as e:
            print('test_simple_1 : Configuration error')
            print(type(e))
            print(e)
            return False
        
        # ---------------------------------------------------------------------------------
        '''
            *** SHOWCASE ***
        '''
        try:
            print('SHOWCASE:\n')
            netnet.Net.show_networks()
            print()
            print(40 * '-')

            print('DEVICES:\n')
            print(pc1)
            print(pc2)
            print(r1)
            print(r2)
            print()
            print(40 * '-')
            
        except Exception as e:
            print('test_simple_1 : Showcase error')
            print(type(e))
            print(e)
            return False
        
        # ---------------------------------------------------------------------------------
        '''
            *** Scenario 1 ***
        '''
        try:
            print('SCENARIO 1:\n')
            packet = netpac.Packet(addr_from='172.16.0.2', addr_to='172.16.0.1', mask_bits_from=30, mask_bits_to=30, type=netpac.PACKET_TYPE.MPLS, data='TEST MPLS')

            print()
            print(40 * '-')

            r2.send_packet(packet)
            
        except Exception as e:
            print('test_simple_1 : Scenario 1 error')
            print(type(e))
            print(e)
            return False
        
        # ---------------------------------------------------------------------------------
        '''
            *** Scenario 2 ***
        '''
        try:
            print('SCENARIO 2:\n')
            packet = netpac.Packet(addr_from='192.168.1.10', addr_to='172.16.0.2', mask_bits_from=24, mask_bits_to=24, type=netpac.PACKET_TYPE.MPLS, data='TEST MPLS')

            # ---------------------------------------------------------------------------------
            print()
            print(40 * '-')

            pc1.send_packet(packet)
            
        except Exception as e:
            print('test_simple_1 : Scenario 2 error')
            print(type(e))
            print(e)
            return False
        
        return True
