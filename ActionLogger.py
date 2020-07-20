# Class responsible for logging all actions
class ActionLogger:
    x=5

    def bb(self):
        return self.x

    # append data at the end of the logfile
    def log(self,datetime):
        print(f'Writing to logfile = {datetime}')
        with open('logging/worker.log', 'a') as f:
            f.write(datetime.strftime("%d/%m/%Y:%X \n"))
