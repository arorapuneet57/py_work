import re
import os, time

def check_OL_HW_counters(dump, hw_counter_set1=0, hw_counter_set2=0):
    actions = dump.get('actions')
    actions_values = actions.split()
    hw_counters1, hw_counters2 = int(actions_values[-1]), int(actions_values[-2])

    if hw_counters1 > hw_counter_set1 and hw_counters2 > hw_counter_set2:
        print("counters incrementing")
        return hw_counters1, hw_counters2
    else:
        raise Exception("counters not incrementing")

def get_matched_pattern(py_dicts, src_ip=None, dst_ip=None, src_mac=None, dst_mac=None):
    L2_Traffic_IN_SAME_SUB_REGEX = 'OL.*bmap.*cg.*dp.*VNI'
    ICMP_Traffic_IN_SAME_SUB_REGEX = 'bmap.*cg.*dp'
    L3_Traffic_IN_DIFF_SUB_VIA_TIER1_REGEX = 'OL.*bmap.*cg.*dp.*VDR.*VNI'
    for rule in py_dicts:
        print(" rule %s " % rule)
        # Check L2 offload over smartnic
        rule_type = ['L2', 'L3', 'L4']
        for r_type in rule_type:
            if r_type in rule.get('FT'.casefold()):
                if src_ip and src_mac:
                    print("Test-flow Rule to check %s" % rule)
                    if src_ip in rule.get('srcIP'.casefold()) and \
                            dst_ip in rule.get('dstIP'.casefold()):
                        import pdb;
                        pdb.set_trace()
                        if int(rule.get('proto')) == 1:
                            print("enter 1 ")
                            OL = (re.search(ICMP_Traffic_IN_SAME_SUB_REGEX, rule.get('actions')))
                            if OL:
                                pylogger.info("SW PING OL done over smartnic for L3 %s" % OL.group(0))
                                return rule, True
                        else:

                            print("enter 2 ")
                            OL = (re.search(
                                L3_Traffic_IN_DIFF_SUB_VIA_TIER1_REGEX,
                                rule.get('actions')) or re.search(
                                L2_Traffic_IN_SAME_SUB_REGEX,
                                rule.get('actions')))
                            if src_mac in rule.get('srcMAC'.casefold()) or \
                                    dst_mac in rule.get('dstMAC'.casefold()):
                                print("enter 3 ")
                                # if re.match(
                                #    r".*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.*",
                                #    rule.get('srcIP'.casefold())):
                                OL1 = re.search(
                                    L3_Traffic_IN_DIFF_SUB_VIA_TIER1_REGEX,
                                    rule.get('actions')) or re.search(
                                    L2_Traffic_IN_SAME_SUB_REGEX,
                                    rule.get('actions'))
                                if OL1 and OL:
                                    print(
                                        "OL done over smartnic for L3 %s" %
                                        OL.group(0))
                                    return rule, True
                    if src_ip and src_mac is None:
                        print("Test-flow Rule to check %s" % rule)
                        if src_ip in rule.get('srcIP'.casefold()) and \
                                dst_ip in rule.get('dstIP'.casefold()):
                            if int(rule.get('proto')) == 1:
                                print("enter 4 ")
                                OL = (re.search(
                                    ICMP_Traffic_IN_SAME_SUB_REGEX,
                                    rule.get('actions')))
                                if OL:
                                    print(
                                        "SW PING OL done over smartnic for L3 %s" %
                                        OL.group(0))
                                    return rule, True
                            else:
                                OL = (re.search(
                                    L3_Traffic_IN_DIFF_SUB_VIA_TIER1_REGEX,
                                    rule.get('actions')) or re.search(
                                    L2_Traffic_IN_SAME_SUB_REGEX,
                                    rule.get('actions')))
                                if OL:
                                    print(
                                        "OL done over smartnic for L3 %s" %
                                        OL.group(0))
                                    return rule, True
    return rule, False

