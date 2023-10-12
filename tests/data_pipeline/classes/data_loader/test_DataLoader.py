import pytest

from data_pipeline.classes.data_loader.DataLoader import DataLoader


class DummyClassImplemented(DataLoader):

    def _open_connection(self):
        pass
        # super(DummyClassImplemented, self)._open_connection()

    def load_from_csv(self, filepath, file_name, file_type):
        # super(DummyClassImplemented, self).load_from_csv(filepath, file_name, file_type)
        pass

    def load_from_dataframe(self, dataframe, file_name, file_type):
        # super(DummyClassImplemented, self).load_from_dataframe(dataframe, file_name, file_type)
        pass

    def load_from_json(self, filepath, file_name, file_type):
        # super(DummyClassImplemented, self).load_from_json(filepath, file_name, file_type)
        pass


class DummyClassNotImplemented(DataLoader):

    def _open_connection(self):
        pass
        # super(DummyClassNotImplemented, self)._open_connection()

    def load_from_csv(self, filepath, file_name, file_type):
        # super(DummyClassNotImplemented, self).load_from_csv(filepath, file_name, file_type)
        pass

    def load_from_dataframe(self, dataframe, file_name, file_type):
        # super(DummyClassNotImplemented, self).load_from_dataframe(dataframe, file_name, file_type)
        pass


class TestDataLoader:

    def test_implemented_class(self):
        try:
            DummyClassImplemented('localhost:5000').load_from_dataframe('df', 'name', 'type')
        except TypeError as e:
            raise pytest.fail(f"Raised the exception {e}")

    def test_unimplemented_class(self):
        with pytest.raises(TypeError):
            DummyClassNotImplemented('localhost:5000').load_from_dataframe('df', 'name', 'type')
        # assert type(error.value.__cause__) is ValueError
