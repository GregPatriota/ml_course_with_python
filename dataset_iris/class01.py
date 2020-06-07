import numpy
from matplotlib import pyplot


def load_dataset(path: str):
    return numpy.genfromtxt(path, delimiter=',', usecols=(0, 1, 2, 3))


def plot01(data01: list, label01: str, data02: list, label02: str):
    pyplot.plot(data01, c='Red', ls=':', marker='s', ms=8, label=label01)
    pyplot.plot(data02, c='Black', ls=':', marker='o', ms=8, label=label02)
    pyplot.legend()
    pyplot.savefig("sample01.png")


def plot02(data01: list, label01: str, data02: list, label02: str):
    pyplot.plot(data01, c='Red', label=label01)
    pyplot.plot(data02, c='Black', label=label02)
    pyplot.legend()
    pyplot.savefig("sample01.png")


def sort_asc(data: list):
    return numpy.sort(data)
