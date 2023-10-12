import pytest
from io import BytesIO
from unittest.mock import patch, PropertyMock

from src.data_pipeline.classes.data_loader.MinIOLoader import MinIOLoader


class TestMinIOLoader:

    @patch("src.data_pipeline.classes.data_loader.MinIOLoader.Minio")
    def test_constructor(self, mock_minio):
        endpoint = 'localhost:5000'
        bucket_name = 'example_bucket'
        type(mock_minio.return_value).ok = PropertyMock(return_value='Connection object')

        loader = MinIOLoader(endpoint, bucket_name)

        assert loader._endpoint == endpoint
        assert loader._bucket_name == bucket_name
        assert loader._connection.ok == 'Connection object'
        mock_minio.assert_called_once()
        mock_minio.assert_called_with(endpoint, access_key='minio', secret_key='minio123', secure=False)

    @patch("src.data_pipeline.classes.data_loader.MinIOLoader.MinIOLoader.load_from_csv")
    @patch("src.data_pipeline.classes.data_loader.MinIOLoader.Minio")
    def test_load_from_csv(self, mock_minio, mock_load):
        endpoint = 'localhost:5000'
        bucket_name = 'example_bucket'
        file = BytesIO()

        loader = MinIOLoader(endpoint, bucket_name)
        loader.load_from_csv(file, 'test.csv')

        mock_minio.assert_called_once()
        mock_load.assert_called_once()
        mock_load.assert_called_with(file, 'test.csv')

    def test_load_from_dataframe(self):
        pass

    @patch("src.data_pipeline.classes.data_loader.MinIOLoader.MinIOLoader.load_from_json")
    @patch("src.data_pipeline.classes.data_loader.MinIOLoader.Minio")
    def test_load_from_json(self, mock_minio, mock_load):
        endpoint = 'localhost:5000'
        bucket_name = 'example_bucket'
        file = BytesIO()

        loader = MinIOLoader(endpoint, bucket_name)
        loader.load_from_json(file, 'test.json')

        mock_minio.assert_called_once()
        mock_load.assert_called_once()
        mock_load.assert_called_with(file, 'test.json')

    def test_load_file(self):
        pass
