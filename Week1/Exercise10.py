
from ciscoconfparse import CiscoConfParse


cisco_cfg = CiscoConfParse("Exercise8ConfigFile")

non_aes_cryptos = cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO', childspec=r'AES-SHA')
#crypto_maps =    cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO', childspec=r'AES')

print ("Printing only Cryptos without AES-SHA and the transforms that they use:\n")

for crypto in non_aes_cryptos:
    print crypto.text
    for child in crypto.children:
        if "transform" in child.text:
            print child.text   


