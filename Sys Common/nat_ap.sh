cat > /etc/systemd/network/08-wlan0.network <<EOF
[Match]
Name=wlan0
[Network]
Address=192.168.4.1/24
MulticastDNS=yes
# IPMasquerade is doing NAT
IPMasquerade=yes
DHCPServer=yes
[DHCPServer]
DNS=84.200.69.80 1.1.1.1
EOF

cat > /etc/systemd/network/04-eth0.network <<EOF
[Match]
Name=eth0
[Network]
DHCP=yes
EOF