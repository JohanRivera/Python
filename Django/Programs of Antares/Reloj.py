# Iniciatily, enable the I2C into the option Interfacing Option and reboot the system with the command:
# sudo raspi-config
# sudo reboot
# Then, to test in raspberry 2 to up with the command: sudo i2cdetect -y 1 and raspberry 1: sudo i2cdetect -y 0
# Put the command: sudo nano /etc/modules 
# And in the open window you must write down everything, rtc-ds3231 and saved the file 
# Put the command: sudo nano /boot/config.txt
# And in the open window you must write in enable the optional hardware interface: dtoverlay=i2c-rtc,ds3231 and saved the file
# Put the command: sudo apt-get -y remove fake-hwclock
# Put the command: sudo update-rc.d -f fake-hwclock remove
# Put the command: sudo nano /lib/udev/hwclock-set
# In the open window you must commentary the lines: if [e /run/systemd/system] ; then
#                                                           exit 0
#                                                   fi
#Note: To commentary a line is with the character '#'
# Put the command: sudo reboot
# If haven't internet change the hour with the command: sudo date -s "Mar 5 2015 12:46:00"
# After, put the command: sudo hwclock -w
# For see the hour, you must put the command: sudo hwclock -r


from datetime import datetime
#Created a dictionary for months

def currentTime():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    return date
