def is_reachable(ip, port):
    import pdb;pdb.set_trace()
    flag = False
    if type(port) is int:
         flag = True
    elif type(port) is list:
        for port_num in port:
           flag = False
    return flag


print(is_reachable('1.1.2.3', port=[22,33]))

