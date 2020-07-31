# author  : Kris & Seth Cardoen
# created : 20/07/2020
# purpose : Automate waterchange and measurements
from datetime import datetime, timedelta
import time
from utils.Pump import Pump
from utils.TempSensor import TempSensor
from utils.PumpLogger import PumpLogger
from utils.ActionLogger import ActionLogger
from utils.archive_file import archive

print(f'{datetime.now()} start main aquacontrole module ....................................................')
# Create an instance to log actions into the generic /logger/action.log
actionlogger = ActionLogger()
actionlogger.log("start main app.py")
# declare check condition to stop module
stopsignal = False
# Create an instance for the pump controller
pump = Pump()
# Create and instance for the temp sensor 1
tempsensor_1 = TempSensor()
# Create an instance to log pump actions into the file /logger/pump.log
pumplogger = PumpLogger()
# start action loop
while not stopsignal:
    # execute actions
    print('> start controle loop ')
    # measure tempsensor 1
    print(f'>> tempsensor 1 = {tempsensor_1.getTemp()}')
    # archive all folders older then
    try:
        archive()
    except FileExistsError:
        print("file could not be archived, archived file already exists")
    print('> end controle loop ')

    # Check if the daily water change has already ran today. If not start it now
    # First check if a previous date was found
    if pumplogger.getlatest() == None:
        print("No previous correct date was found, therefore pump is started")
        print('pump has not started today, action required')
        pumplogger.log("start pump")
        pump.waterchange(10)
        pumplogger.log("stop pump")
    else:
        # If a previous date has been found check if the pump
        # was already started today. If not the case start the pump
        if pumplogger.getlatest() != None and datetime.now().strftime("%d/%m/%Y") != pumplogger.getlatest()[:-20]:
            print('pump has not started today, action required')
            pumplogger.log("start pump")
            pump.waterchange(10)
            pumplogger.log("stop pump")
        else:
            print('pump has been running today no action required')
    time.sleep(60)
else:
    exit()
actionlogger.log("stop main app.py")
print(f'{datetime.now()} end main aquacontrole module ....................................................')