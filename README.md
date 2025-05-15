### SigintOS & Kali

 - Distribution release upgrade  
RELEASE_UPGRADER_ALLOW_THIRD_PARTY=1 do-release-upgrade -m desktop -f DistUpgradeViewKDE  
  
 - Add Kali Repository
echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list.d/kali.list  
wget -q -O - https://archive.kali.org/archive-key.asc | sudo apt-key add -  
  
 - APT Upgrade options  
sudo apt-get dist-upgrade -o Dpkg::Options::="--force-confnew"  

 - Just in case: 'diversion of /lib32 to /.lib32.usr-is-merged by base-files' clashes with ...  
sudo dpkg-divert --package base-files --no-rename --remove lib32 libo32 lib64
sudo apt reinstall base-files  
sudo dpkg -i --force-overwrite /var/cache/apt/archives/libgstreamer  

### Wi-Fi Cheat Sheet

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
  
sudo nmcli radio wifi on  
sudo nmcli dev wifi connect <wifi-ssid> password "<network-password>"  
  
/etc/network/interfaces  i.e.:  
auto lo  
iface lo inet loopback  
  
auto wlan0:0  
iface wlan0:0 inet static  
address 192.168.168.3  
netmask 255.255.255.0  
  
ERROR reminder  
nl80211: kernel reports: Match already configured  

  
### Bookworm & Kali on RPi Zero W  
  
First steps in:  
 - https://www.circuitbasics.com/raspberry-pi-zero-ethernet-gadget/  
 - https://www.instructables.com/The-Ultimate-Headless-RPi-Zero-Setup-for-Beginners/  
  
Install Bonjour and RNDIS ![3rd party drivers]() on Windows  
  
After burning the card with ![the official burner](https://downloads.raspberrypi.org/imager/imager_latest.exe)  
  
Add empty "ssh" filetype:  
nano ssh  
  
Append in config.txt:  
dtoverlay=dwc2  
  
Append after rootwait in cmdline.txt:  
modules-load=dwc2,g_ether  
   
sudo apt update -y && sudo apt full-upgrade -y  

    
Steps to install ![Netscanner](https://github.com/Chleba/netscanner)  
  
Install ![python2.7 requirements](https://github.com/pyenv/pyenv?tab=readme-ov-file#a-getting-pyenv):  
  
curl -fsSL https://pyenv.run | bash  
  
To ~./bashrc:  
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc  
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc  
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc  
  
To ~./profile:  
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile  
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile  
echo 'eval "$(pyenv init - bash)"' >> ~/.profile  
  
Install dependencies:  
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \  
libbz2-dev libreadline-dev libsqlite3-dev curl git \  
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev  
  
Install python2.7:  
pyenv versions  
pyenv install 2.7  
    
For convenience:
sudo apt install locate  
updatedb  
add alias cls="/usr/bin/clear" to .profile  
  
sudo apt install python3-full  
sudo apt install python3-virtualenv  
