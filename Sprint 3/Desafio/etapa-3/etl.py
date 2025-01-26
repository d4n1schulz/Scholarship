# importar pandas
import pandas as pd

# Ler arquivo csv
df = pd.read_csv('concert_tours_by_women.csv')

# Tirando as colunas que não é para aparecer no resultado final
df = df.drop(labels=["Peak", "All Time Peak", "Ref."], axis=1)

# Aqui tentei transformar a coluna Year(s) em Start Year e em End Year(s), mas
# não tive sucesso

# df[['Start Year', 'End Year']] = df['Year(s)'].str.split('–', expand = True)

# Ao executar o código acima, percebi que deu erro pois tinha dados na coluna
# Year(s) que não seguiam o padrão de ter um "ano inicial - ano final",então
# as linhas que tem apenas um ano, eu deixo esse ano como inicial e final

df['Year(s)'] = df['Year(s)'].str.replace('-', '–', regex=False)

df['Year(s)'] = df['Year(s)'].apply(lambda x: f"{x}–{x}" if '–' not in str(x) else x)

df[['Start Year', 'End Year']] = df['Year(s)'].str.split('–', expand=True)

# Como agora não preciso mais da coluna Year(s), vou deletar essa coluna

df = df.drop('Year(s)', axis=1)

# Como percebi olhando o dataframe que a coluna Actual gross e Average gross
# tinham caracteres como "$" e "," e além desses "[ a ]" e "[ b ]"
# que atrapalhariam a análise, acabei tirando-os e transformei essas colunas
# em float.

df.loc[df['Actual gross'] == '$229,100,000[b]', 'Actual gross'] = '$229,100,000'
df.loc[df['Actual gross'] == '$167,700,000[e]', 'Actual gross'] = '$167,700,000'

df['Actual gross'] = df['Actual gross'].replace({'\\$': '', ',': ''}, regex=True).astype(float)
df['Adjusted gross (in 2022 dollars)'] = df['Adjusted gross (in 2022 dollars)'].replace({'\\$': '', ',': ''}, regex=True).astype(float)
df['Average gross'] = df['Average gross'].replace({'\\$': '', ',': ''}, regex=True).astype(float)

# Depois de tratar as colunas que envolviam dinheiro, observei que teve
# alguns caracteres diferentes que estavam na coluna de Tour title, como eram
# poucas linhas acabei modificando diretamente na linha os caracteres
# diferentes

df.loc[df['Tour title'] == 'The Eras Tour †', 'Tour title'] = 'The Eras Tour'
df.loc[df['Tour title'] == 'Sticky & Sweet Tour ‡[4][a]', 'Tour title'] = 'Sticky & Sweet Tour'
df.loc[df['Tour title'] == 'Summer Carnival †', 'Tour title'] = 'Summer Carnival'
df.loc[df['Tour title'] == 'The Monster Ball Tour *', 'Tour title'] = 'The Monster Ball Tour'
df.loc[df['Tour title'] == 'Living Proof: The Farewell Tour ‡[21][a]', 'Tour title'] = 'Living Proof: The Farewell Tour'

# Exportando o dataframe para um arquivo CSV
df.to_csv('csv_limpo.csv', index=False)
