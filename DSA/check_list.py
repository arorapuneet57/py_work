out = ['L4', '00:50:56:ab:37:81', '00:50:56:ab:83:b7', '0', '10', '172.16.1.11', '172.16.1.12', '17', '0', '49164', '49164', 'OL;', 'bmap:0x12000c0', 'inval(s):120', 'cg:1045', 'dp:0x8', 'len:704;', 'DFW', 'on', 'srcPort;', 'VNI:', '66561;', 'DFW', 'on', 'dstPort;', '0', '0']
out = ['L4', '02:50:56:56:44:52', '00:50:56:ab:31:7f', 'OL', '0', '5', '172.16.2.14', '172.16.1.12', '1', '0', '0', '0', 'bmap:0x12800c2', 'inval(s):127', 'cg:1045', 'dp:0x8', 'len:814;', 'DFW', 'on', 'srcPort;', 'VDR', 'inst:', '1;', 'INST', '1:', '0x2;', 'VNI:', '66561;', 'DFW', 'on', 'dstPort;', '0', '0']
check = [True for c in out if 'OL' in c]
if check:
    print(check)


