import re
import time

class SMARTNIC(object):
    @classmethod
    def get_flow_dump_dict(cls, ssh, client_object, OL_FLOW_DUMP_REGEX, PING_FLOW_DUMP_REGEX):
        py_dicts = []
        actions_final = ''
        count = 0
        regex = ''
        cmd = 'nsxdp-cli ens flow-table dump'
        output = ssh.execute_command(client_object, cmd)
        print("nsxdp-cli ens flow-table on smartnic host %r " % output)
        header_keys = ['FT', 'dstMAC', 'srcMAC', 'VLAN', 'srcPort', 'srcIP',
                       'dstIP', 'proto', 'VNI', 'srcPort/type', 'dstPort/code',
                       'Actions']
        header_keys = [key.lower() for key in header_keys]
        lines = output.split('\n')
        tail_index = len(lines)
        # form dict of the response data
        for line in lines[1 + 1:tail_index]:
            if (line.strip() != ""):
                values = line.split()
                py_dicts.append(dict(list(zip(header_keys, values))))
                #import pdb;pdb.set_trace()
                if py_dicts[0].get('proto') == 1:
                    regex = OL_FLOW_DUMP_REGEX
                else:
                    regex = PING_FLOW_DUMP_REGEX
                if regex:
                    actions_final = re.search(regex, line).group(0)
                # Map the key to proper value
                if actions_final:
                    # change the key actions to have full OL value
                    py_dicts[count]['actions'] = actions_final
                count = count + 1
        return py_dicts

    @classmethod
    def get_matched_flow_rule(cls, py_dicts, src_ip=None, dst_ip=None,
                              src_mac=None, dst_mac=None,
                              ICMP_Traffic_IN_SAME_SUB_REGEX=None,
                              output_firewall=None):
        """
        Get Flow rule dict based on matched criteria
        Matched criteria can be checking L2/L3/L4 traffic for ip/mac
        """
        if 'disabled' in output_firewall:
            L2_Traffic_IN_SAME_SUB_REGEX = 'OL.*bmap.*cg.*dp.*VNI'
            L3_Traffic_IN_DIFF_SUB_VIA_TIER1_REGEX = 'OL.*bmap.*cg.*dp.*VDR.*VNI'
            rule_type = ['L2', 'L3']
        elif 'enabled' in output_firewall:
            L2_Traffic_IN_SAME_SUB_REGEX = 'OL.*bmap.*cg.*dp.*DFW.*VNI'
            L3_Traffic_IN_DIFF_SUB_VIA_TIER1_REGEX = 'OL.*bmap.*cg.*dp.*DFW.*VDR.*VNI'
            rule_type = ['L4']
        print("firewall value %s" % output_firewall)
        for rule in py_dicts:
            print(" rule %s " % rule)
            # Check L2 offload over smartnic
            for r_type in rule_type:
                if r_type in rule.get('FT'.casefold()):
                    if src_ip:
                        print("Test-flow Rule to check %s" % rule)
                        if src_ip in rule.get('srcIP'.casefold()) and \
                                dst_ip in rule.get('dstIP'.casefold()):
                            if int(rule.get('proto')) == 1 or int(rule.get('proto')) == 58:
                                OL = re.search(ICMP_Traffic_IN_SAME_SUB_REGEX, rule.get('actions'))
                                if OL:
                                    return rule, True
                            else:
                                OL = re.search(
                                    L3_Traffic_IN_DIFF_SUB_VIA_TIER1_REGEX,
                                    rule.get('actions')) or re.search(
                                    L2_Traffic_IN_SAME_SUB_REGEX,
                                    rule.get('actions'))
                                if OL:
                                    return rule, True
                    if src_mac:
                        print("Test-flow Rule to check %s" % rule)
                        if src_mac in rule.get('srcMAC'.casefold()) or \
                                dst_mac in rule.get('dstMAC'.casefold()):
                            if re.match(
                                r".*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.*",
                                    rule.get('srcIP'.casefold())):
                                if int(rule.get('proto')) == 1 or int(rule.get('proto')) == 58:
                                    OL1 = re.search(ICMP_Traffic_IN_SAME_SUB_REGEX,
                                                    rule.get('actions'))
                                    if OL1:
                                        return rule, True
                                else:
                                    OL2 = re.search(
                                        L3_Traffic_IN_DIFF_SUB_VIA_TIER1_REGEX,
                                        rule.get('actions')) or re.search(
                                        L2_Traffic_IN_SAME_SUB_REGEX,
                                        rule.get('actions'))
                                    if OL2:
                                        return rule, True
        return rule, False

    @classmethod
    def get_smartnic_ens_flow(cls, ssh, client_object, src_ip=None, dst_ip=None,
                              src_mac=None, dst_mac=None,
                              get_smartnic_ens_flow=None):
        """
        @type client_object: ESXCLIClient
        @param client_object: CLI Client used to execute calls on the host.
        @type src_ip: str
        @param src_ip: ip address
        @type src_ip: str
        @param src_ip: ip address

        @rtype: boolen
        @return: Retrun true if flow rules exists
        """
        flag = False
        OL_FLOW_DUMP_REGEX = "OL.*bmap.*dp.*"
        PING_FLOW_DUMP_REGEX = "bmap.*dp.*"
        cmd = "nsxcli -c get firewall status"
        output_firewall = ssh.execute_command(client_object, cmd)
        """
        if 'disabled' in output_firewall:
            ICMP_Traffic_IN_SAME_SUB_REGEX = OL_FLOW_DUMP_REGEX
        else:
            ICMP_Traffic_IN_SAME_SUB_REGEX = PING_FLOW_DUMP_REGEX
        """
        for lapse in range(1, 7):
            # Check flow rules for 120 seconds if not found
            #import pdb;
            #pdb.set_trace()

            py_dicts = cls.get_flow_dump_dict(ssh, client_object, OL_FLOW_DUMP_REGEX ,
                                              PING_FLOW_DUMP_REGEX)
            print("py dicts %s" % py_dicts)
            # traverse the dicts to get the OF rules and mark falg true/false
            # accrodingly
            if py_dicts:
                # traverse the dicts to get the OF rules and mark falg true/false
                # accrodingly
                rule, flag = cls.get_matched_flow_rule(py_dicts, src_ip,
                                                       dst_ip, src_mac,
                                                       dst_mac,
                                                       PING_FLOW_DUMP_REGEX,
                                                       output_firewall)
                if flag:
                    print("SW PING OL done over smartnic for rule %s" % rule)
                    break
            # Retry to check flow rules after 20 secs
            time.sleep(20)
            if flag is False:
                print("Flow rules not available over smartnic !!")
                continue
        if flag:
            return {'flow_rules': True}
        else:
            return {'flow_rules': False}

from paramiko_client import ssh_connection
ssh = ssh_connection()
client_object = ssh.create_connection('10.208.143.97')

smart = SMARTNIC()
src_ip = '172.16.1.11'
dst_ip =  '172.16.1.12'
smart.get_smartnic_ens_flow(ssh, client_object, src_ip=src_ip, dst_ip=dst_ip)