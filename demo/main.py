import network.net as nnet
from controller import Controller


intf_name_0 = 'Fe0/0'
intf_name_1 = 'Fe0/1'
intf_name_2 = 'Fe0/2'

    
def main():
    pcs = []
    routers = []
    
    # Adding devices
    for i in range(4):
        pcs.append(Controller.add_pc(f'Pecet{i+1}'))
        routers.append(Controller.add_router(f'R{i+1}'))

    # Adding interfaces for pcs
    for i, pc in enumerate(pcs):
        intf_addr = f'172.16.{i+1}.10'
        intf_mask = nnet.MASK[24]
        gateway_addr = f'172.16.{i+1}.1'
        pc = Controller.add_interface(pc, intf_name_0, intf_addr, intf_mask)
        pc = Controller.add_gateway(pc, gateway_addr)
    
    # Adding interfaces for routers
    for i, router in enumerate(routers):
        intf_addr_0 = f'172.16.{i+1}.1'
        intf_addr_1 = f'10.0.{i+1}.1'
        intf_addr_2 = f'10.0.{len(routers)-i}.2'
        
        router = Controller.add_interface(router, intf_name_0, intf_addr_0, nnet.MASK[24])
        router = Controller.add_interface(router, intf_name_1, intf_addr_1, nnet.MASK[30])
        router = Controller.add_interface(router, intf_name_2, intf_addr_2, nnet.MASK[30])
    
    print('\n' + 60 * '*' + '\n')
    
    nnet.Net.show_networks()
    
    print('\n' + 60 * '*' + '\n')
    print('ROUTERS:')
    
    for router in routers:
        print(router)

    print('\n' + 60 * '*' + '\n')
    print('PCs:')
    
    for pc in pcs:
        print(pc)
    
    
if __name__ == '__main__':
    main()
    print()