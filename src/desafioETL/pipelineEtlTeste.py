# Importa a biblioteca Pandas
# Uma ferramenta para manipulação e análise de dados
# Renomea para pd para facilitar o uso no código. 
import pandas as pd

arquivo = r"src/desafioETL/dataSource/PipelineEtl_Jr2026.csv"  
arquivo_teste = pd.read_csv(arquivo, sep=';', encoding='utf-8')  # Lê o arquivo CSV com separador ponto e vírgula e codificação UTF-8

# Teste de leitura do arquivo CSV
print("\nTeste de leitura do arquivo CSV:")
print(arquivo_teste.head())  # Exibe as primeiras linhas do DataFrame para ver

print("\nIds dos clientes extraídos do arquivo CSV:")
clientesIds = arquivo_teste['ClienteId'].tolist()   
print(clientesIds)  # Exibe a lista de IDs dos clientes

print("\nNomes dos clientes extraídos do arquivo CSV:")
clientesNomes = arquivo_teste['Nome'].tolist()  
print(clientesNomes)  # Exibe a lista de nomes dos clientes

print("\nConta dos clientes extraídos do arquivo CSV:")
clientesContas = arquivo_teste['Conta'].tolist()  
print(clientesContas)  # Exibe a lista de contas dos clientes

print("\nCartões dos clientes extraídos do arquivo CSV:")
clientesCartoes = arquivo_teste['Cartao'].tolist()  
print(clientesCartoes)  # Exibe a lista de cartões dos clientes
