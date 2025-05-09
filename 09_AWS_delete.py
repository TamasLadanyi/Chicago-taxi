import boto3
import os

# identify the AWS credentials
AWS_Access_key = os.getenv('AWS_Access_key')
AWS_Secret_access_key = os.getenv('AWS_Secret_access_key')

s3 = boto3.client('s3', aws_access_key_id=AWS_Access_key, aws_secret_access_key=AWS_Secret_access_key)  # noqa: E501


# list function
def list_from_s3(bucket: str, path: str, file_format: str) -> list:
    """
    List all files in a specified S3 bucket.

    Parameters
    ----------
    bucket : str
        Describe the bucket name
    path : str
        Describe the path name where the file is located
    file_format : str
        describe the file format, for example: csv, json, etc.

    Returns
    -------
    list
        List from the S3 bucket, which contains the file names
    """
    s3 = boto3.client('s3')

    list_from_s3 = []
    # List all objects in the specified bucket and prefix
    for file in s3.list_objects(Bucket=bucket, Prefix=path)['Contents']:
        list_key = file['Key']

        if list_key.split('/')[-1].strip() != '':
            if list_key.split('.')[1] == file_format:

                filename = list_key.split('/')[-1]
                list_from_s3.append(filename)

    return list_from_s3


# delete function
def delete_from_s3(bucket: str, file_list: list, path: str) -> None:
    """
    This function deletes the first 7 files from a specified list
    in an S3 bucket.

    Parameters
    ----------
    bucket : str
        bucket name
    file_list : list
        The list of all files, the first 7 files will be deleted
    path : str
        path name where the file is located in the bucket

    Returns
    -------
    None
        This function does not return anything.
        It prints the names of the files that were deleted.
    """
    s3 = boto3.client('s3')
    files_to_delete = file_list[0:7]
    print("Files to be delete:", files_to_delete)

    if files_to_delete:
        for obj in files_to_delete:
            full_key = f"{path}{obj}"
            s3.delete_object(Bucket=bucket, Key=full_key)
            print(f"Deleted: {full_key}")
    else:
        print("No objects found in the bucket.")

    return None


# taxi_trip delete
my_bucket = 'chichago-taxi'
taxi_trips_path = 'transformed_data/taxi_trips/'
file_format = "csv"

taxi_trip_file_name_list = list_from_s3(my_bucket, taxi_trips_path, file_format)  # noqa: E501
print(taxi_trip_file_name_list)
delete_from_s3(my_bucket, taxi_trip_file_name_list, taxi_trips_path)

# weather delete
my_bucket = 'chichago-taxi'
weather_path = 'transformed_data/weather/'
file_format = "csv"

weather_file_name_list = list_from_s3(my_bucket, weather_path, file_format)
print(weather_file_name_list)
delete_from_s3(my_bucket, weather_file_name_list, weather_path)

# raw data delete
my_bucket = 'chichago-taxi'
raw_taxi_trips_path = 'raw_data/processed/taxi_data/'
file_format = "json"

raw_taxi_trips_name_list = list_from_s3(my_bucket, raw_taxi_trips_path, file_format)  # noqa: E501
print(raw_taxi_trips_name_list)
delete_from_s3(my_bucket, raw_taxi_trips_name_list, raw_taxi_trips_path)

my_bucket = 'chichago-taxi'
raw_weather_name_path = 'raw_data/processed/weather_data/'
file_format = "json"

raw_weather_name_list = list_from_s3(my_bucket, raw_weather_name_path, file_format)  # noqa: E501
print(raw_weather_name_list)
delete_from_s3(my_bucket, raw_weather_name_list, raw_weather_name_path)
