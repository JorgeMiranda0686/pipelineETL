# Importa a biblioteca Pandas
# Uma ferramenta para manipulação e análise de dados
# Renomea para pd para facilitar o uso no código. 
import pandas as pd

# Etapa de Extração (Extract): Leitura do arquivo CSV
print("Iniciando a etapa de Extração (Extract): Leitura do arquivo CSV")

# Leitura do arquivo CSV, dentro da pasta dataSource e conversão para uma lista de dicionários
# Diretório: src/desafioETL/dataSource
# Arquivo: PipelineEtl_Jr2026.csv
# Variável (clientes): variável que armazena uma lista de dicionários contendo os dados extraídos do arquivo CSV
# Método read_csv: função do Pandas para ler arquivos CSV e convertê-los em DataFrames
# Método to_dict(orient='records'): converte o DataFrame em uma lista de dicionários, onde cada dicionário representa uma linha do DataFrame
# orient='records': define o formato da saída como uma lista de dicionários, onde cada dicionário representa uma linha (ou "registro") do arquivo original

print("\nCarregando o arquivo CSV e convertendo para lista de dicionários:")
# Carrega o arquivo CSV e o transforma em um DataFrame (uma tabela de dados do Pandas)
clientes = pd.read_csv('src/desafioETL/dataSource/PipelineEtl_Jr2026.csv', sep=';', encoding='utf-8').to_dict(orient='records')
print(clientes)  # Exibe a lista de dicionários contendo os dados dos clientes

print("\nNúmero total de clientes carregados:", len(clientes))  # Exibe o número total de clientes carregados

print("\nEtapa de Extração (Extract) concluída com sucesso!")

print("\nIniciando a etapa de Transformação (Transform): Adicionando informações aos clientes:")
# O código percorre a lista de clientes um por um. Cada cliente é um dicionário que contém os dados vindos do seu CSV

for cliente in clientes:
    cliente['news'] = [] # Para cada cliente, ele cria uma nova chave chamada 'news', pronta para receber dados, e atribui a ela uma lista vazia, onde serão armazenadas 'notícias' relacionadas a esse cliente
    
    # Criando uma mensagem personalizada usando os dados do CSV
    nome_cliente = cliente['Nome']
    conta_cliente = cliente['Conta']
    mensagem = f"Olá {nome_cliente}, em 2026 sua conta {conta_cliente} foi atualizada e preparamos investimentos exclusivos para você!"
    # Adicionando a mensagem à estrutura do cliente
    cliente['news'].append({
        "description": mensagem
    })

    # Cliente atualizado com a nova informação
    print(cliente)
    print("----------------------------------------------------------------\n")  # Separador para melhor visualização entre clientes

print("Etapa de Transformação (Transform) concluída com sucesso!")

print("\nIniciando a etapa de Carga (Load): gravando em um arquivo de saída:")

# Converte a lista de dicionários modificada de volta para um DataFrame
clientesAlterados = pd.DataFrame(clientes)


# Exporta para um novo arquivo CSV
# index=False evita que o Pandas crie uma coluna extra de números à esquerda
clientesAlterados.to_csv('src/desafioETL/dataTarget/PipelineEtl_Alterado_Jr2026.csv', index=False)

print("Etapa de Carga (Load) concluída com sucesso!")
