# Author: Victor Ding

# -*- coding: utf-8 -*-

import paramiko

trans = paramiko.Transport(('192.168.2.21',22))
trans.connect(username='vding',password='password')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh._transport = trans

ssh.open_sftp() # sftp client

# ssh.connect(hostname='192.168.2.21',port=22,username='vding',password='password')

stdin,stdout,stderr = ssh.exec_command("ls -a")
print(stdout.read().decode())

stdin,stdout,stderr = ssh.exec_command("df -hl")
print(stdout.read().decode())
