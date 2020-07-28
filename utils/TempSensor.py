from utils.TempLogger import TempLogger

#Class responsible for managing temperature sensor


class TempSensor:
    templogger = TempLogger()

    def __init__(self):
        pass

    def getTemp(self):
        self.templogger.log("test")
        return "25"
