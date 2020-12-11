# author  : Kris & Seth Cardoen
# created : 20/07/2020
# purpose : Automate waterchange and measurements
# update : 24/08/2020
from datetime import datetime, timedelta
import time
from utils.Pump import Pump
#from utils.TempSensor import TempSensor
from utils.PumpLogger import PumpLogger
from utils.ActionLogger import ActionLogger
#import requests
import utils.archive_file
print(f'{datetime.now()} start main aquacontrole module.....................')
# Create an instance to log actions into the generic /logger/action.log
actionlogger = ActionLogger()
actionlogger.log("start main app.py")
# declare check condition to stop module
stopsignal = False
# Create an instance for the pump controller
# pump = Pump()
# Create and instance for the temp sensor 1
# tempsensor_1 = TempSensor()
# Create an instance to log pump actions into the file /logger/pump.log
# start action loop
while not stopsignal:
    # execute actions
    print('sleep for 3 minutes')
    time.sleep(1 * 60)
    print('> start controle loop ')
    # measure tempsensor 1
    #print(f'>> tempsensor 1 = {tempsensor_1.getTemp()}')
    # archive all folders older then
    #r =requests.get("http://192.168.0.223:5000/datastream/1")
    #print(f'request :{r.request} ')
    #print(f'status code :{r.status_code}')
    #print(f'headers :{r.headers}')
    #print(f'body : {r.text}')
    
    try:
        print("start archive from app.py")
        utils.archive_file.archive()
        pass
    except FileExistsError:
        print("file could not be archived, archived file already exists")
    
    print('> end controle loop ')
    number = 1 
    
    while number < 2 :  
        print("start check run : " + str(number))

        
        
        pumplogger = PumpLogger(number)
        # Check if the daily water change has already ran today. If not start it now
        # First check if a previous date was found
        if pumplogger.getlatest() == None:
            print(f"No previous correct date was found for turn {cd number}, therefore pump is started")
            print(f'turn {number} has not started today, action required')
            if number ==1:
                print("waiting 8h for start of cycle 1")
                time.sleep(1 * 1 * 60)
                #time.sleep(1 * 1 * 20)
            else:
                print("waiting 3h for start of cycle 1")
                time.sleep(1 * 1 * 60)
                #time.sleep(1 * 1 * 20)
                
            pumplogger.log("start pump")
            pump = Pump()
            pump.waterchange(5* 60)
            pumplogger.log("stop pump")
        else:
            # If a previous date has been found check if the pump
            # was already started today. If not the case start the pump
            if pumplogger.getlatest() != None and datetime.now().strftime("%d/%m/%Y") != pumplogger.getlatest()[:-20]:
                print(f'trun {number} has not started today, action required')
                if number ==1:
                    print("waiting 8h for start of cycle 1")
                    time.sleep(1 * 1 * 60)
                    #time.sleep(1 * 1 * 20)
                else:
                    print("waiting 3h for start of cycle 1")
                    time.sleep(1 * 1 * 60)
                    #time.sleep(1 * 1 * 20)
                    
                pumplogger.log("start pump")
                pump.waterchange(5* 60)
                pumplogger.log("stop pump")
            else:
                print(f'turn {number} has been running today no action required')

        number = number + 1
        
else:
    exit()
actionlogger.log("stop main app.py")
print(f'{datetime.now()} end main aquacontrole module ..............................................')


