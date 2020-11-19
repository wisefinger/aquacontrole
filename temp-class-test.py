from utils.TempSensor import TempSensor
import json2html 

print("starting test tempSensor class..........")
sensor = TempSensor()
print(sensor.getAllTemp())
del sensor
print("ending test tempSensor class..........")
