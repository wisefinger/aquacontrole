# Class responsible for reading and writing data to the pump logfile
from datetime import datetime
import os.path
from os import path
class PumpLogger:

    def __init__(self, id):
        self.id = id
        #Check if the logfile alreay exist or not, and create a new file is none is present
        if path.exists(f'logging/pump{self.id}.log'):
            None
        else:
            with open(f'logging/pump{self.id}.log', 'a') as f:
                f.write(f'{datetime.now().strftime("%d/%m/%Y:%X")}: new log created.')
                f.write("\n")
    # append data at the end of the logfile
    def log(self,message):
        
        if path.exists(f'logging/pump{self.id}.log'):
            with open(f'logging/pump{self.id}.log', 'a') as f:
                f.write(f'{datetime.now().strftime("%d/%m/%Y:%X")}: {message}')
                f.write("\n")
                
        else:
            with open(f'logging/pump{self.id}.log', 'a') as f:
                f.write(f'{datetime.now().strftime("%d/%m/%Y:%X")}: new log created.')
                f.write("\n")
                
                

    # get last the last rundate of the logfile
    def getlatest(self):
        #print(f' self:logging/pump{self.id}.log')
        if path.exists(f'logging/pump{self.id}.log'):

            with open(f'logging/pump{self.id}.log', 'r') as f:
                for line in f:
                    line = line.strip(' \t\r\n')
                    if line.__contains__(('stop')):
                        last_line = line
                    pass
            try:
                if last_line.__contains__(('stop')):
                    return last_line
                else:
                    return None
            except UnboundLocalError:
                #print('Empty logfile no previous history')
                pass
        
        else:
            with open(f'logging/pump{self.id}.log', 'a') as f:
                f.write(f'{datetime.now().strftime("%d/%m/%Y:%X")}: new log created.')
                f.write("\n")
            return None
    