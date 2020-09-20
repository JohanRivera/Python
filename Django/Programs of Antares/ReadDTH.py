#Is necessary download the library in the console of pyhton with the command: sudo pip3 install Adafruit_DHT
#This function return a list with two floats, first is temperature and second is humedity
import Adafruit_DHT
dth_sensor=22 #Select between DTH11 or DTH22
def readDTH(dth_pin):#dth_pin is the line yellow in the DTH22
    humidity, temperature = Adafruit_DHT.read(dth_sensor,dth_pin)
    if humidity is not None and temperature is not None and temperature > 0:
        dth = [temperature,humidity]
        return dth
    else:
        dth = [0,0]
        return dth

         