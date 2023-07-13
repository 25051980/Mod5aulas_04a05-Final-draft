#!/usr/bin/env python
# coding: utf-8

# # Tarefa 02 Módulo 05
# 
# O nosso projeto desta sequência de módulos do curso será um aprofundamento da demonstração sobre classificação de risco de crédito que vimos lá no comecinho. Pois recebemos uma base já montada pra nós. Tenha certeza de que ela passou por um longo processamento até ficar daquele jeito. Neste exercício vamos exercitar o que aprendemos nas ultimas aulas e montar a variável resposta da base do nosso projeto.
# 
# # Marcação de bom e mau
# O objetivo da modelagem é classificar o risco de inadimplência, ou como se diz no meio, o risco de *default*. Podemos fazer longas discussões sobre o conceito de *default* com base em estudos e exigências regulatórias, para efeitos deste estudo, um cliente em *default* é aquele que está em 60 dias de atraso ou mais. Então classificaremos os clientes como 'bons' e 'maus' assim:
# - **Maus** pagadores: são aqueles que entraram em 'default' (atraso 60 dias ou mais) nos 24 meses seguintes à aquisição do cartão de crédito. 
# - **Bons** pagadores: são considerados todos os demais.
# - **Excluídos**: Clientes que não adquiriram um cartão de crédito (seja por recusa, seja por desistência) não possuem informações de pagamento, portanto não se pode identificar se são bons ou maus. Há uma longa discussão e literatura sobre *inferência de rejeitados* que está fora do escopo deste exercício.
# 
# #### Bases disponíveis
# Temos duas bases importantes aqui: uma de propostas, com diversas informações dos vários solicitantes de cartão de crédito, e uma base de pagamentos. A base de pagamentos será utilizada para identificar a ocorrência de *default*. A base de propostas tem diversas informações coletadas no momento da solicitação do crédito (isto é importante: qualquer informação posterior a essa data é impossível de ser coletada na aplicação do modelo e não pode ser utilizada).
# 
# As variáveis delas são:
# 
# Base de propostas - application_records.csv
# 
# | Nome da Variável         | Description                                         | Tipo  |
# | ------------------------ |:---------------------------------------------------:| -----:|
# | ID| identificador do cliente (chave) |inteiro|
# | CODE_GENDER| M = 'Masculino'; F = 'Feminino' |M/F|
# | FLAG_OWN_CAR| Y = 'possui'; N = 'não possui' |Y/N|
# | FLAG_OWN_REALTY| Y = 'possui'; N = 'não possui' |Y/N|
# | CNT_CHILDREN| Quantidade de filhos |inteiro|
# | AMT_INCOME_TOTAL| Annual income |inteiro|
# | NAME_INCOME_TYPE|Tipo de renda (ex: assaliariado, autônomo etc) | texto |
# | NAME_EDUCATION_TYPE| Nível de educação (ex: secundário, superior etc) |texto|
# | NAME_FAMILY_STATUS | Estado civil (ex: solteiro, casado etc)| texto |
# | NAME_HOUSING_TYPE | tipo de residência (ex: casa/apartamento, com os pais etc) | texto |
# | DAYS_BIRTH | Count backwards from current day (0), -1 means yesterday |inteiro|
# | DAYS_EMPLOYED | Count backwards from current day (0), -1 means yesterday |inteiro|
# | FLAG_MOBIL | Indica se possui celular (1 = sim, 0 = não) |binária|
# | FLAG_WORK_PHONE | Indica se possui telefone comercial (1 = sim, 0 = não) |binária|
# | FLAG_PHONE | Indica se possui telefone (1 = sim, 0 = não) |binária|
# | FLAG_EMAIL | Indica se possui e-mail (1 = sim, 0 = não) |binária|
# | OCCUPATION_TYPE | Occupation	 |Qualitativa|
# | CNT_FAM_MEMBERS | quantidade de pessoas na residência |inteiro|
# 
# Base de pagamentos - pagamentos_largo.csv  
# 
# | Nome da Variável         | Description                                         | Tipo  |
# | ------------------------ |:---------------------------------------------------:| -----:|
# | ID| identificador do cliente (chave) |inteiro|
# | mes_00 a mes_24| faixa de atraso mês a mês do cliente <br>0: 1-29 days past due &nbsp;&nbsp;&nbsp;&nbsp; 1: 30-59 days past due <br />2: 60-89 days overdue &nbsp;&nbsp;&nbsp;&nbsp; 3: 90-119 days overdue <br /> 4: 120-149 days overdue &nbsp;&nbsp;&nbsp;&nbsp; 5: more than 150 days <br />C: paid off that month &nbsp;&nbsp;&nbsp;&nbsp; X: No loan for the month |Qualitativa|
# 
# #### Construindo a variável resposta
# A base de pagamentos está em um formato de 'base larga'. Essa base possui informações de pagamentos do cliente mês a mês a partir do mês de aquisição do crédito (mês 0) até o vigésimo quarto mês após a aquisição do crédito (mês 24). Utilizaremos essa base para determinar se um proponente é considerado 'bom pagador' ou caso apresente atraso representativo, será considerado 'mau pagador'.
# 
# #### Base larga vs base longa
# A base ser larga significa que há uma linha para cada cliente, e que as informações estarão nas colunas, em contraste com a 'base longa', em que haveria uma linha para cada combinação cliente/mês, uma coluna indicando o cliente, outra indicando o mês, e apenas uma coluna com a informação do atraso.
# 
# #### Tarefa 1) Marcar *default* no mês
# Faça uma indicadora de se o cliente está em *default* em cada uma das marcações (mes_00 a mes_24). Dica: você pode utilizar o método ```.isin()``` do Pandas. Consulte a [documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html) caso necessário.
# 
# #### Tarefa 2) 'bons' e 'maus' ao longo de todos os 24 meses de desempenho
# Marque para cada cliente se ele teve pelo menos um episódio de *default* entre o mês 0 e o mês 24. Dica: o método ```sum()``` pode ajudar. Caso precise, consulte a [documentação](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html) e procure pelo argumento ```axis```, você viu outros métodos que possuem esse argumento também. Tendo o número de meses em default de cada cliente, basta marcar ```True``` para todos aqueles que possuem pelo menos 1 mês em *default* e ```False``` para os demais.
# 
# #### Tarefa 3) Marcando proponentes expostos ao risco de crédito
# Marcando proponentes que se tornaram tomadores: lembre-se de que clientes que não adquiriram o cartão devem ser desconsiderados. A base de pagamentos possui apenas clientes que adquiriram cartão de crédito, então você pode selecionar somente os clientes da base de propostas que se encontram na base de pagamentos.
# 
# #### Tarefa 4) Consolidando as informações
# Faça uma junção das informações da base de propostas com a variável de *default* que você acabou de construir. Talvez você consiga realizar a tarefa 3 e tarefa 4 em uma única linha de código ;)
# 
# #### Tarefa 5) Verificando
# Faça uma contagem dos valores do *default* que você construiu. 

