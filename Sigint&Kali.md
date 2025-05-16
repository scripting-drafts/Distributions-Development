### SigintOS & Kali

 - Distribution release upgrade  
RELEASE_UPGRADER_ALLOW_THIRD_PARTY=1 do-release-upgrade -m desktop -f DistUpgradeViewKDE  
  
 - Add Kali Repository
echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee /etc/apt/sources.list.d/kali.list  
wget -q -O - https://archive.kali.org/archive-key.asc | sudo apt-key add -  
  
 - APT Upgrade options  
sudo apt-get dist-upgrade -o Dpkg::Options::="--force-confnew"  

 - Just in case: 'diversion of /lib32 to /.lib32.usr-is-merged by base-files' clashes with ...  
sudo dpkg-divert --package base-files --no-rename --remove lib32 libo32 lib64
sudo apt reinstall base-files  
sudo dpkg -i --force-overwrite /var/cache/apt/archives/libgstreamer  