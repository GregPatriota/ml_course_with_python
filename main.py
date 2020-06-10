from dataset_iris.class01 import load_dataset, plot02, sort_asc
from os import path
from pandas_dataframe.class01 import LittlePanda
from pandas_dataframe.class02 import KungFuPanda
from pandas_dataframegroupeby.class01 import GroupByDataFrama

if __name__ == '__main__':
    # data = load_dataset(path.join('dataset_iris', 'iris.data'))
    # sorted01 = sort_asc(data[:50, 0])
    # sorted02 = sort_asc(data[50:100,0])
    # plot02(sorted01, 'Comp. Sépala Iris-Setosa', sorted02, 'Comp. Sépala Iris-Versicolo')
    # little_panda = LittlePanda([
    #     ['fchollet/keras', 11302], ['openai/universe', 4350], ['pandas-dev/pandas', 8168]
    # ])
    # little_panda = LittlePanda([
    #     ['PE', 'Pernambuco', 'Recife'], ['RJ', 'Rio de Janeiro', 'Rio de Janeiro'],
    #     ['PB', 'Paraíba', 'João Pessoa'], ['SP', 'São Paulo', 'São Paulo'],
    #     ['MG', 'Minas Gerais', 'Belo Horizonte'], ['CE', 'Ceará', 'Fortaleza'],
    #     ['AC', 'Acre', 'Rio Branco'], ['MA', 'Maranhão', 'São Luís'], ['RN', 'Rio Grande do Norte', 'Natal'],
    #     ['PR', 'Paraná', 'Curitiba'], ['RS', 'Rio Grande do Sul', 'Porto Alegre']
    #     ], ['Sigla', 'Nome', 'Capital']
    # )
    # print('Before')
    # print(little_panda.to_print())
    # little_panda.change_indexes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    # print('After')
    # print(little_panda.to_print())
    # little_panda.change_indexes(['Melhor', 'Suave', 'Arretado', 'Gigante', 'Bao', 'Fuderoso', 'Nunca fui',
    #                              'Quero ir', 'Oww Safadao', 'Bora ver', 'Eita'])
    # print('After')
    # print(little_panda.to_print())

    # kungfu = KungFuPanda()
    # kungfu.load_from_file(path.join('pandas_dataframe', 'copacabana.csv'))
    # ret = kungfu.get_where('DistPraia', ' <= 40')
    # print(ret)

    data = GroupByDataFrama(path.join('pandas_dataframegroupeby', 'original.csv'))
    data.group_by_column('state')
    data.filter_lambda(lambda x: x['votes'].sum() > 1000000)



