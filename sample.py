import re
import os
"""
DHCP="false"
SERVERIP="10.3.2.1"
filepath1='prov.ini'

GATEWAY_IP
filepath="final.yaml"
if DHCP is not 'true':
   print('hi')
   with open(filepath) as fp:
      line = fp.readline()
      cnt = 1
      while line:    
          if re.search(r'gateway4', line):
               if re.sub('gateway4: ','gateway4: %s', line) % GATEWAY_IP
               break
          line = fp.readline()
          cnt+=1
fp.close()
"""
import yaml
import sys
with open('/home/vagrant/machine_non_dhcp.yaml') as fp:
    list= yaml.load(fp,  Loader=yaml.FullLoader)
    print list
    list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['ipAddrs'][0]='%s/24' % sys.argv[1]
    list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['nameservers'][0]='%s' % sys.argv[2]
    list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['gateway4']='%s' % sys.argv[3]
    list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['networkName']='%s' % sys.argv[4]

fp.close()
with open('/home/vagrant/machine_non_dhcp.yaml', 'w') as file:
    yaml.dump(list, file)
file.close()
