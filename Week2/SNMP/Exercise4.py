#!/usr/bin/env python


import snmp_helper


def get_snmp_data(param_tuple, oid):
 
    snmp_data = snmp_helper.snmp_get_oid(param_tuple, oid)
    output = snmp_helper.snmp_extract(snmp_data)
    return output

def main():
        print ("Type END to quit")
        ip_addr = raw_input ("Please enter IP address:")
        if ip_addr == 'END': sys.exit()

        comm_string = raw_input ("Please enter community string:")
        if comm_string == 'END': sys.exit()

        oid = raw_input ("Please enter oid to lookup:")
        if oid == 'END': sys.exit()

        param_tuple =  (ip_addr, comm_string, 161)
        
        print get_snmp_data(param_tuple,oid)

        
main()        
