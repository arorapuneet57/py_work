import requests
import ssl

# Write this line before creating pyVmomi session
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

from pyVim.connect import SmartConnect
from pyVmomi import vim
si = SmartConnect(host='10.186.76.20',
                               user='administrator@vsphere.local',
                               pwd='Admin!23',
                               port=int(443))

content = si.RetrieveContent()
opaque_1 = vim.vm.device.VirtualEthernetCard.OpaqueNetworkBackingInfo
rootFolder = content.rootFolder
o = si.content.viewManager.CreateContainerView(rootFolder, [vim.HostSystem], True)
network_info = o.view[0].configManager.networkSystem.networkInfo
print("network_info puneet %s" % network_info)
opqaue_network = network_info.opaqueNetwork
print("opqaue network puneet %s" % opqaue_network)
import pdb;pdb.set_trace()
pg_list = o.view[0].network

if pg_list is not None:
    for dvpg in pg_list:
        if (hasattr(dvpg, 'config')):
            import pdb;pdb.set_trace();
            print(dvpg.config.logicalSwitchUuid)
            print(dvpg)