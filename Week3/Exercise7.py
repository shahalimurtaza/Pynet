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

    config_commands = ['logging buffered 666666']
    
    print pynet_rtr2.send_config_set(config_commands)

    #pynet_rtr2.send_command('logging buffered 6666666')
    #pynet_rtr2.send_command('end')

    print pynet_rtr2.send_command('show run | include logging buffered')



if __name__ == "__main__":
    main()




