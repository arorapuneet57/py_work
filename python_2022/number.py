"""
uplink_name = 'www\n'
port_id = 'dddd\n'
dvs_name = 'dddvf'
command = "esxcfg-vswitch -Q %s -V %s %s" % (uplink_name.strip('\n'),
                        port_id.strip('\n'), dvs_name.strip('\n'))


print(command)
"""

info = '{"DvsPortset-0": {"dvsName": "50 2a 71 6a cd 25 db ae-e6 62 43 cb b8 10 a6 8d", "alias": "1-vds-1171", "portCount": {"numPorts": 2060, "numAvailablePorts": 2042}}}'


import json
out = json.loads(info)
print(out.get("DvsPortset-0")['alias'])
print(info)



