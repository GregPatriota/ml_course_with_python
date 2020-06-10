from asyncore import file_wrapper

import pandas
import numpy


class GroupByDataFrama:

    def __init__(self, path_file: str):
        self.dataframe = pandas.read_csv(path_file)
        self.group_by = None

    def group_by_column(self, column: str, aggregate: str = None):
        self.group_by = self.dataframe.groupby(column)
        if aggregate is not None:
            print(self.group_by.aggregate({aggregate: [min, numpy.mean, max]}))

    def filter_lambda(self, func):
        print(self.group_by.filter(func))


