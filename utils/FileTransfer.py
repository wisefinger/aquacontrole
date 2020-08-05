# author  : Kris & Seth Cardoen
# created : 20/07/2020
# purpose : Responsible for uploading files into the cloud
import os
import shutil
import zipfile

from botocore.exceptions import ClientError

print("starting FileTransfer .................................................................")
# Based on web https://realpython.com/python-boto3-aws-s3/
# Import AWS Lib for Python
import boto3

# Define high level interface for S3
s3_resource = boto3.resource('s3')

s3 = boto3.client('s3')

# Show current session settings
print(f'> region name       :{boto3.session.Session().region_name}')
print(f'> active profile    :{boto3.session.Session().profile_name}')


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print.error(e)
        return False
    return True


def archive():
    files_moved_counter = 0

    # specify the path
    path_input = "./archive_logging"
    path_workdir = "./transfer_queue"
    path_output = "./transferred_files"

    # move files transfer_queue for processing
    for filename in os.listdir(path_input):
        shutil.move(path_input + "/" + filename, path_workdir + "/" + filename)

    # zip files
    for filename in os.listdir(path_workdir):
        if (filename.__str__()[-4:]) == ".log":
            # zip the file before starting the transfer
            zipfile.ZipFile(path_workdir + "/" + filename + ".zip", mode='w').write(path_workdir + "/" + filename)
            # remove the original file
            os.remove(path_workdir + "/" + filename)
        else:
            pass

    # start transfer of the zip files

    for filename in os.listdir(path_workdir):
        print("send file " + filename)
        with open(path_workdir + "/" + filename, "rb") as f:
            s3.upload_fileobj(f, "aquacontrole", filename)
        shutil.move(path_workdir + "/" + filename, path_output + "/" + filename)

archive()

print("stopping FileTransfer .................................................................")
