# Release Notes  
  
## SigintOS + Kali  

 - Distribution release upgrade  
RELEASE_UPGRADER_ALLOW_THIRD_PARTY=1 do-release-upgrade -m desktop -f DistUpgradeViewKDE  

 - APT Upgrade options  
sudo apt-get dist-upgrade -o Dpkg::Options::="--force-confnew"  
  
## Wi-Fi Cheat Sheet

sudo iwlist wlan0 scan  
wpa_passphrase "essid" pwd | sudo tee AP/wifi_wpa_supplicant.conf  
sudo wpa_supplicant -B -i wlan0 -c AP/wifi_wpa_supplicant.conf  
sudo dhclient wlan0 -r  
MAC: cat /sys/class/net/wlan0/address  
  
Other:  
 - List drivers  
 ethtool -i wlan0  
  
 - List driver info  
 /sbin/modinfo nic_driver  
  
 - Enable Power Management  
 sudo modprobe -r rtl8187  
 sudo modprobe nic_driver ps_enable=1  
  
 - Run changes on boot  
 sudo echo 'options nic_driver ps_enable=1' >> /etc/modprobe.d/rtl8187.conf

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
  
  
  
  
  
/etc/network/interfaces  i.e.:  
auto lo  
iface lo inet loopback  
  
auto wlan0:0  
iface wlan0:0 inet static
        address 192.168.168.3
        netmask 255.255.255.0
  
ERROR  
nl80211: kernel reports: Match already configured  
