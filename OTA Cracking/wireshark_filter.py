import pyshark
from airmon import iface

'TODO:'
''' Deauth packet filters
 wlan.fc.type_subtype == 0 (association request)
 wlan.fc.type_subtype == 4 (probe request)
 wlan.fc.type_subtype == 5 (probe response)'''
capture = pyshark.LiveRingCapture(interface='WiFi', debug=True)
capture = capture.
# , filter='wlan.fc.type_subtype == 0,4,5'
for packet in capture.sniff_continuously(packet_count=5000):
    
    print('Just arrived:', packet)

for port in tqdm(ports):
    rtp_cap = pyshark.FileCapture("fixed_" + capture_file, display_filter='rtp', decode_as={'udp.port==' + port: 'rtp'})
    # rtp_cap.set_debug()
    for rtp_packet in rtp_cap:
        length = rtp_packet.length
        if length == "85" or length == "73":
            seq = int(rtp_packet.rtp.seq)
            ssrc = rtp_packet.rtp.ssrc