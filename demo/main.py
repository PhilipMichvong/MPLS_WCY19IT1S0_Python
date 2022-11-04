import Network as nw

def main():
    p_addr_from = "10.6.9.20"
    p_addr_to = "10.6.9.21"
    p_type = 'MPLS'
    p_data = "Info"
    
    packet = nw.Packet(p_addr_from, p_addr_to, p_type, p_data)
    # print(packet)
    
    intf1 = nw.Interface("Fe0/1", p_addr_from)
    intf2 = nw.Interface("Fe0/1", p_addr_to)
    
    r1 = nw.Router(name="R1", interfaces=[intf1])
    r2 = nw.Router(name="R2", interfaces=[intf2])
    
    r1.route_table.append(intf2.address)
    r2.route_table.append(intf1.address)
    
    for router in nw.Router.router_list:
        print(router)
        
    r1.send_packet(packet)
    
    
if __name__ == '__main__':
    main()