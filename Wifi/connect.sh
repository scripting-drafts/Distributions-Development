# sudo ip link set wlan0 down
# sudo ip link set wlan0 up
sudo wpa_supplicant -B -i wlan1 -c wpa_supplicant.conf -D nl80211,wext
sudo dhclient wlan1
