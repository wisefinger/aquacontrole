import time
from datetime import datetime
from utils.ActionLogger import ActionLogger
# declare check condition to stop module
from utils.PumpLogger import PumpLogger
stopsignal = False
# declare polling time for checking if all pump cycles have already been done today in minutes
polling = 15
# declare number of waterchanges per day
changes = 3
# declare the duration of the pump interval in minutes
# 5 minutes is about 27 liters
duration = 5
# declare start hours (00h00 + x), first run will start at x hours
start = 9
# declare number of hours between runs
pause = 4

print("DONT FORGET TO ADD THE ARCHIVING PROCESS TO A CRON JOB")
print(f'> {datetime.now()} : start run watercycle process................')
# Create an instance to log actions into the generic /logger/action.log
actionlogger = ActionLogger()
actionlogger.log("start run_wc.py")


while not stopsignal:
    print(f' > pause loop check for {polling} minutes')
    time.sleep(polling * 60)

    number = 1

    while number <= changes:
        # print("   > start check run : " + str(number))
        # initiate class for log creation/update/check
        pumplogger = PumpLogger(number)
        # Check if the daily water change has already ran today for this number. If not start it now
        if pumplogger.getlatest() == None:
            print(f"   > No previous run  was found for turn {number} today, action required ")

            if number == 1:
                print(f"     > waiting for  {start} hours before starting first run ")
                time.sleep(start * 60 * 60)

            else:
                print(f"     > waiting for  {pause} hours before starting run {number}" )
                time.sleep(pause * 60 * 60)

            pumplogger.log("start pump")
            time.sleep(polling * 5)
            #pump.waterchange(5 * 60)
            pumplogger.log("stop pump")
        else:
            print(f"   > A previous run  was found for turn {number} today, no action required  ")
        # was already started today. If not the case start the pump
        number = number + 1

actionlogger.log("end run_wc.py")
print(f'> {datetime.now()} : start run watercycle process................')