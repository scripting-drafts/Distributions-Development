### Bookworm & Kali on RPi Zero W  
  
## Manage like USB Gadget  
  
First steps in:  
 - https://www.circuitbasics.com/raspberry-pi-zero-ethernet-gadget/  
 - https://www.instructables.com/The-Ultimate-Headless-RPi-Zero-Setup-for-Beginners/  
  
Install Bonjour and RNDIS ![3rd party drivers](https://github.com/scripting-drafts/Distributions-Development/tree/main/Third%20Party) on Windows  
  
After burning the card with ![the official burner](https://downloads.raspberrypi.org/imager/imager_latest.exe)  
  
Add empty "ssh" filetype:  
touch ssh  
  
Append in config.txt:  
dtoverlay=dwc2  
  
Append after rootwait in cmdline.txt:  
modules-load=dwc2,g_ether  
  
For convenience:  

<!-- sudo nano /etc/dhcp/dhcpd.conf  
interface usb0
static ip_address=192.168.100.100/24
static routers=192.168.100.1
static domain_name_servers=192.168.100.1 -->
  
add 'sudo ifconfig usb0 up' to .bashrc
sudo apt update && sudo apt full-upgrade -y  
sudo apt install locate  
add alias cls="/usr/bin/clear" to .profile  
sudo nano /etc/motd  
updatedb  

For Bookworm:  
sudo apt install rpi-connect  
rpi-connect on  
rpi-connect signin  

For Buster:  
sudo raspi-config
enable RealVNC through Interfaces  
  
Deploy Hotspot Captive Portal:  
sudo apt-get install libmicrohttpd-dev  
cd ~/  
git clone https://github.com/nodogsplash/nodogsplash.git  
cd nodogsplash  
make  
sudo make install  
sudo nano /etc/nodogsplash/nodogsplash.conf  
Edit parameters "GatewayInterface", "GatewayAddress"  
sudo nano /etc/rc.local  
Editable at:  

Make Hotspot (without the password arg):  
copy "interfaces" and "dhcpcd.conf" to rpi  

set the servers in /etc/resolvconf.conf:  
name_servers="8.8.8.8 8.8.4.4"  
And afterwards run resolvconf -u, to generate /etc/resolv.conf  
  
sudo nano /etc/dhcp/dhclient.conf

git clone https://github.com/oblique/create_ap
cd create_ap
make install




## Other
sudo nano /etc/NetworkManager/NetworkManager.conf  
cd ~/  
  
[main]  
   plugins=ifupdown,keyfile  
   managed=true  

sudo nano /etc/NetworkManager/conf.d/10-my-config.conf
  
[usb0]  
   managed=true  
  


sudo nano /etc/network/interfaces  
auto usb0  
allow-hotplug usb0  
iface usb0 inet static  
        address 192.168.7.2  
        netmask 255.255.255.0  
        network 192.168.7.0  
        broadcast 192.168.7.255  
        gateway 192.168.7.1  
  
Assert interfaces status:  
nmcli general
nmcli device
nmcli radio
ip link

Follow the steps in ![Setting a Static Address](https://raspberrypi.stackexchange.com/questions/145593/how-do-i-set-up-networking-on-raspberry-pi-os-bookworm)  
  
  
sudo apt install python3-full  
sudo apt install python3-virtualenv  

    
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