def get_smartnic_ens_flow(src_ip=None, dst_ip=None,
                          src_mac=None, dst_mac=None,
                          get_smartnic_ens_flow=None):
        # Check flow rules for 120 seconds if not found
        for lapse in range(1, 7):
            flag = False
            #py_dicts = [{'ft': 'L4', 'dstmac': '00:50:56:ab:1a:dd', 'srcmac': '00:50:56:ab:83:b7', 'vlan': '0', 'srcport': '10', 'srcip': '172.16.1.11', 'dstip': '172.16.1.23', 'proto': '17', 'vni': '0', 'srcport/type': '49162', 'dstport/code': '49162', 'actions': 'OL; bmap:0x12000c0 inval(s):108 cg:1045 dp:0xf len:704; DFW on srcPort; VNI: 66561; DFW on dstPort;   1  2'}]
            py_dicts = [{'ft': 'L4', 'dstmac': '00:50:56:ab:37:81', 'srcmac': '00:50:56:ab:83:b7', 'vlan': '0', 'srcport': '10', 'srcip': '172.16.1.11', 'dstip': '172.16.1.12', 'proto': '17', 'vni': '0', 'srcport/type': '49164', 'dstport/code': '49164', 'actions': 'bmap:0x12000c0 inval(s):120 cg:1045 dp:0x8 len:704; DFW on srcPort; VNI: 66561; DFW on dstPort;   0  0'}]
            print("puneet1 py_dicts  %s " % py_dicts)
            if py_dicts:

                rule, pattern = get_matched_pattern(py_dicts, src_ip, dst_ip, src_mac, dst_mac)
                if pattern:
                    hw_counters1, hw_counters2 = check_OL_HW_counters(rule, 0, 0)
                    if hw_counters1 and hw_counters2:
                        time.sleep(10)
                        py_dicts = [{'ft': 'L4', 'dstmac': '00:50:56:ab:1a:dd', 'srcmac': '00:50:56:ab:83:b7', 'vlan': '0', 'srcport': '10', 'srcip': '172.16.1.11', 'dstip': '172.16.1.23', 'proto': '17', 'vni': '0', 'srcport/type': '49162', 'dstport/code': '49162', 'actions': 'OL; bmap:0x12800c2 inval(s):114 cg:1045 dp:0x5 len:814; DFW on srcPort; VDR inst: 1; INST 1: 0x2; VNI: 71680; DFW on dstPort;   3  4'}]
#                        py_dicts = {'ft': 'L4', 'dstmac': '02:50:56:56:44:52', 'srcmac': '00:50:56:ab:37:81', 'vlan': '0', 'srcport': '8', 'srcip': '172.16.1.12', 'dstip': '172.16.2.14', 'proto': '17', 'vni': '0', 'srcport/type': '49162', 'dstport/code': '49162', 'actions': 'OL; bmap:0x12800c2 inval(s):114 cg:1045 dp:0x5 len:814; DFW on srcPort; VDR inst: 1; INST 1: 0x2; VNI: 71680; DFW on dstPort;   0  0'}
                        #py_dicts = [{'ft': 'L4', 'dstmac': '02:50:56:56:44:52', 'srcmac': '00:50:56:ab:ae:08', 'vlan': '0', 'srcport': '4', 'srcip': '172.17.1.15', 'dstip': '172.17.2.18', 'proto': '17', 'vni': '0', 'srcport/type': '49162', 'dstport/code': '49162', 'actions': 'OL; bmap:0x12800c2 inval(s):93 cg:1045 dp:0x10 len:814; DFW on srcPort; VDR inst: 1; INST 1: 0x3; VNI: 70656; DFW on dstPort;   0  0'}]
                        rule, pattern = get_matched_pattern(py_dicts, src_ip, dst_ip, src_mac, dst_mac)
                        if pattern:
                            flag = True
                            if check_OL_HW_counters(rule, hw_counters1, hw_counters1):
                                break
                        else:
                            flag = False
                            print("OL not done for rule %s" % rule)
            # Check flow rules for 120 secds if not found
            time.sleep(20)
            if flag is False:
                print("Flow rules not available over smartnic xxxxxxxxxx !!")
                continue
            else:
                break
        if flag:
            return {'flow_rules': True}
        else:
            return {'flow_rules': False}


get_smartnic_ens_flow(src_ip='172.16.1.11', dst_ip='172.16.1.12', src_mac='00:50:56:ab:83:b7', dst_mac='00:50:56:ab:37:81')