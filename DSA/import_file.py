from paramiko_client import ssh_connection
pp = ssh_connection()
ssh = pp.create_connection('10.208.143.97')
pp.execute_command(ssh, 'ls')