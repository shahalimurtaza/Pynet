#!/usr/bin/env python

import telnetlib
import time

ip_addr = '184.105.247.70'
username = 'pyclass'
password = '88newclass'

TELNET_PORT = 23
TELNET_TIMEOUT = 6


def main():
    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')

    output = remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    
    time.sleep(1)
    
    output = remote_conn.read_very_eager()
    
    print output
    
    remote_conn.write('show ip int br' + '\n')
    
    time.sleep(1)

    output = remote_conn.read_very_eager()
    print output
    
    remote_conn.close()

if __name__ == "__main__":
    main()
