#!/usr/bin/env python

import telnetlib

#if __name__ == "__main__":
#    main()


ip_addr = '184.105.247.70'
username = 'pyclass'
password = '88newclass'

TELNET_PORT = 23
TELNET_TIMEOUT = 6

main()

def main():
    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    print output

    remote_conn.write('pyclass' + '\n')

    output = remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    print output
    remote_conn.write('88newclass' + '\n')

    #remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
    remote_conn.write('show ip int br' + '\n')

    output = remote_conn.read_very_eager()

    print output
    
    remote_conn.close()

  
#output = remote_conn.read_very_eager()

#remote_conn.close()

#print output

