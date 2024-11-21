import subprocess

iface = 'wlan1'
airmon_1 = f'airmon-ng check kill'
airmon_2 = f'airmon-ng {iface} start'
airodump_1 = f'airodump-ng {iface}'

try:
    subprocess.call(airmon_1)
    subprocess.call(airmon_2)
    subprocess.call(airodump_1)
except Exception as e:
    print(e)