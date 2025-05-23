## /home/pi/bridge.sh
#!/usr/bin/env bash

service hostapd stop
service dnsmasq stop

service dhcpcd restart
ifconfig wlan0 down
ifconfig wlan0 up

sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"

iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables --table nat --append POSTROUTING --out-interface usb0 -j MASQUERADE
iptables --append FORWARD --in-interface usb0 -j ACCEPT

systemctl unmask hostapd
systemctl enable hostapd

service dnsmasq start
service hostapd start