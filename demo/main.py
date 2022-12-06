import network.net as nnet
from controller import Controller

intf_name_0 = 'Fe0/0'
intf_name_1 = 'Fe0/1'
intf_name_2 = 'Fe0/2'

    
def main():
    
    # Adding devices
    for i in range(4):
        Controller.add_pc()
        Controller.add_router(f'R{i+1}')

    # Adding interfaces for pcs
    for i, pc in enumerate(Controller.PCs):
        intf_addr = f'172.16.{i+1}.10'
        intf_mask = nnet.MASK[24]
        gateway_addr = f'172.16.{i+1}.1'
        pc._add_interface(intf_name_0, intf_addr, intf_mask)
        pc.add_gateway(gateway_addr)
    
    # Adding interfaces for routers
    for i, router in enumerate(Controller.Routers):
        intf_addr_0 = f'172.16.{i+1}.1'
        intf_addr_1 = f'10.0.{i+1}.1'
        intf_addr_2 = f'10.0.{len(Controller.Routers)-i}.2'
        
        router._add_interface(intf_name_0, intf_addr_0, nnet.MASK[24])
        router._add_interface(intf_name_1, intf_addr_1, nnet.MASK[30])
        router._add_interface(intf_name_2, intf_addr_2, nnet.MASK[30])
    
    print('\n' + 60 * '*' + '\n')
    
    nnet.Net.show_networks()
    
    print('\n' + 60 * '*' + '\n')
    print('ROUTERS:')
    
    Controller.show_routers()

    print('\n' + 60 * '*' + '\n')
    print('PCs:')
    
    Controller.show_pcs()
    
    
if __name__ == '__main__':
    main()
    print()