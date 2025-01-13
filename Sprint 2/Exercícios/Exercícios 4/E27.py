def ler_csv(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filepath}' não encontrado.")
        return None, None

    cabecalho = linhas[0].strip().split(',')
    dados = []

    for linha in linhas[1:]:
        valores = []
        acumulador = ''
        dentro_aspas = False

        for char in linha:
            if char == '"' and not dentro_aspas:
                dentro_aspas = True
            elif char == '"' and dentro_aspas:
                dentro_aspas = False
            elif char == ',' and not dentro_aspas:
                valores.append(acumulador.strip())
                acumulador = ''
            else:
                acumulador += char

        valores.append(acumulador.strip())  
        dados.append(valores)

    return cabecalho, dados


def etapa1(dados, cabecalho):
    index_actor = cabecalho.index('Actor')
    index_number_movies = cabecalho.index('Number of Movies')

    maior = 0
    top = ''

    for linha in dados:
        try:
            numero_filmes = int(float(linha[index_number_movies].strip()))
            if numero_filmes > maior:
                maior = numero_filmes
                top = linha[index_actor].strip().replace('"', '')
        except ValueError:
            continue

    with open('etapa-1.txt', 'w', encoding='utf-8') as arquivo:
        print(f"O ator que mais possui filmes no dataset é {top} com {maior} filmes.",file=arquivo)


def etapa2(dados, cabecalho):
    index_gross = cabecalho.index('Gross')
    valores = []

    for linha in dados:
        try:
            gross = float(linha[index_gross].strip().replace(',', ''))
            valores.append(gross)
        except ValueError:
            continue

    media = sum(valores) / len(valores) if valores else 0
    with open('etapa-2.txt', 'w', encoding='utf-8') as arquivo:
        print(f"A média de receita bruta dos principais filmes é: {media:.2f}",file=arquivo)


def etapa3(dados, cabecalho):
    index_actor = cabecalho.index('Actor')
    index_avg_per_movie = cabecalho.index('Average per Movie')

    maior = 0
    top = ''

    for linha in dados:
        try:
            media_receita = float(linha[index_avg_per_movie].strip().replace(',', ''))
            if media_receita > maior:
                maior = media_receita
                top = linha[index_actor].strip().replace('"', '')
        except ValueError:
            continue
    with open('etapa-3.txt', 'w', encoding='utf-8') as arquivo:        
        print(f"O ator com a maior média de receita por filme é {top} com {maior:.2f} milhões.",file=arquivo)


def etapa4(dados, cabecalho):
   
    index_movie = cabecalho.index('#1 Movie')
    contagem_filmes = {}

    for linha in dados:
        filme = linha[index_movie].strip().replace('"', '')
        if filme in contagem_filmes:
            contagem_filmes[filme] += 1
        else:
            contagem_filmes[filme] = 1

    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))
    with open('etapa-4.txt', 'w', encoding='utf-8') as arquivo:
        print("Filmes ordenados pela quantidade de aparições:",file=arquivo)
        for filme, contagem in filmes_ordenados:
            print(f"{filme}: {contagem} aparições",file=arquivo)


def etapa5(dados, cabecalho):
    """Lista os atores ordenados pela receita bruta de bilheteria."""
    index_actor = cabecalho.index('Actor')
    index_total_gross = cabecalho.index('Total Gross')
    receita_atores = {}

    for linha in dados:
        ator = linha[index_actor].strip().replace('"', '')
        try:
            receita = float(linha[index_total_gross].strip().replace(',', ''))
            if ator in receita_atores:
                receita_atores[ator] += receita
            else:
                receita_atores[ator] = receita
        except ValueError:
            continue

    atores_ordenados = sorted(receita_atores.items(), key=lambda x: -x[1])
    with open('etapa-5.txt', 'w', encoding='utf-8') as arquivo:
        print("Atores ordenados pela receita bruta de bilheteria:",file=arquivo)
        for ator, receita in atores_ordenados:
            print(f"{ator}: {receita:.2f} milhões",file=arquivo)


if __name__ == "__main__":
    cabecalho, dados = ler_csv('actors.csv')
    
    if cabecalho and dados:
        etapa1(dados, cabecalho)
        etapa2(dados, cabecalho)
        etapa3(dados, cabecalho)
        etapa4(dados, cabecalho)
        etapa5(dados, cabecalho)
