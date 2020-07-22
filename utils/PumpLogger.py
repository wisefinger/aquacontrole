# Class responsible for reading and writing data to the pump logfile
from datetime import datetime
import os.path
from os import path
class PumpLogger:

    def __init__(self):
        #Check if the logfile alreay exist or not, and create a new file is none is present
        if path.exists('logging/pump.log'):
            None
        else:
            with open('logging/pump.log', 'a') as f:
                f.write(f'{datetime.now().strftime("%d/%m/%Y:%X")}: new log created.')
                f.write("\n")
    # append data at the end of the logfile
    def log(self,message):
        with open('logging/pump.log', 'a') as f:
            f.write(f'{datetime.now().strftime("%d/%m/%Y:%X")}: {message}')
            f.write("\n")

    # get last the last rundate of the logfile
    def getlatest(self):
        with open('logging/pump.log', 'r') as f:
            for line in f:
                line = line.strip(' \t\r\n')

                if line.__contains__(('stop')):
                    print(line)

                pass
        try:
            return line
        except UnboundLocalError:
            print('Empty logfile no previous history')
            return None
