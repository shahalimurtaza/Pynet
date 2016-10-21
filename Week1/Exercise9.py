
from ciscoconfparse import CiscoConfParse


cisco_cfg = CiscoConfParse("Exercise8ConfigFile")

group2_cryptos = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'set pfs group2')
#crypto_maps =    cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'pfs group2')

print ("Printing only PFS Group 2 Cryptos:\n")

for crypto in group2_cryptos:
    print crypto.text    


