# author  : Kris & Seth Cardoen
# created : 20/07/2020
# purpose : Automate waterchange and measurements
from datetime import datetime, timedelta
import time
from utils.Pump import Pump
from utils.PumpLogger import PumpLogger
from utils.ActionLogger import ActionLogger
print(f'{datetime.now()} start main aquacontrole module ....................................................')
# Create an instance to log actions into the generic /logger/action.log
actionlogger = ActionLogger()
actionlogger.log("start main app.py")
# Create an instance for the pump controller
pump = Pump()
# Create an instance to log pump actions into the file /logger/pump.log
pumplogger = PumpLogger()
# Check if the daily water change has already ran today. If not start it now
# First check if a previous date was found
if pumplogger.getlatest() == None:
    print("No previous correct date was found, therefore pump is started")
    print('pump has not started today, action required')
    pumplogger.log("start pump")
    pump.start()
    time.sleep(5)
    pump.stop()
    pumplogger.log("stop pump")
else:
        # If a previous date has been found check if the pump
        # was already started today. If not the case start the pump
        if pumplogger.getlatest() != None and datetime.now().strftime("%d/%m/%Y") != pumplogger.getlatest()[:-20] :
                print('pump has not started today, action required')
                pumplogger.log("start pump")
                pump.start()
                time.sleep(5)
                pump.stop()
                pumplogger.log("stop pump")
        else:
                print('pump has been running today no action required')



















# <editor-fold desc="Description">
#log = Logger()

# pumpy = utils.pump
#init()

# get last rundate from logfile
#try:
#    last_date_run = datetime.strptime(log.getlatest(), datetime.now().strftime("%d/%m/%Y:%X"))
#    None
#except TypeError:
    # Set last run to day -1 to make sure the task will run
 #   last_date_run = datetime.today() - timedelta(days=1)

#print(f'> last day run     = {last_date_run.strftime("%d/%m/%Y:%X")}')
#print(f'> current datetime = {datetime.now().strftime("%d/%m/%Y:%X")}')


#if datetime.now().strftime("%x") == last_date_run.strftime("%x"):
 #   print(">> program did already run today. No action required")
#else:
#    print(">> program did not run yet today. Starting")
#    log.log(datetime.now())
# </editor-fold>

actionlogger.log("stop main app.py")
print(f' \n {datetime.now()} stop  main aquacontrole module....................................................')
