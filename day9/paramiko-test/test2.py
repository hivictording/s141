# Author: Victor Ding

# -*- coding: utf-8 -*-

import paramiko

trans = paramiko.Transport(('192.168.2.21'),22)
trans.connect(username='vding',password='password')

sftp_client = paramiko.SFTPClient
sftp = sftp_client.from_transport(trans)

sftp.put('ansible.pdf','aaa.pdf')

sftp.get('aaa.pdf','bbb.pdf')

trans.close()
