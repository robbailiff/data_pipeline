from classes.data_extractor.SQLExtractor import SQLExtractor
from classes.data_loader.MinIOLoader import MinIOLoader
from classes.data_loader.S3Loader import S3Loader


def main():

    postgres = SQLExtractor("postgresql://root:development@localhost:5432/dvdrental")
    df = postgres.extract_to_dataframe("SELECT * FROM rental LIMIT 10")
    print(df.head())

    # postgres.extract_to_csv("test.csv", "SELECT * FROM rental LIMIT 10")
    # postgres.extract_to_json("test.json", "SELECT * FROM rental LIMIT 10")

    # =======================
    # Do some transformations
    # =======================

    bucket = MinIOLoader("localhost:9000", "test2-bucket")
    print(bucket._connection)
    # bucket.load_from_dataframe(df, 'rental_first_10.csv')

    # s3 = S3Loader("localhost:9000", "s3-bucket")
    # s3.load_from_dataframe(df, 'S3_rental_first_10.csv')
    # print(s3._bucket_instance)
    # s3.load_from_csv("test.csv", "S3_top10_3.csv")

    # load_dotenv()
    # access_key = os.getenv("MINIO_USER")
    # secret_key = os.getenv("MINIO_PASSWORD")
    #
    # s3 = boto3.resource('s3',
    #                     endpoint_url=f'http://localhost:9000',
    #                     aws_access_key_id=access_key,
    #                     aws_secret_access_key=secret_key,
    #                     # config=Config(signature_version='s3v4'),
    #                     # region_name='us-east-1'
    #                     )
    # print(s3)
    # bucket = s3.create_bucket(Bucket='s3-bucket')
    # b_list = [bucket for bucket in s3.buckets.all()]
    # print(b_list)
    # print(bucket)
    # bucket.upload_file("test.csv", "S3_top10.csv")
    # s3.Bucket('test-bucket').upload_file("test.csv", "S3_top10.csv")

    # bucket.load_from_csv("test.csv", "top10.csv")

    # data = requests.get(
    #     "https://jsonplaceholder.typicode.com/todos/1",
    # ).text.encode()
    #
    # print(data)
    # text_data = io.BytesIO(data)


if __name__ == "__main__":
    main()
