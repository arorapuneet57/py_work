import paramiko

class ssh_connection:

    def create_connection(self, ip):
            port = 22
            ssh = paramiko.client.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, port, 'root', 'ca$hc0w')

            return ssh

    def execute_command(self, ssh, cmd):
        stdin, stdout, stderr = ssh.exec_command(cmd)
        outlines = stdout.readlines()
        resp = ''.join(outlines)
        return resp


pp = ssh_connection()
ssh = pp.create_connection('10.208.143.97')

pp.execute_command(ssh, 'nsxcli -c get firewall status')
