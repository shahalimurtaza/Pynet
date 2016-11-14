
import time
from getpass import getpass
import sys
from netmiko import ConnectHandler


def getpassword():
    password = getpass()
    return password

def connect_setup(device_attr):
    return ConnectHandler(**device_attr)

def sendcommand(ssh_object):
    return ssh_object.send_command("show arp")


def main():

    pynet1 = {
          'device_type' : 'cisco_ios',
          'ip' : '184.105.247.70',
          'username' : 'pyclass',
          'password' : getpassword()
          }

    pynet2 = {
        'device_type' : 'cisco_ios',
        'ip' : '184.105.247.71',
        'username' : 'pyclass',
        'password' : getpassword()
        }

    pynet3 = {
        'device_type' : 'juniper',
        'ip' : '184.105.247.76',
        'username' : 'pyclass',
        'password' : getpassword()
        }

    devices = [ pynet1, pynet2, pynet3]

    for i in devices:
        ssh_object = connect_setup(i)
        
        print ("\nPrinting for: {0}\n".format(i['device_type']))
        print sendcommand(ssh_object)



if __name__ == "__main__":
    main()





