import pandas


class LittlePanda:

    def __init__(self, frame: list, column_name: list):
        self.data_frame = pandas.DataFrame(
            frame,
            columns=column_name
        )

    def shape(self):
        return self.data_frame.shape

    def get_indexes(self):
        return self.data_frame.index

    def to_print(self):
        return self.data_frame

    def change_indexes(self, new_idx: list):
        self.data_frame.index = pandas.Index(new_idx)
        print(self.data_frame)

