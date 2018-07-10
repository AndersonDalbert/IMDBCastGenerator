import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

atores = pd.read_csv('./relacaoatoresimdb250atoresFinal.csv')
atoresComOscar = atores[atores['TEMOSCAR'] == 1]

qtdAtores = len(atores.index)
qtdAtoresComOscar = len(atoresComOscar.index)

# plot do gráfico em pizza

labels = 'Com Oscar', 'Sem Oscar'
sizes = [qtdAtoresComOscar, qtdAtores]
colors = ['yellow', 'blue']
explode = (0.1, 0)

plt.title('Porcentagem de atores com Oscar entre o elenco dos 250 melhores filmes (Fonte: IMDB)')
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()

def qtdRelacoesDeTrabalho(df, dfIndex) :
   relacoesDeTrabalho = df.loc[dfIndex, 'JATRABALHOU']	
   return len(list( map(int, relacoesDeTrabalho.split(", ")) ))


def qtdAtoresComDeterminadoRangeDeRelacoesDeTrabalho(df, qtdMin, qtdMax) :
   qtd = 0	
   for i, row in df.iterrows():
      qtdRelacoes = qtdRelacoesDeTrabalho(df, i)
      if qtdRelacoes >= qtdMin and qtdRelacoes <= qtdMax:
         qtd += 1
      	
   return qtd

def qtdAtoresAcimaDeDeterminadaQtdDeRelacoesDeTrabalho(df, qtdMin) :
   qtd = 0	
   for i, row in df.iterrows():
      qtdRelacoes = qtdRelacoesDeTrabalho(df, i)
      if qtdRelacoes >= qtdMin :
         qtd += 1
      	
   return qtd

# plot do gráfico em barras de todos atores

entre_1_e_3 = qtdAtoresComDeterminadoRangeDeRelacoesDeTrabalho(atores, 1, 3)
entre_4_e_6 = qtdAtoresComDeterminadoRangeDeRelacoesDeTrabalho(atores, 4, 6)
mais_que_6 = qtdAtoresAcimaDeDeterminadaQtdDeRelacoesDeTrabalho(atores, 7)

objects = ('1 a 3', '4 a 6', 'Acima de 6')
y_pos = np.arange(len(objects))
performance = [entre_1_e_3, entre_4_e_6, mais_que_6]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)	
plt.ylabel('Quantidade de atores')
plt.xlabel('Número de relacionamentos (atuações em conjunto) com outros atores')
plt.title('Distribuição de atores por número de relacionamentos com outros atores')

plt.show()

# plot do gráfico em barras dos atores que ganharam oscar

entre_1_e_3 = qtdAtoresComDeterminadoRangeDeRelacoesDeTrabalho(atoresComOscar, 1, 3)
entre_4_e_6 = qtdAtoresComDeterminadoRangeDeRelacoesDeTrabalho(atoresComOscar, 4, 6)
mais_que_6 = qtdAtoresAcimaDeDeterminadaQtdDeRelacoesDeTrabalho(atoresComOscar, 7)

objects = ('1 a 3', '4 a 6', 'Acima de 6')
y_pos = np.arange(len(objects))
performance = [entre_1_e_3, entre_4_e_6, mais_que_6]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)	
plt.ylabel('Quantidade de atores')
plt.xlabel('Número de relacionamentos (atuações em conjunto) com outros atores')
plt.title('Distribuição de atores que ganharam Oscar por número de relacionamentos com outros atores ganhadores')

plt.show()
