import pandas
import pydataset


class KungFuPanda:

    def __init__(self):
        self.data_frame = None

    def load_from_file(self, file_path: str):
        self.data_frame = pandas.read_csv(file_path, delimiter=';')
        # if '.xls' in file_path:
        #     self.data_frame = pandas.read_excel(file_path)
        # elif '.csv' in file_path:
        #     self.data_frame = pandas.read_csv(file_path)

    def load_from_pydataset(self, dataset: str):
        self.data_frame = pydataset.data(dataset)

    def get_where(self, column: str, condition: str):
        return self.data_frame.loc[eval(f"self.data_frame['{column}']" + condition)]
