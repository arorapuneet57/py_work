import re
import os
import yaml
import sys
print "I am inside python now"
with open('%s' % sys.argv[1]) as fp:
   list= yaml.load(fp,  Loader=yaml.FullLoader)
   if sys.argv[1] == "/home/vagrant/worker_machine_non_dhcp.yaml":
       list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['ipAddrs'][0]='%s/24' % sys.argv[2]
       list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['nameservers'][0]='%s' % sys.argv[3]
       list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['gateway4']='%s' % sys.argv[4]
       list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['networkName']='%s' % sys.argv[5]
       list['items'][0].get('spec')['providerSpec']['value']['template']='%s' % sys.argv[7]
       list['items'][1].get('spec')['providerSpec']['value']['network']['devices'][0]['ipAddrs'][0]='%s/24' % sys.argv[6]
       list['items'][1].get('spec')['providerSpec']['value']['network']['devices'][0]['nameservers'][0]='%s' % sys.argv[3]
       list['items'][1].get('spec')['providerSpec']['value']['network']['devices'][0]['gateway4']='%s' % sys.argv[4]
       list['items'][1].get('spec')['providerSpec']['value']['network']['devices'][0]['networkName']='%s' % sys.argv[5]
       list['items'][1].get('spec')['providerSpec']['value']['template']='%s' % sys.argv[7]
       print list
   else:
       list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['ipAddrs'][0]='%s/24' % sys.argv[2]
       list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['nameservers'][0]='%s' % sys.argv[3]
       list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['gateway4']='%s' % sys.argv[4]
       list['items'][0].get('spec')['providerSpec']['value']['network']['devices'][0]['networkName']='%s' % sys.argv[5]
       list['items'][0].get('spec')['providerSpec']['value']['template']='%s' % sys.argv[6]
       print list

fp.close()
with open('%s' % sys.argv[1], 'w') as file:
    yaml.dump(list, file)
file.close()

