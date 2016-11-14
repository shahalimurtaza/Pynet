#!/usr/bin/env python

import time
from getpass import getpass
import sys
from netmiko import ConnectHandler


def main():

    password = getpass()

    pynet2 = {
        'device_type' : 'cisco_ios',
        'ip' : '184.105.247.71',
        'username' : 'pyclass',
        'password' : password
        }

    pynet_rtr2 = ConnectHandler(**pynet2)
    
    print pynet_rtr2.find_prompt()

    pynet_rtr2.config_mode()

    print pynet_rtr2.find_prompt()

    print pynet_rtr2.check_config_mode()




if __name__ == "__main__":
    main()



