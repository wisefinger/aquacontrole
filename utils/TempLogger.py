# Class responsible for reading and writing data to the temperature logfile
from datetime import datetime
import os.path
from os import path
class TempLogger:

    def __init__(self):
        #Check if the logfile alreay exist or not, and create a new file is none is present
        if path.exists('logging/temp.log'):
            None
        else:
            with open('logging/temp.log', 'a') as f:
                #f.write(f'{datetime.now().strftime("%d/%m/%Y:%X")}: new log created.')
                #f.write("\n")
                pass
    # append data at the end of the logfile
    def log(self,message):
        with open('logging/temp.log', 'a') as f:
            #f.write(f'{datetime.now().strftime("%d/%m/%Y:%X")}: {message}')
            f.write(f'{message}')
            f.write("\n")

