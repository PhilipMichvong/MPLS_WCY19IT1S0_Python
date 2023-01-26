import backend.network.packet as netpac
import backend.network.devices as netdev
import backend.network.interface as netint
import backend.network.net as netnet
import PIL.Image
import PIL.ImageTk
from tkinter import *
import pathlib
# from frontend.gui import GUI

class Controller:

    ROUTERS : netdev.Router = []
    PCS : netdev.PC = []

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

    # -- Add interface to `Controller.ROUTER[router_index]`
    @staticmethod
    def add_interface(app, router_index : int, intf_name: str, intf_ip_addr: str, intf_mask: str) -> None:
        log : str = ""
        try:
            Controller.ROUTERS[router_index].add_interface(intf_name, intf_ip_addr, intf_mask)
            log = f"{Controller.ROUTERS[router_index]._name} : Konfiguracja interfejsu wdrożona."
        except Exception as e:
            log = str(e)        
        finally:
            app.console_log(log)

    # -- Add gateway to `Controller.PCS[pc_index]`
    @staticmethod
    def add_gateway(app, pc_index : int, ip_addr: str) -> None:
        Controller.PCS[pc_index].add_gateway(ip_addr)
        log : str = ""
        try:
            Controller.PCS[pc_index].add_gateway(ip_addr)
            log = f"{Controller.PCS[pc_index]._name} : Brama domyślna skonfigurowana."
        except Exception as e:
            log = str(e)        
        finally:
            app.console_log(log)

    # -- Remove all created networks and devices
    @staticmethod
    def clear() -> None:
        netnet.Net.clear_networks()
        netdev.Device.clear_devices()
        Controller.PCS = []
        Controller.ROUTERS = []

    # --------------------------------------------

    # -- GUI Methods --
    '''
        TOPOLOGY:
                [PC1] -- [R1] --- [R2] -- [PC2]
                           |        |
                           |        |
                [PC4] -- [R4] --- [R3] -- [PC3]
            
            ADDRESS TABLE:
                LANs:
                    192.168.1.0 /24 | pc 10 | router 1
                    192.168.2.0 /24 | pc 10 | router 2
                    192.168.3.0 /24 | pc 10 | router 3
                    192.168.4.0 /24 | pc 10 | router 4
                    
                WANs:
                    172.16.0.0  /30
                    172.16.0.4  /30
                    172.16.0.8  /30
                    172.16.0.12 /30
    '''
    
    @staticmethod
    def mpls_start():
        # TODO
        #   [1]: TOPOLOGY
        #   [2]: Configuration
        #   [3]: RIP Distribution
        #   [4]: MPLS packet track
        pass
    
    @staticmethod
    def routers_add(app):
        r1 = Controller.add_router('R1')
        app.console_log(f'{r1._name} : Added.')
        
        r2 = Controller.add_router('R2')
        app.console_log(f'{r2._name} : Added.')
        
        r3 = Controller.add_router('R3')
        app.console_log(f'{r3._name} : Added.')
        
        r4 = Controller.add_router('R4')
        app.console_log(f'{r4._name} : Added.')
        
        Controller.ROUTERS = [r1, r2, r3, r4]
    
    @staticmethod
    def pcs_add(app):
        pc1 = Controller.add_pc('PC1')
        app.console_log(f'{pc1._name} : Added.')
        
        pc2 = Controller.add_pc('PC2')
        app.console_log(f'{pc2._name} : Added.')
        
        pc3 = Controller.add_pc('PC3')
        app.console_log(f'{pc3._name} : Added.')
        
        pc4 = Controller.add_pc('PC4')
        app.console_log(f'{pc4._name} : Added.')
        
        Controller.PCS = [pc1, pc2, pc3, pc4]
    
    @staticmethod
    def pc_configure(app, pc_index : int, gateway : str, ip_addr : str, mask : str):
        log : str = ""
        try:
            if Controller.PCS[pc_index].get_interfaces_count() != 0:
                Controller.PCS[pc_index].remove_interfaces()

            Controller.PCS[pc_index].add_interface("Fe0/0", ip_addr, mask)
            Controller.PCS[pc_index].add_gateway(gateway)
            log = f"{Controller.PCS[pc_index]._name} : Konfiguracja interfejsu wdrożona."
        except Exception as e:
            log = str(e)        
        finally:
            app.console_log(log)
    
    @staticmethod
    def load_default_config(app):
        Controller.clear()
        
        app.Devices_add()
        
        app.console_log("Konfiguracja domyślna w trakcie ładowania...")
        
        try:
            Controller.pc_configure(app, 0, '192.168.1.1', '192.168.1.10', '255.255.255.0')
            Controller.pc_configure(app, 1, '192.168.2.1', '192.168.2.10', '255.255.255.0')
            Controller.pc_configure(app, 2, '192.168.3.1', '192.168.3.10', '255.255.255.0')
            Controller.pc_configure(app, 3, '192.168.4.1', '192.168.4.10', '255.255.255.0')

            Controller.add_interface(app, 0, 'Fe0/0', '172.16.0.1', '255.255.255.252')
            Controller.add_interface(app, 0, 'Fe0/1', '172.16.0.14', '255.255.255.252')
            Controller.add_interface(app, 0, 'Fe0/2', '192.168.1.1', '255.255.255.0')

            Controller.add_interface(app, 1, 'Fe0/0', '172.16.0.2', '255.255.255.252')
            Controller.add_interface(app, 1, 'Fe0/1', '172.16.0.5', '255.255.255.252')
            Controller.add_interface(app, 1, 'Fe0/2', '192.168.2.1', '255.255.255.0')

            Controller.add_interface(app, 2, 'Fe0/0', '172.16.0.6', '255.255.255.252')
            Controller.add_interface(app, 2, 'Fe0/1', '172.16.0.9', '255.255.255.252')
            Controller.add_interface(app, 2, 'Fe0/2', '192.168.3.1', '255.255.255.0')

            Controller.add_interface(app, 3, 'Fe0/0', '172.16.0.10', '255.255.255.252')
            Controller.add_interface(app, 3, 'Fe0/1', '172.16.0.13', '255.255.255.252')
            Controller.add_interface(app, 3, 'Fe0/2', '192.168.4.1', '255.255.255.0')
            
            app.console_log("Konfiguracja domyślna załadowana.")
            
            global line, line2, line3, line4
            jpg_path = pathlib.Path.absolute(
                pathlib.Path('.\\frontend\\line.png')
            )
            jpg_path2 = pathlib.Path.absolute(
                pathlib.Path('.\\frontend\\line_hori.png')
            )
            img = PIL.Image.open(
                jpg_path)
            img2 = PIL.Image.open(
            jpg_path)
            img3 = PIL.Image.open(
            jpg_path2)
            img4 = PIL.Image.open(
            jpg_path2)
            line = PIL.ImageTk.PhotoImage(img)
            line2 = PIL.ImageTk.PhotoImage(img2)
            line3 = PIL.ImageTk.PhotoImage(img3)
            line4 = PIL.ImageTk.PhotoImage(img4)
            label_line = Label(image=line)
            label_line.place(x=274,y=115)
            label_line2 = Label(image=line2)
            label_line2.place(x=274, y=330)
            label_line3 = Label(image=line3)
            label_line3.place(x=230, y=150)
            label_line4 = Label(image=line4)
            label_line4.place(x=788, y =150)
            
        except Exception as e:
            print('load_default_config : Configuration error')
            print(type(e))
            print(e)
        
    # --------------------------------------------
    # -- TESTS --
    @staticmethod
    def integration_tests(app):
        tests_names = {
            0 : "Simple communication",
            1 : "RIP"
        }
        t1 = Controller.test_com()
        t2 = Controller.test_rip()
        
        T = [t1, t2]
        for i, t in enumerate(T):
            if t:
                log = f'Test[{i+1}] : {tests_names[i]} : Passed!'
                # print(f'Test[{i+1}] : {tests_names[i]} : Passed!')
            else:
                log = f'Test[{i+1}] : {tests_names[i]} : Not Passed!'
                # print(f'Test[{i+1}] : {tests_names[i]} : Not Passed!')
            app.console_log(log)
            
        if all(T):
            global line, line2, line3, line4
            jpg_path = pathlib.Path.absolute(
                pathlib.Path('.\\frontend\\line.png')
            )
            jpg_path2 = pathlib.Path.absolute(
                pathlib.Path('.\\frontend\\line_hori.png')
            )
            img = PIL.Image.open(
                jpg_path)
            img2 = PIL.Image.open(
            jpg_path)
            img3 = PIL.Image.open(
            jpg_path2)
            img4 = PIL.Image.open(
            jpg_path2)
            line = PIL.ImageTk.PhotoImage(img)
            line2 = PIL.ImageTk.PhotoImage(img2)
            line3 = PIL.ImageTk.PhotoImage(img3)
            line4 = PIL.ImageTk.PhotoImage(img4)
            label_line = Label(image=line)
            label_line.place(x=274,y=115)
            label_line2 = Label(image=line2)
            label_line2.place(x=274, y=330)
            label_line3 = Label(image=line3)
            label_line3.place(x=230, y=150)
            label_line4 = Label(image=line4)
            label_line4.place(x=788, y =150)
    
    @staticmethod
    def test_com():
        '''
            *** Scenario 1 ***
            [R1] --- [R2]
        '''
        try:
            addr_from   = Controller.ROUTERS[0].interfaces[0].address
            addr_to     = Controller.ROUTERS[1].interfaces[0].address
            mask_bits_from  = netnet.Net.get_mask_bits(Controller.ROUTERS[0].interfaces[0].mask)
            mask_bits_to    = netnet.Net.get_mask_bits(Controller.ROUTERS[1].interfaces[0].mask)
            
            packet = netpac.Packet(addr_from=addr_from, addr_to=addr_to,
                                   mask_bits_from=mask_bits_from, mask_bits_to=mask_bits_to,
                                   type=netpac.PACKET_TYPE.ICMP, data="REQ")

            Controller.ROUTERS[0].send_packet(packet)
            
        except Exception as e:
            print('test_simple_1 : Scenario 1 error')
            print(type(e))
            print(e)
            return False
        
        return True
    
    @staticmethod
    def test_rip():
        '''
            *** RIP DISTRIBUTION ***
        '''
        try:
            print('RIP DISTRIBUTION:\n')
            for _ in range(2):
                for router in Controller.ROUTERS:
                    router.rip_distribute()
                    
        except Exception as e:
            print('test_rip : RIP distribution Error')
            print(type(e))
            print(e)
            return False
        
        '''
            *** LDP DISTRIBUTION ***
        '''
        try:
            print('LDP DISTRIBUTION:\n')
            for _ in range(2):
                for router in Controller.ROUTERS:
                    router.ldp_distribute()
                    
        except Exception as e:
            print('test_rip : LDP distribution Error')
            print(type(e))
            print(e)
            return False
        
        '''
            *** AFTER LDP SHOWCASE ***
        '''
        try:
            print('\nAFTER RIP SHOWCASE:\n')
            print('ROUTERS - ROUTE TABLES:')
            for router in Controller.ROUTERS:
                print(router)
            
            print(40 * '-')
        except Exception as e:
            print('test_rip : After RIP Showcase error')
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
            addr_from   = Controller.PCS[0].interfaces[0].address
            addr_to     = Controller.PCS[1].interfaces[0].address
            mask_bits_from  = netnet.Net.get_mask_bits(Controller.PCS[0].interfaces[0].mask)
            mask_bits_to    = netnet.Net.get_mask_bits(Controller.PCS[1].interfaces[0].mask)
            
            packet = netpac.Packet(addr_from=addr_from, addr_to=addr_to,
                                   mask_bits_from=mask_bits_from, mask_bits_to=mask_bits_to,
                                   type=netpac.PACKET_TYPE.ICMP, data="REQ")
            print(40 * '-')

            Controller.PCS[0].send_packet(packet)
            
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
            addr_from   = Controller.PCS[0].interfaces[0].address
            addr_to     = Controller.PCS[3].interfaces[0].address
            mask_bits_from  = netnet.Net.get_mask_bits(Controller.PCS[0].interfaces[0].mask)
            mask_bits_to    = netnet.Net.get_mask_bits(Controller.PCS[3].interfaces[0].mask)
            
            packet = netpac.Packet(addr_from=addr_from, addr_to=addr_to,
                                   mask_bits_from=mask_bits_from, mask_bits_to=mask_bits_to,
                                   type=netpac.PACKET_TYPE.ICMP, data="REQ")
            print(40 * '-')

            Controller.PCS[0].send_packet(packet)
            
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
            addr_from   = Controller.PCS[0].interfaces[0].address
            addr_to     = Controller.PCS[2].interfaces[0].address
            mask_bits_from  = netnet.Net.get_mask_bits(Controller.PCS[0].interfaces[0].mask)
            mask_bits_to    = netnet.Net.get_mask_bits(Controller.PCS[2].interfaces[0].mask)
            
            packet = netpac.Packet(addr_from=addr_from, addr_to=addr_to,
                                   mask_bits_from=mask_bits_from, mask_bits_to=mask_bits_to,
                                   type=netpac.PACKET_TYPE.ICMP, data="REQ")
            print(40 * '-')

            Controller.PCS[0].send_packet(packet)
            
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
            for router in Controller.ROUTERS:
                print(router)
            
            print(40 * '-')
        except Exception as e:
            print('test_rip : After RIP Showcase error')
            print(type(e))
            print(e)
            return False
        
        return True
    
    # --------------------------------------------