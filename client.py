import boto3
from botocore.exceptions import NoCredentialsError

# Replace these with your details
ACCESS_KEY = 'YOUR ACCESS KEY'
SECRET_KEY = 'YOUR SECRET KEY'
BUCKET_NAME = 'YOUR BUCKET NAME'
ENDPOINT = 'https://eu-west-1.storage.impossibleapi.net'
REGION = 'eu-west-1'

# Initialize the S3 client for Impossible Cloud
s3 = boto3.client('s3',
                  aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY,
                  endpoint_url=ENDPOINT,
                  region_name=REGION)  # Ensure region matches endpoint

def upload_file(file_path, object_name):
    print("Upload file")
    """
    Upload a file to Impossible Cloud.

    :param file_path: Local file path to upload
    :param object_name: Name for the file on Impossible Cloud (e.g., 'folder/filename')
    :return: None
    """
    try:
        s3.upload_file(file_path, BUCKET_NAME, object_name)
        print(f"File uploaded successfully: {object_name}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_file(object_name, download_path):
    print("Download file")
    """
    Download a file from Impossible Cloud.

    :param object_name: The file object name on Impossible Cloud
    :param download_path: Path to save the downloaded file locally
    :return: None
    """
    try:
        s3.download_file(BUCKET_NAME, object_name, download_path)
        print(f"File downloaded successfully: {object_name}")
    except FileNotFoundError:
        print(f"File not found: {object_name}")
    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    print("Starting program")
    # Upload file
    file_path_to_upload = 'examplefile.txt'
    object_name_to_upload = 'examplefolder/examplefile.txt'
    upload_file(file_path_to_upload, object_name_to_upload)

    # Download file
    object_name_to_download = 'examplefolder/examplefile.txt'
    download_path = 'examplefiledownloaded.txt'
    download_file(object_name_to_download, download_path)
