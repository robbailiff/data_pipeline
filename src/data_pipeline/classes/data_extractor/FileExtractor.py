from data_pipeline.classes.data_extractor.DataExtractor import DataExtractor


class FileExtractor(DataExtractor):

    def _open_connection(self):
        pass

    def extract_to_csv(self, filepath, query):
        pass

    def extract_to_dataframe(self, query):
        pass

    def extract_to_json(self, filepath, query):
        pass
