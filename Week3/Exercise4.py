import pexpect
import time
from getpass import getpass
import sys



def main():

    ip_addr = '184.105.247.71'
    username = 'pyclass'
    port = 22


    password = getpass()

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

    ssh_conn.timeout = 3

    #ssh_conn.logfile = sys.stdout

    ssh_conn.expect('ssword:')

    ssh_conn.sendline(password)

    time.sleep(1)

    ssh_conn.expect('#')

    ssh_conn.sendline('terminal length 0')

    ssh_conn.expect('#')

    ssh_conn.sendline('configure terminal')

    time.sleep(1)

    ssh_conn.expect('#')

    ssh_conn.sendline('logging buffered 65535')

    ssh_conn.expect('#')

    ssh_conn.sendline('end')

    ssh_conn.expect('#')

    ssh_conn.sendline('show run | include logging buffer')

    ssh_conn.expect('#')

    print ssh_conn.before


if __name__ == "__main__":
    main()

    

