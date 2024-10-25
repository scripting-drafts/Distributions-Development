https://medium.com/nybles/exploring-android-hacking-with-metasploit-framework-2306c3511698

# Wifi Cheatsheet

sudo iwlist wlan0 scan

wpa_passphrase "HP Deskjet 2060" Ocarina8080 | sudo tee AP/wifi_wpa_supplicant.conf

sudo wpa_supplicant -B -i wlan0 -c AP/wifi_wpa_supplicant.conf

sudo dhclient wlan0 -r
  
Other:
 - List drivers  
 ethtool -i wlan0  
  
 - List driver info  
 /sbin/modinfo rtl8187  
  
 - Enable Power Management  
 sudo modprobe rtl8187 ps_enable=1   
  
 - Run changes on boot   
 echo 'options ath9k ps_enable=1' >> /etc/modprobe.d/rtl8187.conf  
