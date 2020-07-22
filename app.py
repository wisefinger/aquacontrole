# author  : Kris & Seth Cardoen
# created : 20/07/2020
# purpose : Automate waterchange and measurements
from datetime import datetime, timedelta
from utils.pump import init
from logger import Logger
from ActionLogger import ActionLogger

print(f'{datetime.now()} start main aquacontrole module ....................................................')


actionlogger = ActionLogger();
print(actionlogger.x)


log = Logger()

# pumpy = utils.pump
init()

# get last rundate from logfile
try:
#    last_date_run = datetime.strptime(log.getlatest(), datetime.now().strftime("%d/%m/%Y:%X"))
    None
except TypeError:
    # Set last run to day -1 to make sure the task will run
    last_date_run = datetime.today() - timedelta(days=1)

print(f'> last day run     = {last_date_run.strftime("%d/%m/%Y:%X")}')
print(f'> current datetime = {datetime.now().strftime("%d/%m/%Y:%X")}')


if datetime.now().strftime("%x") == last_date_run.strftime("%x"):
    print(">> program did already run today. No action required")

else:
    print(">> program did not run yet today. Starting")
    log.log(datetime.now())

print(f'{datetime.now()} stop  main aquacontrole module....................................................')
