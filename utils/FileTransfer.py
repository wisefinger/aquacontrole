# author  : Kris & Seth Cardoen
# created : 20/07/2020
# purpose : Responsible for uploading files into the cloud
import os
import shutil
import zipfile
import boto3 
from botocore.client import Config

print("starting FileTransfer .................................................................")
def upload():
    files_moved_counter = 0
    print('starting the transfer')
    # specify the path
    path_input = "/home/pi/code/aquacontrole/archive_logging"
    path_workdir = "/home/pi/code/aquacontrole/transfer_queue"
    path_output = "/home/pi/code/aquacontrole/transferred_files"
    

    # move files transfer_queue for processing
    for filename in os.listdir(path_input):
        #print(filename)
        print('from  ' + path_input + '/' + filename)
        print('tot   '+ path_workdir + '/' + filename)
        os.rename(path_input + '/' + filename, path_workdir + '/' + filename)

    # zip files
    print('start zipping the files')
    for filename in os.listdir(path_workdir):
        #print('>' + filename.__str__()[-14:-11])
        if (filename.__str__()[-14:-11]) == "log":
            # zip the file before starting the transfer
            zipfile.ZipFile(path_workdir + "/" + filename + ".zip", mode='w').write(path_workdir + "/" + filename)
            # remove the original file
            os.remove(path_workdir + "/" + filename)
        else:
            pass

    BUCKET_NAME = 'aquacontrole'
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(BUCKET_NAME)

    for filename in os.listdir(path_workdir):
        print("send file " + path_workdir + "/" + filename)
        data = open(path_workdir + "/" + filename,'rb')
        FILE_NAME = filename
        s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data)
        shutil.move(path_workdir + "/" + filename, path_output + "/" + filename)

#upload()

print("stopping FileTransfer .................................................................")
