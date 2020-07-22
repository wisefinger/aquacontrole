# Class responsible for logging all actions
# all the actions are written to file under /logger/action.log
from datetime import datetime
import os.path
from os import path

class ActionLogger:


    def __init__(self):
        #Check if the logfile alreay exist or not, and create a new file is none is present
        if path.exists('logging/action.log'):
            None
        else:
            with open('logging/action.log', 'a') as f:
                f.write(f'{datetime.now().strftime("%d/%m/%Y:%X")}: new log created.')
                f.write("\n")
    # append data at the end of the logfile
    def log(self,message):
        with open('logging/action.log', 'a') as f:
            f.write(f'{datetime.now().strftime("%d/%m/%Y:%X")}: {message}')
            f.write("\n")

