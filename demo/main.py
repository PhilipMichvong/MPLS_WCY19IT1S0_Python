import network.packet as netpac
import network.devices as netdev
import network.net as nnet

intf_name_0 = 'Fe0/0'
intf_name_1 = 'Fe0/1'
intf_name_2 = 'Fe0/2'

    
def main():
    
    pc1 = netdev.PC()
    pc2 = netdev.PC()
    pc3 = netdev.PC()
    pc4 = netdev.PC()
    
    r1 = netdev.Router('R1')
    r2 = netdev.Router('R2')
    r3 = netdev.Router('R3')
    r4 = netdev.Router('R4')
    
    PCs = [pc1, pc2, pc3, pc4]
    for i, pc in enumerate(PCs):
        intf_addr = f'10.0.{i+1}.10'
        intf_mask = nnet.MASK[24]
        pc._add_interface(intf_name_0, intf_addr, intf_mask)
        
    Routers = [r1, r2, r3, r4]
    for i, router in enumerate(Routers):
        intf_addr_0 = f'10.0.{i+1}.1'
        intf_addr_1 = f'172.16.{i+1}.1'
        intf_addr_2 = f'172.16.{len(Routers)-i}.2'
        
        router._add_interface(intf_name_0, intf_addr_0, nnet.MASK[24])
        router._add_interface(intf_name_1, intf_addr_1, nnet.MASK[30])
        router._add_interface(intf_name_2, intf_addr_2, nnet.MASK[30])
    
    print('\n' + 60 * '*' + '\n')
    
    nnet.Net.show_networks()
    
    print(r1)
    
    
if __name__ == '__main__':
    main()
    print()