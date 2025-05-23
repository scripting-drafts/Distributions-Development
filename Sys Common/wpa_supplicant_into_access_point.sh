cat > /etc/wpa_supplicant/wpa_supplicant-wlan0.conf <<EOF

country=DE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="Open Access Point"
    mode=2
    frequency=2437
    key_mgmt=NONE
    # delete next 3 lines if key_mgmt=NONE
    # key_mgmt=WPA-PSK
    # proto=RSN WPA
    # psk="password"
}
EOF

chmod 600 /etc/wpa_supplicant/wpa_supplicant-wlan0.conf
systemctl disable wpa_supplicant.service
systemctl enable wpa_supplicant@wlan0.service
rfkill unblock wlan