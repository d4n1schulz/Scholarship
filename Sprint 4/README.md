# Resumo

**AWS Partner: Sales Accreditation (Business)**  Aprendi a articular a proposta de valor da AWS, focando em benefícios como economia de custos, produtividade e agilidade. Também aprendi a responder objeções comuns dos clientes e a vender em parceria com a AWS, utilizando práticas recomendadas.

**AWS Partner: Economias na nuvem AWS**: No curso "Aspectos Econômicos na Nuvem", aprendi sobre os pilares do AWS Cloud Value Framework, focando na redução de custos, aumento de produtividade e agilidade empresarial com a AWS. O curso também abordou práticas de otimização de custos, sustentabilidade e gerenciamento financeiro, além de como usar a Avaliação do Portfólio de Migração (MPA).

**AWS Skill Builder - AWS Cloud Quest**: No game interativo da AWS, aprendi a implementar soluções práticas, como hospedar páginas estáticas com Amazon S3, aumentar a escalabilidade de instâncias EC2, configurar redes VPC, otimizar bancos de dados com Amazon RDS e DynamoDB, e usar Amazon EFS para armazenamento. O jogo também abordou segurança com AWS IAM, arquiteturas de alta disponibilidade e o uso do AWS Pricing Calculator para estimativas de custo. 

# Exercícios

## Exercício 1

1. ...
[Arquivos e Pastas](../Sprint%204/Exercícios/E01/Arquivos%20e%20Pastas/)

2. ...
[Evidências](../Sprint%204/Exercícios/E01/Evidências/)


## Exercício 2

1. ...
[Arquivos e Pastas](../Sprint%204/Exercícios/E02/Arquivos/)

2. ...
[Evidências](../Sprint%204/Exercícios/E02/Evidências/)


## Exercício 3

1. ...
[Arquivos e Pastas](../Sprint%204/Exercícios/E03/Arquivos%20e%20Pastas/)

2. ...
[Evidências](../Sprint%204/Exercícios/E03/Evidências/)



# Evidências

### Exercício 1:

Procurei pelo serviço S3 e cliquei em "Criar Bucket"

![criando_bucket](../Sprint%204/Exercícios/E01/Evidências/criando_bucket.png)

Configurando Bucket

![configurando_bucket](../Sprint%204/Exercícios/E01/Evidências/diretório_e_nome.png)

Criando Bucket

![salvando_bucket](../Sprint%204/Exercícios/E01/Evidências/criei_bucket.png)

Habilitando hospedagem de site estático

![hospedar_site](../Sprint%204/Exercícios/E01/Evidências/editar_hospedagem_site.png)

Configurando hospedagem de site estático

![config_hospedagem](../Sprint%204/Exercícios/E01/Evidências/configurando_hospedagem.png)

Copiando endpoint em "Hospedagem de sites estáticos"

![endpoint_copiado](../Sprint%204/Exercícios/E01/Evidências/endpoint_copiado.png)

Colei o endpoint no navegador e o acesso ficou negado

![endpoint_erro](../Sprint%204/Exercícios/E01/Evidências/rodando_endpoint_erro.png)

Em "Permissões" no S3, no "Bloqueio de acesso público
(configurações de bucket)", escolhi "Editar"

![editar_bloqueio_publico](../Sprint%204/Exercícios/E01/Evidências/editar_bloqueio_publico.png)

Desmarquei "Bloquear todo acesso público" e cliquei em "Salvar alterações"

![desat_bloqueio_publico](../Sprint%204/Exercícios/E01/Evidências/desativar_bloqueio_publico.png)

Em "Permissões" fui em "Política de bucket" e escolhi "Editar" e para conceder acesso público de leitura ao site, copiei a política de bucket na questão da Udemy e colei-a no Bucket "Editor de política de bucket"

![desat_bloqueio_publico](../Sprint%204/Exercícios/E01/Evidências/editando_politica.png)

Criando o documento "index.html"

![criando_index.html](../Sprint%204/Exercícios/E01/Evidências/criando_doc_índice.png)

Fazendo upload do arquivo "index.html" no bucket

![upload_index](../Sprint%204/Exercícios/E01/Evidências/índice_upload.png)

Criei a pasta "Dados" com o arquivo CSV baixado no pb

![pasta_dados_com_csv](../Sprint%204/Exercícios/E01/Evidências/pasta_dados_com_CSV.png)

Upload da pasta "Dados"

![upload_pasta_Dados](../Sprint%204/Exercícios/E01/Evidências/upload_pasta.png)

Criação do documento de erro

![criação_doc_erro](../Sprint%204/Exercícios/E01/Evidências/doc_erro.png)

Upload do documento de erro

![upload_doc_erro](../Sprint%204/Exercícios/E01/Evidências/upload_doc_erros.png)


Em "Propriedades" e na parte inferior da página, em "Hospedagem estática de sites", Cliquei no "Endpoint de site do Bucket". Meu documento de índice é aberto em uma janela separada do navegador e agora aparece o conteúdo do arquivo

![doc_erro_teste](../Sprint%204/Exercícios/E01/Evidências/teste_final.jpeg)


