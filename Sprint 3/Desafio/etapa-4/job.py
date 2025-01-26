import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv_limpo.csv')

# Questões

# Q1 - Qual é a artista que mais aparece nessa lista e possui a
# maior média de seu faturamento bruto (Actual gross)?

media = df.groupby('Artist')['Actual gross'].mean()

cont = df['Artist'].value_counts()

cont_max = cont.idxmax()
gross_max = media.idxmax()

with open("respostas.txt", "a") as arquivo:
    arquivo.write("Q1:\n")
    if gross_max == cont_max:
        arquivo.write(f"--- A artista que aparece mais vezes e tem a maior media de faturamento: {gross_max}\n\n")
    else:
        arquivo.write(f"--- As artistas diferem:\n"
                      f"--- Artista com maior média de faturamento: {gross_max}\n"
                      f"--- Artista que aparece mais vezes: {cont_max}\n\n")


# Q2 - Das turnês que aconteceram em um ano, apresente a turnê com a
# maior média de faturamento bruto (Average gross).

um_ano = df[df['Start Year'] == df['End Year']]

avg_gross = um_ano[['Tour title', 'Average gross']].sort_values('Average gross', ascending=False).head(1)

with open("respostas.txt", "a") as arquivo:
    arquivo.write("Q2:\n")
    arquivo.write(f"--- Das tours que aconteceram em um ano, a tour com a maior media de faturamento bruto: {avg_gross['Tour title'].values[0]}\n\n")

# Q3 - Quais são as 3 artistas que mais lucraram com menos número de shows?
# Cite também o nome da turnê de cada artista. Utilize a coluna "Adjusted
# gross (in 2022 dollars)".

df_aux = df[['Artist', 'Adjusted gross (in 2022 dollars)', 'Shows', 'Tour title']]
df_aux['Lucro_por_show'] = df_aux['Adjusted gross (in 2022 dollars)'] / df_aux['Shows']

maiores_lucros = df_aux.loc[df_aux.groupby("Artist")["Lucro_por_show"].idxmax()][['Lucro_por_show', 'Artist', 'Tour title']]

# Encontrei a turnê com o menor número de shows para cada artista
menor_shows = df.loc[df.groupby("Artist")["Shows"].idxmin()][['Artist', 'Tour title', 'Shows']]

resultado = pd.merge(menor_shows, maiores_lucros, on=["Artist", "Tour title"])

# Mostrei as turnês que atendem aos dois critérios
resultado_final = resultado.sort_values("Lucro_por_show", ascending=False).head(3)[['Artist', 'Tour title']]

with open("respostas.txt", "a") as arquivo:
    arquivo.write("Q3:\n")
    arquivo.write('--- As 3 artistas que mais lucraram com menos quantidade de shows:\n')
    for index, i in resultado_final.iterrows():
        arquivo.write(f"--- Artista: {i['Artist']}, Tour: {i['Tour title']}\n")
    arquivo.write("\n")


# Q4 - Para a artista que mais aparece nessa lista e que tenha o maior
# somatório de faturamento bruto, crie um gráfico de linhas que mostra o
# faturamento por ano da turnê (use a coluna Start Year).

# Descobri qual artista aparece mais vezes
frequente = df['Artist'].value_counts().idxmax()

# Descobri qual artista tem o maior faturamento total
faturamento_total = df.groupby('Artist')['Actual gross'].sum()
maior_faturamento = faturamento_total.idxmax()

import matplotlib.ticker as ticker
# Utilizei a biblioteca Matplotlib.ticker para criar o gráfico e formatar o
# eixo y para exibir valores sem notação científica.

# Atribuindo a df_artist as informações da artista
df_artist = df[df['Artist'] == frequente]

plt.figure(figsize=(10, 6))
plt.plot(df_artist['Tour title'], df_artist['Actual gross'])
plt.xlabel('Título da Turnê')
plt.ylabel('Faturamento (dólares)')
plt.title(f'Faturamento por Turnê - {frequente}')
plt.xticks(rotation=45)
plt.grid(True)

# Desativando a notação científica no eixo y
plt.gca().yaxis.set_major_formatter(ticker.ScalarFormatter(useOffset=False))
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))

# Salvando o gráfico como imagem PNG
plt.savefig('Q4.png')

plt.show()

# Q5 - Faça um gráfico de colunas demonstrando as 5 artistas com mais shows na lista.

# Agrupei por artista e somei o número de shows
artist_shows = df.groupby('Artist')['Shows'].sum()

top5 = artist_shows.sort_values(ascending=False).head(5)

# Criei o gráfico de colunas
plt.figure(figsize=(10, 6))
top5.plot(kind='bar', color='skyblue')
plt.xlabel('Artista')
plt.ylabel('Número de Shows')
plt.title('Top 5 Artistas com Mais Shows')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Salvando o gráfico como imagem PNG
plt.savefig('Q5.png')

plt.show()
