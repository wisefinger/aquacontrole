from datetime import datetime, timedelta
print("start aquacontrole ....................................................")
# define a date that contains the data that pumps have been activated
# this will be used to make sure that the pumps are not started several times on the same day
last_date_run = datetime.now() + timedelta(days=-1) #SET TO DAY -1 for testing only!!!!!!!!!!
# ....................................init......................................

#.....................................init.......................................


print(f'> current datetime = {datetime.now().strftime("%d/%m/%Y:%X")}')
print(f'> last day run     = {last_date_run.strftime("%d/%m/%Y:%X")}')

if datetime.now().strftime("%x") == last_date_run.strftime("%x") :
 print(">> program did already run today. No action required")

else:
    print(">> program did not run yet today. Starting")


print("stop aquacontrole ....................................................")