import pandas as pd
from sqlalchemy import create_engine

from classes.data_extractor.DataExtractor import DataExtractor


class SQLExtractor(DataExtractor):

    def _open_connection(self):
        connection = create_engine(self._endpoint).connect()
        return connection

    def extract_to_csv(self, filepath, query):
        result = self._connection.execute(f"{query}")
        self._write_to_csv(filepath, result)

    def extract_to_dataframe(self, query):
        result = pd.read_sql_query(f"{query}", self._connection)
        return result

    def extract_to_json(self, filepath, query):
        result = self._connection.execute(f"{query}")
        formatted_result = [dict(row) for row in result]
        self._write_to_json(filepath, formatted_result)
