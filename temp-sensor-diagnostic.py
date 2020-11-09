from w1thermsensor import W1ThermSensor
#from utils.TempSensor import TempSensor


print("start sensordiagnostic..........................")
 
#sensor1 = TempSensor("sensor1")
#print(sensor1.getTemp())
print("checking for available temperature sensors")
for sensor in W1ThermSensor.get_available_sensors():
    print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))

    

print("end sensordiagnostic..........................")