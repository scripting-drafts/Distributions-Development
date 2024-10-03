# sudo ip link set wlan0 down
# sudo ip link set wlan0 up
sudo wpa_supplicant -B -i wlan0 -c /home/kali/Desktop/wifi/wpa_supplicant.conf -D nl80211,wext
sudo dhclient wlan0
