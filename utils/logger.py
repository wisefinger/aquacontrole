# Class responsible for reading and writing data to the worker logfile
class Logger:
    # append data at the end of the logfile
    def log(self,datetime):
        print(f'Writing to logfile = {datetime}')
        with open('../logging/action.log', 'a') as f:
            f.write(datetime.strftime("%d/%m/%Y:%X \n"))

    # get last 10 lines of the logfile
    def getlatest(self):
        with open('../logging/action.log', 'r') as f:
            for last_line in f:
                print(f'last time run {last_line}')
                pass
        try:
            return last_line.strip(' \t\r\n')
        except UnboundLocalError:
            print('Empty logfile no previous history')
            return None