### Exercício 2:

Criando uma pasta "queries" no bucket criado no exercício anterior, o AWS Athena usará para armazenar as consultas executadas

![pasta_queries](../Sprint%204/Exercícios/E02/Evidências/pasta_queries.png)


Acessando o Athena

![athena](../Sprint%204/Exercícios/E02/Evidências/editor_athena.png)

Indo em "Gerenciar configurações" na "Localização dos resultados da Consulta" inseri o caminho para o bucket criado no Amazon S3 para resultados de consultas

![local_resultado](../Sprint%204/Exercícios/E02/Evidências/local_resultados.png)

Usando o editor de consultas do Athena para criar um banco de dados denominado "meubanco"

![criando_database](../Sprint%204/Exercícios/E02/Evidências/database_criando.png)

Na lista "Banco de dados" à esquerda, escolhi "meubanco" para torná-lo meu banco de dados atual

![banco_atual](../Sprint%204/Exercícios/E02/Evidências/database_atual.png)

Elaborando a query para criar a tabela no banco de dados que eu criei

![criando_tabela](../Sprint%204/Exercícios/E02/Evidências/criando_tabela.png)

Testando os dados com a consulta colocada no pb

![testando_dados](../Sprint%204/Exercícios/E02/Evidências/testando_consulta.png)

Uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje

![consulta_final](../Sprint%204/Exercícios/E02/Evidências/consulta_final.png)

Execução da consulta

![consulta_final_exe](../Sprint%204/Exercícios/E02/Evidências/execução_consulta_final.png)

Arquivos na pasta "queries" dentro do bucket

![arq_dentro_do_bucket](../Sprint%204/Exercícios/E02/Evidências/resultados_consultas.png)

### Exercício 3:

Criando a função no Lambda

![criando_func_lambda](../Sprint%204/Exercícios/E03/Evidências/criando_função.png)


Criando teste

![criando_teste](../Sprint%204/Exercícios/E03/Evidências/criando_teste.png)


Erro ao executar a função

![erro_teste](../Sprint%204/Exercícios/E03/Evidências/tela_erro.png)

Código para acessar o S3 

![acessa_s3](../Sprint%204/Exercícios/E03/Evidências/acessa_S3.png)

Para fazer a camada da função, será usado o Dockerfile para carregar as aplicações necessárias. Criando Dockerfile:

![criando_dockerfile](../Sprint%204/Exercícios/E03/Evidências/dockerfile_codigo.png)

Construindo imagem

![construindo_imagem](../Sprint%204/Exercícios/E03/Evidências/construindo_imagem.png)

Rodando imagem

![rodando_imagem](../Sprint%204/Exercícios/E03/Evidências/rodando_imagem.png)

Criando a pasta que será utilizada para armazenar as bibliotecas necessárias para a layer que será criada

![preparando_pasta_layer](../Sprint%204/Exercícios/E03/Evidências/preparando_diretórios_container.png)

Instalando Pandas

![instalando_pandas](../Sprint%204/Exercícios/E03/Evidências/instalando_pandas.png)

Compactando todos os arquivos do diretório "python" em um arquivo chamado "minha-camada-pandas.zip"

![compactando_app](../Sprint%204/Exercícios/E03/Evidências/transformando_python_em_zip.png)

Descobrindo o ID do Container para copiar o arquivo para a máquina local

![descobrindo_id_container](../Sprint%204/Exercícios/E03/Evidências/descobrindo_id_container.png)

Copiando o arquivo para a máquina local

![copiando_arquivo](../Sprint%204/Exercícios/E03/Evidências/copiando_arquivo.png)

Fazendo upload do arquivo zip

![upload_do_zip](../Sprint%204/Exercícios/E03/Evidências/upload_do_zip.png)

Upload realizado

![upload_feito](../Sprint%204/Exercícios/E03/Evidências/upload_feito.png)

Criando a camada

![criando_camada](../Sprint%204/Exercícios/E03/Evidências/criando_camada.png)

Camada criada

![camada_criada](../Sprint%204/Exercícios/E03/Evidências/camada_criada.png)

Adicionando uma camada para a função

![adicionando_camada_p_func](../Sprint%204/Exercícios/E03/Evidências/add_camada_para_função.png)


Configurando camada

![confi_camada](../Sprint%204/Exercícios/E03/Evidências/configurando_camada.png)


Camada adicionada

![camada_adicionada](../Sprint%204/Exercícios/E03/Evidências/camada_adicionada.png)

Configuração para o teste ser realizado corretamente

![confif_teste](../Sprint%204/Exercícios/E03/Evidências/configuração_para_teste_funcionar.png)

Teste realizado com sucesso

![teste_final](../Sprint%204/Exercícios/E03/Evidências/teste_final.png)

# Certificados

![certificado_aspec_econ_nuv](../Sprint%204/Certificados/Aspectos_econômicos_da_nuvem.png)

![certificado_sales_acred](../Sprint%204/Certificados/Sales_Accreditation(Business).png)

![certificado_cloud_quest](../Sprint%204/Certificados/Cloud_Quest.png)
