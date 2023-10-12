import os
import boto3
from dotenv import load_dotenv

from classes.data_loader.DataLoader import DataLoader


class S3Loader(DataLoader):

    def __init__(self, endpoint, bucket_name):
        super().__init__(endpoint)
        self._bucket_name = bucket_name
        self._bucket_instance = self._create_bucket()

    def _open_connection(self):
        load_dotenv()
        access_key = os.getenv("MINIO_USER")
        secret_key = os.getenv("MINIO_PASSWORD")

        return boto3.resource('s3',
                              endpoint_url=f'http://{self._endpoint}',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key
                              )

    def _create_bucket(self):
        buckets = [bucket.name for bucket in self._connection.buckets.all()]
        if self._bucket_name not in buckets:
            return self._connection.create_bucket(Bucket=f"{self._bucket_name}")
        else:
            print(f"Bucket {self._bucket_name} already exists")
            return self._connection.Bucket(f"{self._bucket_name}")

    def load_from_csv(self, upload_filepath, file_name, file_type='csv'):
        self._load_file(upload_filepath, file_name, file_type)

    def load_from_dataframe(self, dataframe, file_name, file_type='csv'):
        csv_file = dataframe.to_csv().encode('utf-8')

        self._bucket_instance.put_object(
            Body=csv_file,
            Bucket=self._bucket_name,
            Key=file_name,
            ContentType=f'application/{file_type}'
        )

    def load_from_json(self, upload_filepath, file_name, file_type='json'):
        self._load_file(upload_filepath, file_name, file_type)

    def _load_file(self, upload_filepath, file_name, file_type):
        self._bucket_instance.upload_file(
            upload_filepath,
            file_name,
            ExtraArgs={'ContentType': f'application/{file_type}'}
        )
