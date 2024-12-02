# Solar_Radiation_Data_Analysis
Este repositório apresenta um projeto completo de análise de dados sobre radiação solar. O objetivo principal é explorar o conjunto de dados, identificar padrões e construir modelos preditivos para entender a relação entre variáveis climáticas e a radiação solar.
Estrutura do Projeto
SolarPrediction.csv: Conjunto de dados utilizado na análise.
solar_analysis.py: Código principal para processamento de dados, modelagem e visualização.
# Ferramentas e Tecnologias
Pandas: Manipulação e limpeza de dados, criação de colunas temporais, e eliminação de valores nulos/duplicados.
Scikit-learn: Divisão dos dados em treino/teste e aplicação do modelo RandomForestRegressor.
Statsmodels: Construção de um modelo de regressão linear para explorar a relação entre temperatura e radiação solar.
Matplotlib e Seaborn: Criação de gráficos para análise visual.
# 🚀 Etapas do Projeto
# 1️⃣ Pré-processamento dos Dados
Conversão de colunas temporais.
Eliminação de duplicatas e valores nulos.
Criação de novas colunas como DaylightHours (horas de luz solar).
Identificação de colunas com baixa variabilidade.
# 2️⃣ Exploração Visual
Histograma: Distribuição da radiação solar.
Gráficos de Linha: Variação de radiação ao longo do tempo e médias diárias.
Gráfico de Dispersão: Relação entre temperatura e radiação solar.
Gráfico por Hora do Dia: Média de radiação por horário.
# 3️⃣ Modelagem Preditiva
Utilização do RandomForestRegressor:
R² do modelo: 0.90.
Análise de um modelo linear simples com statsmodels.
📊 Exemplos de Gráficos
Distribuição da Radiação Solar

Radiação ao Longo do Tempo

Correlação entre Temperatura e Radiação Solar

Radiação Média por Hora do Dia

# 🏆 Resultados Obtidos
O modelo RandomForestRegressor apresentou bom desempenho, com R² de 0.90, demonstrando sua capacidade de prever a radiação solar com base nas variáveis climáticas.
Os gráficos reforçam a forte relação entre temperatura e radiação solar, além de padrões diários consistentes.

# 📬 Contato
Caso tenha dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou entrar em contato:

LinkedIn: https://www.linkedin.com/in/marlonmarquesmdm/
E-mail: marlon.marques.mmd@gmail.com
🌟 Contribuições são bem-vindas!
Sinta-se livre para contribuir com melhorias ou novas funcionalidades para este projeto. 😊
