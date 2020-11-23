from utils.TempSensor import TempSensor


print("starting test tempSensor class..........")
sensor = TempSensor()
infoFromJson = (sensor.getAllTempJson())
print(infoFromJson)
infoFromHtml = (sensor.getAllTempHtml())
print(infoFromHtml)
del sensor
#print (json2html.convert(json = infoFromJson))
print("ending test tempSensor class..........")