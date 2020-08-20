# this python program will create a daily archive file
# importing the required modules
import os
import shutil
import time
import utils.FileTransfer
# main function
from datetime import datetime
from datetime import date

def archive():

    arch_path = "./archive_logging"

    for filename in os.listdir(arch_path):
        # checking the current directory files
        # print(f'file: {filename}')
        # file path
        file_path = os.path.join(arch_path, filename)
        #os.rename(file_path, file_path + '_' + date.today().__str__())
        if (filename.__str__()[-3:]) == "log":
            print("logfile detected......")
            os.rename(file_path, file_path + '_' + date.today().__str__())
        
            
    utils.FileTransfer.upload()