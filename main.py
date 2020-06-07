from dataset_iris.class01 import load_dataset, plot02, sort_asc
from os import path

if __name__ == '__main__':
    data = load_dataset(path.join('dataset_iris', 'iris.data'))
    sorted01 = sort_asc(data[:50, 0])
    sorted02 = sort_asc(data[50:100,0])
    plot02(sorted01, 'Comp. Sépala Iris-Setosa', sorted02, 'Comp. Sépala Iris-Versicolo')
