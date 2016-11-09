#!/usr/bin/env python


import paramiko
import time
from getpass import getpass



def main():
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    port = 22


    password = getpass()

    remote_conn_pre=paramiko.SSHClient()

    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

    remote_conn = remote_conn_pre.invoke_shell()

    print remote_conn.recv(5000)

    remote_conn.send("configure terminal\n")

    time.sleep(1)
   

    remote_conn.send("logging buffered 65535\n")

    time.sleep(1)

    print remote_conn.recv(5000)





if __name__ == "__main__":
    main()


