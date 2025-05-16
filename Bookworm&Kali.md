### Bookworm & Kali on RPi Zero W  
  
(All works till "Install python 2.7")

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
sudo apt update && sudo apt full-upgrade -y  
sudo apt install rpi-connect  
rpi-connect on  
rpi-connect signin  
sudo apt install locate    

add alias cls="/usr/bin/clear" to .profile  
sudo nano /etc/motd  
updatedb  
  
sudo nano /etc/NetworkManager/NetworkManager.conf
  
[main]  
   plugins=ifupdown,keyfile  
   managed=true  
  
sudo nano /etc/dhcpcd.conf
interface usb0
static ip_address=192.168.2.3/24
static routers=192.168.2.1
static domain_name_servers=192.168.2.1

sudo nano /etc/network/interfaces  
auto usb0  
allow-hotplug usb0  
iface usb0 inet static  
        address 192.168.7.2  
        netmask 255.255.255.0  
        network 192.168.7.0  
        broadcast 192.168.7.255  
        gateway 192.168.7.1  

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
