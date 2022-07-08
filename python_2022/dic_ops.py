from collections import OrderedDict
dic  = OrderedDict()
import pdb;pdb.set_trace()
out = 'PortNum          Type SubType SwitchName       MACAddress         ClientName\n2248146958          4       0 vSwitch0         bc:97:e1:d3:42:40  vmnic0\n100663316           3       0 vSwitch0         bc:97:e1:d3:42:40  vmk0\n100663335           5       9 vSwitch0         00:50:56:99:db:d6  6-vm-ubuntu-18.04-server-amd64-local-1196-01964aa9-e913-47f9-8439-80a4f5a59458\n100663337           5       9 vSwitch0         00:50:56:99:49:a6  2-vm-ubuntu-18.04-server-amd64-local-1196-2fbc6754-d320-4b22-a751-50149f3fe6e8\n100663339           5       9 vSwitch0         00:50:56:99:b8:c1  1-vm-ubuntu-18.04-server-amd64-local-1196-db522d61-3cb5-4971-916f-ebb06125a739\n100663341           5       9 vSwitch0         00:50:56:99:97:c5  5-vm-ubuntu-18.04-server-amd64-local-1196-0d0f77c5-6e27-4dba-aa00-77dfa723c181\n2281701400          4       0 vSwitchBMC       b0:7b:25:d7:19:77  vusb0\n134217754           3       0 vSwitchBMC       b0:7b:25:d7:19:77  vmk1\n2315255836          4       0 DvsPortset-0     00:ae:cd:f6:3c:41  vmnic5\n167772198           5       9 DvsPortset-0     00:50:56:99:5d:51  6-vm-ubuntu-18.04-server-amd64-local-1196-01964aa9-e913-47f9-8439-80a4f5a59458.eth1\n167772200           5       9 DvsPortset-0     00:50:56:99:e3:6c  2-vm-ubuntu-18.04-server-amd64-local-1196-2fbc6754-d320-4b22-a751-50149f3fe6e8.eth1\n167772202           5       9 DvsPortset-0     00:50:56:99:bd:5f  1-vm-ubuntu-18.04-server-amd64-local-1196-db522d61-3cb5-4971-916f-ebb06125a739.eth1\n167772204           5       9 DvsPortset-0     00:50:56:99:3c:80  5-vm-ubuntu-18.04-server-amd64-local-1196-0d0f77c5-6e27-4dba-aa00-77dfa723c181.eth1\n'
p_li = []
check = []
check = out.split('\n')
new_item = check[0]
p_li = check[1:]

count = 0
dic1 = dict()
for r in new_item.split()[count:count+1]:
    for i in p_li:
        for num in i.split()[count:count+1]:
            #dic[r] = num
            dic1[r].append(num)
            #dic.append(r) = num
    count += 1