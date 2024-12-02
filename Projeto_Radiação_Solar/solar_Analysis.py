import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#caminho
archive = r'C:\\Users\\Public\\Documents\\Projeto_Radiação_Solar\\SolarPrediction.csv'

def carregarDados(data):
    data = pd.read_csv(archive)

    return data

dados = carregarDados(archive)


def tratamentoDados(dados):

    print(dados.head()) # Mostra 5 primeiras linhas

    print(dados.info()) #Tipos de dados

    print(dados.describe()) # Dados Estatísticos

    print(dados.isnull().sum()) # Verificar e contar valores nulos

    dados.drop_duplicates(inplace=True) ## remove linhas duplicadas em memoria e salva

    dados.dropna(inplace=True) # remove informações null

    # Calcular percentual de valores ausentes
    missing_percentage = dados.isnull().mean() * 100
    print(f"Colunas com muitos valores ausentes: ")
    print(missing_percentage[missing_percentage > 80]) # Mostrar colunas com mais de 80% de valores ausentes

    # Encontrar colunas constantes
    constant_colums = [col for col in dados.columns if dados[col].nunique() == 1]
    print("Colunas com valores constantes:")
    print(constant_colums)

    dados['DateTime'] = pd.to_datetime(dados['UNIXTime'], unit='s') # Converter UNIXTime para datetime

    # Extrair informações de data e hora, se necessário
    dados['Hour'] = dados['DateTime'].dt.hour
    dados['Day'] = dados['DateTime'].dt.day
    dados['Month'] = dados['DateTime'].dt.month
    dados['Year'] = dados['DateTime'].dt.year

     # Corrigir formato TimeSunRise e TimeSunSet
    dados['TimeSunRise'] = pd.to_datetime(
        dados['Data'] + ' ' + dados['TimeSunRise'], 
        format='%m/%d/%Y %I:%M:%S %p', 
        errors='coerce'
    )
    dados['TimeSunSet'] = pd.to_datetime(
        dados['Data'] + ' ' + dados['TimeSunSet'], 
        format='%m/%d/%Y %I:%M:%S %p', 
        errors='coerce'
    )

    # Criar novas colunas com informações temporais
    dados['DaylightHours'] = (dados['TimeSunSet'] - dados['TimeSunRise']).dt.total_seconds() / 3600

    # Filtrar colunas numéricas
    numeric_cols = dados.select_dtypes(include=['number'])
    low_variance_cols = [col for col in numeric_cols.columns if numeric_cols[col].std() < 0.1]
    print("Colunas com baixa variabilidade:", low_variance_cols)

tratamentoDados(dados)

#Selecionado variáveis preditosras e alvo principal
X = dados[['Temperature','Humidity', 'Pressure', 'Speed', 'Hour']]
y = dados['Radiation']

# Seprando dados de trino e dados de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Treinando o Modelo
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Avaliar Modelo
score = model.score(X_test, y_test)
print(f"R² do modelo: {score:.2f}")

X_temp = X[['Temperature']]
X_temp = sm.add_constant(X_temp) # Adicionar uma constante para o modelo
linear_model = sm.OLS(y, X_temp).fit() # Ajustar o modelo

# Previsões
predictions = linear_model.predict(X_temp)

def predicao(X,y):
    plt.figure(figsize=(10,6))
    plt.scatter(X['Temperature'], y, label='Dados Originais', alpha=0.5)
    plt.plot(X['Temperature'], predictions, color='red', label='Linha de Regressão', linewidth=2)
    plt.title('Regressão Linear: Temperatura vs Radiação Solar')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Radiação (W/m²)')
    plt.legend()
    plt.grid()
    plt.show()

predicao(X, y)

def plot1(dados):
    plt.hist(dados['Radiation'], bins=30, color='orange')
    plt.title('Distribuição de Radiação Solar')
    plt.xlabel('Radiação')
    plt.ylabel('Frequência')
    plt.show()

plot1(dados)

def plot2(dados):
    plt.figure(figsize=(10, 5))
    plt.plot(dados['DateTime'], dados['Radiation'], label='Radiação Solar', color='red')
    plt.title('Radiação Solar ao longo do tempo')
    plt.xlabel('Tempo')
    plt.ylabel('Radiação (W/m²)')
    # Média diária de radiação
    daily_radiation = dados.groupby(dados['DateTime'].dt.date)['Radiation'].mean()
    plt.plot(daily_radiation.index, daily_radiation.values, label='Média Diária', color='blue')
    plt.legend()
    plt.show()

plot2(dados)

def plot3(dados):
    sns.scatterplot(x=dados['Temperature'], y=dados['Radiation'], color='blue')
    plt.title('Relação entre Temperatura e Radiação Solar')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Radiação (W/m²)')
    plt.show()

plot3(dados)

def plot4(dados):
    hourly_radiation = dados.groupby('Hour')['Radiation'].mean()

    plt.figure(figsize=(12, 6))
    plt.plot(hourly_radiation.index, hourly_radiation.values, label='Média po Hora', color='green')
    plt.title('Média de Radiação Solar por Hora do Dia')
    plt.xlabel('Hora do Dia')
    plt.ylabel('Radiação Média (W/m²)')
    plt.legend()
    plt.grid()
    plt.show()

plot4(dados)
