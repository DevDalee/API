import pandas as pd

#Função para inserir uma linha no dataframe
def Insert_row_(row_number, df, row_value):
    #Dividindo o dataset do meio pra cima
    df1 = df[0:row_number]
   
    # Guardando que sobrou do dataset
    df2 = df[row_number:]
   
    #Inserindo uma linha encima
    df1.loc[row_number]=row_value
   
    #Concatenando os dois dataframes
    df_result = pd.concat([df1, df2])
   
    #Remontando os indexes
    df_result.index = [*range(df_result.shape[0])]
   
    return df_result
   
#Criando a linha que queremos inserir
def inserir(valor):
    valor2 = []
    for x in valor:
        valor2.append(x)
    df = pd.read_excel('/home/dalessandro/Desktop/API/dados/dados_teste.xlsx')
    row_number = 0
    row_value = valor2
    #df = df.drop(1)
    print(valor2)
    #print(df)
    try:
        df.to_excel(r'/home/dalessandro/Desktop/API/dados/teste2_novo.xlsx', index = False)
        return True
    except:
        return False
