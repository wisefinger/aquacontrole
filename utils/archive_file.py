# this python program will create a daily archive file
# importing the required modules
import os
import shutil
import time

# main function
from datetime import date


def archive():
    # initializing the count
    deleted_files_count = 0

    # specify the path
    path = "./logging"
    arch_path = "./archive_logging"

    # specify the days
    days = 1

    # converting days to seconds
    # time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)
    # print(f'current time in seconds : {seconds}')
    # print(f'path defined : {path}')

    # checking whether the file is present in path or not
    for filename in os.listdir(path):
        # checking the current directory files

        # print(f'file: {filename}')
        # file path
        file_path = os.path.join(path, filename)

        fileseconds = os.stat(path + '/' + filename).st_ctime
        seconds_difference = seconds - fileseconds
        minutes_difference = seconds_difference / 60
        hours_difference = minutes_difference / 60
        days_difference = hours_difference / 24

        # comparing the days
        # print(f'seconds_difference:{seconds_difference} ')
        # print(f'minutes_difference:{minutes_difference} ')
        # print(f'hours_difference:{hours_difference} ')
        # print(f'days_difference:{days_difference} ')

        if seconds >= os.stat(path + '/' + filename).st_ctime:
            print("file needs to be archived......")
            os.rename(path + '/' + filename, './archive_logging/' + filename + '_' + date.today().__str__())

