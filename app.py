from datetime import datetime, timedelta
# import utils.pump
from utils.pump import init
from logger import Logger

print("start aquacontrole ....................................................")
# define a date that contains the data that pumps have been activated


log = Logger()

# pumpy = utils.pump
init()


# get last rundate from logfile
try:
    last_date_run = datetime.strptime(log.getlatest(),"%d/%m/%Y:%X")
except ValueError:
    # Set last run to day -1 to make sure the task will run
    last_date_run = datetime.today() - timedelta(days=1)

print(f'> current datetime = {datetime.now().strftime("%d/%m/%Y:%X")}')
print(f'> last day run     = {last_date_run.strftime("%d/%m/%Y:%X")}')

if datetime.now().strftime("%x") == last_date_run.strftime("%x"):
    print(">> program did already run today. No action required")

else:
    print(">> program did not run yet today. Starting")
    log.log(datetime.now())

print("stop aquacontrole ....................................................")
