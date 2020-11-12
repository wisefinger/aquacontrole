from w1thermsensor import W1ThermSensor



print("start sensordiagnostic..........................")
 
#sensor1 = TempSensor("sensor1")
#print(sensor1.getTemp())
print("checking for available temperature sensors")
print("you can check your connected sensors via ls -ltr in /sys/bus/w1/devices  on your pi")
for sensor in W1ThermSensor.get_available_sensors():
    print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))
    #sensor.set_resolution(12,True)

    

print("end sensordiagnostic..........................")