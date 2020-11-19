#from utils.TempSensor import TempSensor
from json2html import *

print("starting test tempSensor class..........")
#sensor = TempSensor()
#print(sensor.getAllTemp())
#del sensor
print("ending test tempSensor class..........")

infoFromJson = {
        "name": "json2html",
        "description": "Converts JSON to HTML tabular representation"
}
print (json2html.convert(json = infoFromJson))