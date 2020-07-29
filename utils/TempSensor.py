# Class responsible for managing temperature sensor
import time
from utils.TempLogger import TempLogger
from w1thermsensor import W1ThermSensor


class TempSensor:
    templogger = TempLogger()

    def __init__(self):
        pass

    def getTemp(self):
        sensor = W1ThermSensor()
        temperature = sensor.get_temperature()
        # print("The temperature is %s °C" % temperature)
        self.templogger.log(temperature)
        return temperature
