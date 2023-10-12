from abc import ABCMeta, abstractmethod


class DataLoader(metaclass=ABCMeta):

    def __init__(self, endpoint):
        self._endpoint = endpoint
        self._connection = self._open_connection()

    @abstractmethod
    def _open_connection(self):
        raise NotImplementedError

    @abstractmethod
    def load_from_csv(self, filepath, file_name, file_type):
        raise NotImplementedError

    @abstractmethod
    def load_from_dataframe(self, dataframe, file_name, file_type):
        raise NotImplementedError

    @abstractmethod
    def load_from_json(self, filepath, file_name, file_type):
        raise NotImplementedError
