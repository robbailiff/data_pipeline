import os
from dotenv import load_dotenv
from minio import Minio
from io import BytesIO

from data_pipeline.classes.data_loader.DataLoader import DataLoader


class MinIOLoader(DataLoader):

    def __init__(self, endpoint, bucket_name):
        super().__init__(endpoint)
        self._bucket_name = bucket_name
        self._create_bucket()

    def _open_connection(self):
        load_dotenv()
        access_key = os.getenv("MINIO_USER")
        secret_key = os.getenv("MINIO_PASSWORD")

        return Minio(self._endpoint, access_key=access_key, secret_key=secret_key, secure=False)

    def _create_bucket(self):
        bucket_exists = self._connection.bucket_exists(self._bucket_name)
        if not bucket_exists:
            return self._connection.make_bucket(f"{self._bucket_name}")
        else:
            print(f"Bucket {self._bucket_name} already exists")

    def load_from_csv(self, upload_filepath, file_name, file_type='csv'):
        self._load_file(upload_filepath, file_name, file_type)

    def load_from_dataframe(self, dataframe, file_name, file_type='csv'):
        csv_file = dataframe.to_csv().encode('utf-8')
        csv_buffer = BytesIO(csv_file)

        self._connection.put_object(
            self._bucket_name,
            file_name,
            csv_buffer,
            length=len(csv_file),
            content_type=f'application/{file_type}'
        )

    def load_from_json(self, upload_filepath, file_name, file_type='json'):
        self._load_file(upload_filepath, file_name, file_type)

    def _load_file(self, upload_filepath, file_name, file_type):
        self._connection.fput_object(
            self._bucket_name,
            file_name,
            upload_filepath,
            content_type=f'application/{file_type}'
        )
