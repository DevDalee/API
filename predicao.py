#mensagens de aviso se houver falhas
import warnings
warnings.filterwarnings("ignore")

#import padrão para manipulação da base de dados e plot de resultados
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#melhores regressores
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import LinearSVR

#metricas para analise (Coeficiente de determinação, Erro médio absoluto e Erro quadrado médio).
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse

#modolos para divisão de traino e teste.
from sklearn.model_selection import train_test_split

#modulos para selecao dos melhores atributos
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.feature_selection import f_regression

#Padroniza recursos removendo a média e dimensionando para a variação da unidade.
from sklearn.preprocessing import StandardScaler

#Leitura do datasete
#print(dados.keys())


#Remoção dos parametros não nescessarios
def drop(tdado):
    tdado = tdado.drop(['Lote','Datacol', 'diacol', 'mescol', 'anocol', 'Propriedade',
                        'Municipio', 'UF', 'Raca', 'NomeAnimal', 'tatuagem/brinco',
                        'animal/ARCO', 'NomedoPai', 'NumeroPai', 'pai', 'Nome da Mãe ',
                        'NumeroMae', 'mae','Idade', 'DataNasc', 'Dian', 'Mesn','Anon',
                        'IdadeansCalc', 'FAMACHA','CESC','EGE'],1)
    return tdado

#Divisão treino X teste
def div_train_test(X,y):
    reg = RandomForestRegressor()
    print(reg)
    X_train, X_test, y_train, y_test = train_test_split(np.asarray(X), np.asarray(y), test_size=0.3)
    X_train = StandardScaler().fit_transform(X_train)
    X_test = StandardScaler().fit_transform(X_test)
    reg.fit(X_train,y_train)
    pred = reg.predict(X_test)
    r2 = r2_score(y_test, pred)
    mae_ = mae(y_test, pred)
    mse_ = mse(y_test, pred)
    return reg

#Converte todos os dados categoricos em númericos
def conversao_bin(tdado):
    tdado['Sexo'] = tdado['Sexo'].replace(['F','M'],[0,1])
    #print (tdado.dtypes)
    tdado['ECC'] = tdado['ECC'].astype(float)
    return tdado

def execusoes():
    dados = pd.read_excel('/home/dalessandro/Desktop/API/dados/dados1.xlsx')
    teste2 = pd.read_excel('/home/dalessandro/Desktop/API/dados/teste2_novo.xlsx')
    teste = drop(teste2)
    dados2 = drop(dados)

    #Conversão
    dados2 = conversao_bin(dados2)
    teste = conversao_bin(teste)

    #Remoção de Atributos vazios
    dados2.dropna(inplace=True)
    teste.dropna(inplace=True)

    x_teste2 = teste.drop('aol',1)
    X = dados2.drop('aol',1) #X recebe tudo menos o AOL
    y = dados2['aol'] #y recebe somente o AOL

    reg = div_train_test(X,y)
    pred2 = reg.predict(x_teste2)
    return pred2