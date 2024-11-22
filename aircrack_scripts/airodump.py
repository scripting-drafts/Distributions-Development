import subprocess
from sys import argv
from airmon import iface

mac = argv[2]
channel = argv[1]

if channel == '--help':
    print('Usage: python aircrack_scripts/airmon_airodump.py <channel> <mac>')
    print('Example: python aircrack_scripts/airmon_airodump.py 11 U3:E5:3A:30:20:11')
    exit()

airodump_2 = f'airodump-ng -c {channel} --bssid {mac} -w output-file {iface}'
subprocess.call(airodump_2)