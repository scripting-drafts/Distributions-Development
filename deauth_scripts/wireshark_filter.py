import pyshark
from airmon import iface

''' Deauth packet filters
 wlan.fc.type_subtype == 0 (association request)
 wlan.fc.type_subtype == 4 (probe request)
 wlan.fc.type_subtype == 5 (probe response)'''

capture = pyshark.LiveRingCapture(interface='WiFi', debug=True)

# , filter='wlan.fc.type_subtype == 0,1,5'
for packet in capture.sniff_continuously(packet_count=5000):
    print('Just arrived:', packet)
