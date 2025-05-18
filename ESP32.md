# Esp32 OTG USB <-> Midi
  
git clone https://github.com/espressif/esp-idf.git  
Run install.bat or install.ps1  
IN CMD run: export.bat  
cd C:\Users\USERNAME\Desktop\esp-idf\examples\peripherals\usb\device\tusb_midi  
idf.py set-target esp32s2  
idf.py -p COM8 flash monitor  
  
![The project description](https://github.com/espressif/esp-idf/tree/master/examples/peripherals/usb/device/tusb_midi)