# In[37]:


import pandas as pd


# In[38]:


import pandas as pd

# Ler o arquivo CSV 'pagamentos_largo.csv'
pg = pd.read_csv('pagamentos_largo.csv')

print("\nPrimeiras linhas do arquivo 'pagamentos_largo.csv':")
print(pg.head())


# In[39]:


pg.head()


# In[40]:


import pandas as pd

# Ler o arquivo CSV
propostas = pd.read_csv('application_record.csv')

# Verificar as primeiras linhas do DataFrame
print(propostas.head())


# In[41]:


pg.head()


# In[42]:


# 1) Seu código aqui
import pandas as pd

# Ler o arquivo CSV 'pagamentos_largo.csv'
pg = pd.read_csv('pagamentos_largo.csv')

# Selecionar apenas as colunas referentes aos meses de 'mes_00' a 'mes_24'
mes_columns = [f'mes_{i:02d}' for i in range(10, 25)]

# Criar a coluna 'Default' no DataFrame 'pg' marcando se o cliente está em default em cada um dos meses
pg['Default'] = pg[mes_columns].isin(['C']).any(axis=1)



# Exibir as primeiras linhas do DataFrame 'pg' com a coluna 'Default' adicionada
print(pg.head())


# In[43]:


# 2) Seu código aqui
import pandas as pd

# Ler o arquivo CSV 'pagamentos_largo.csv'
pg = pd.read_csv('pagamentos_largo.csv')

# Selecionar apenas as colunas referentes aos meses presentes nos dados
mes_columns = pg.columns[1:-1]  # Excluir a coluna 'ID' e 'Default'

# Verificar se o cliente teve pelo menos um episódio de default entre o mês 0 e o mês 24
pg['Default'] = pg[mes_columns].isin(['C']).any(axis=1)

# Marcar os clientes como 'bons' ou 'maus' com base na presença de default
pg['Status'] = pg['Default'].apply(lambda x: 'maus' if x else 'bons')

# Exibir as primeiras linhas do DataFrame 'pg' com as colunas 'Default' e 'Status' adicionadas
print(pg.head())




# In[44]:


# 3) Seu código aqui
import pandas as pd

# Ler o arquivo CSV 'application_record.csv'
propostas = pd.read_csv('application_record.csv')

# Ler o arquivo CSV 'pagamentos_largo.csv'
pg = pd.read_csv('pagamentos_largo.csv')

# Filtrar os clientes da base de propostas que estão presentes na base de pagamentos
propostas_tomadores = propostas[propostas['ID'].isin(pg['ID'])]

# Exibir as primeiras linhas do DataFrame 'propostas_tomadores'
print(propostas_tomadores.head())



# In[45]:


# 4) eu código aqui
# Tarefa 3) Marcando proponentes expostos ao risco de crédito
# Filtrar os clientes da base de propostas que estão na base de pagamentos
propostas_risco = propostas[propostas['ID'].isin(pg['ID'])]

# Tarefa 2) 'bons' e 'maus' ao longo de todos os 24 meses de desempenho
# Verificar se cada cliente teve pelo menos um episódio de default entre o mês 0 e o mês 24
default_indicator = pg.iloc[:, 1:25].isin(['C']).any(axis=1)

# Criar a variável defaults contendo a informação de default para cada cliente
defaults = pd.DataFrame({'ID': pg['ID'], 'Default': default_indicator})

# Tarefa 4) Consolidando as informações
# Fazer a junção das informações da base de propostas com a variável de default
propostas_default = propostas_risco.merge(defaults[['ID', 'Default']], on='ID', how='left')

# Exibir o resultado
print(propostas_default)



# In[36]:


# Contagem dos valores do Default
contagem_default = propostas_default['Default'].value_counts()

# Exibindo a contagem
print(contagem_default)

