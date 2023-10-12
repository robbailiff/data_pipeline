from abc import ABCMeta, abstractmethod
import csv
import json


class DataExtractor(metaclass=ABCMeta):

    def __init__(self, endpoint):
        self._endpoint = endpoint
        self._connection = self._open_connection()

    @abstractmethod
    def _open_connection(self):
        raise NotImplementedError

    @abstractmethod
    def extract_to_csv(self, filepath, data):
        raise NotImplementedError

    @abstractmethod
    def extract_to_dataframe(self, data):
        raise NotImplementedError

    @abstractmethod
    def extract_to_json(self, filepath, data):
        raise NotImplementedError

    @staticmethod
    def _write_to_csv(filepath, data):
        with open(f'{filepath}', 'w+') as file:
            writer = csv.writer(file)
            writer.writerow(data.keys())
            writer.writerows(data)

    @staticmethod
    def _write_to_json(filepath, data):
        with open(filepath, "w") as json_file:
            return json.dump(data, json_file, default=str)
