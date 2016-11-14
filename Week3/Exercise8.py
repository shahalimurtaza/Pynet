#!/usr/bin/env python
import time
from getpass import getpass
import sys
from netmiko import ConnectHandler


def getpassword():
    password = getpass()
    return password

def connect_setup(device_attr):
    return ConnectHandler(**device_attr)

def sendcommand_fromfile(ssh_object, config_file):
    return ssh_object.send_config_from_file(config_file)

def sendcommand(ssh_object,command):
    return ssh_object.send_command(command)


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

    devices = [ pynet1, pynet2]

    for a_device in devices:
        ssh_object = connect_setup(a_device)
        print sendcommand_fromfile(ssh_object, 'config_file.txt')     
        print sendcommand(ssh_object, 'show run | include logging buffered')
        print sendcommand(ssh_object, 'show run | include console')



if __name__ == "__main__":
    main()

