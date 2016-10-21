
from ciscoconfparse import CiscoConfParse


cisco_cfg = CiscoConfParse("Exercise8ConfigFile")
crypto = cisco_cfg.find_objects(r"^crypto map CRYPTO")

#Use below for testing and to print out the contents of crypto list
#for i in range(len(crypto)):
#    print crypto[i].text

for map in crypto:
    print map.text
    for cryptochild in map.children:
        print cryptochild.text

