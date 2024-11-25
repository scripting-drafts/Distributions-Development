import subprocess

iface = 'wlan1'
airmon_1 = f'sudo airmon-ng check kill'
airmon_2 = f'sudo airmon-ng {iface} '
airmon_2 = f'sudo airmon-ng start {iface}'
airodump_1 = f'sudo airodump-ng {iface} -w dump_capture --output-format csv'

try:
    subprocess.call(airmon_1)
    subprocess.call(airmon_2)
    subprocess.call(airodump_1)
except Exception as e:
    print(e)