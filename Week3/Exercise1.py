
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
 
    output = remote_conn.recv(5000)

    print output

    remote_conn.send("terminal length 0\n")

    time.sleep(1)

    output = remote_conn.recv(5000)

    print output
       
    time.sleep(1)
    
    remote_conn.send("show version\n")
    
    time.sleep(1)
    
    output = remote_conn.recv(65535)    

    #if remote_conn.recv_ready():
    #    output += remote_conn.recv(65535)


    print output


if __name__ == "__main__":
    main()


