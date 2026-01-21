# Pipeline ETL — Estudos em Ciência de Dados (Python)

Descrição
- Projeto de estudos para praticar conceitos e técnicas de ETL (Extract, Transform, Load) usando Python e ferramentas comuns do ecossistema de ciência de dados.
- Foco em: ingestão de dados, limpeza/transformação, testes, versionamento de dados e orquestração básica.

O que há de novo neste repositório
- Implementação de um exemplo simples de pipeline em `src/desafioETL/pipelineEtl.py` cobrindo as etapas:
  - Extract: leitura de arquivo CSV com `sep=';'` e normalização de colunas, diretório `src/desafioETL/dataSource/`.
  - Transform: adição de mensagens personalizadas (`news`) para cada cliente, com tratamento robusto para variações no nome das colunas.
  - Load: gravação do resultado em `src/desafioETL/dataTarget/` via função `load_to_csv`.

- Aprender e aplicar padrões de engenharia de dados e ETL.
- Construir pipelines reproducíveis e testáveis.
- Explorar integração com bancos de dados, formatos comuns (CSV, Parquet), e notebooks para exploração.

Descrição
- Projeto de estudos para praticar conceitos e técnicas de ETL (Extract, Transform, Load) usando Python e ferramentas comuns do ecossistema de ciência de dados.
- Foco em: ingestão de dados, limpeza/transformação, testes, versionamento de dados e orquestração básica.

Objetivos
- Aprender e aplicar padrões de engenharia de dados e ETL.
- Construir pipelines reproducíveis e testáveis.
- Explorar integração com bancos de dados, formatos comuns (CSV, Parquet), e notebooks para exploração.

Conteúdo sugerido
- Ingestão: leitura de arquivos locais, APIs simples e consultas a bases SQL.
- Transformação: limpeza com `pandas`, normalização, agregações, e validação de qualidade.
- Armazenamento: escrita em CSV/Parquet, e inserção em bancos via `sqlalchemy`.
- Orquestração/execução: scripts CLI simples (`click`/`argparse`) e/ou tarefas com `prefect`.
- Testes: unitários com `pytest` e validação de dados.

Estrutura de pastas (sugestão)
```
src/
├─ data/           # amostras de dados (não commitar dados sensíveis)
├─ notebooks/      # exploração e análises interativas
├─ src/            # código do projeto (etl, utils, db)
│  ├─ etl.py
│  ├─ extract.py
│  ├─ transform.py
│  └─ load.py
├─ tests/          # testes unitários
├─ configs/        # arquivos de configuração (yaml/json)
└─ README.md       # este arquivo
```

Requisitos (exemplo)
- Python 3.9+ (recomendado)
- Bibliotecas comuns:
  - `pandas`, `numpy`, `pyyaml`, `sqlalchemy`, `requests`, `prefect` (opcional), `click`, `jupyterlab`, `pytest`, `black`

Instalação e setup (Windows PowerShell)
```powershell
# criar e ativar ambiente virtual
python -m venv .venv
.venv\Scripts\Activate.ps1

# atualizar pip e instalar dependências (se existir requirements.txt)
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# atualizar ferramentas básicas
python -m pip install --upgrade pip setuptools wheel

# deve imprimir a versão do pandas sem erro
python -c "import pandas as pd; print(pd.__version__)"

# instalar pandas no mesmo interpretador
python -m pip install pandas

# rodar Jupyter Lab (opcional)
jupyter lab
```

Execução (exemplos)
- Executar um script ETL simples (se existir `src/etl.py`):
```powershell
python src/etl.py
# ou, se o projeto for instalado como pacote local (ex.: usando pyproject/poetry):
python -m src.etl
```
- Executar um pipeline com `prefect` (exemplo genérico):
```powershell
prefect deployment run my-etl/deployment-name
```

Boas práticas
- Separar responsabilidades: `extract`, `transform`, `load` em módulos distintos.
- Manter dados sensíveis fora do repositório (usar `.gitignore` e variáveis de ambiente).
- Adicionar testes para transformações críticas e validações de esquema.
- Documentar decisões e suposições nos notebooks ou no `README`.

Como contribuir / estudar com este repositório
- Crie uma branch para a sua feature/experimento: `git checkout -b feat/nome-experimento`.
- Adicione testes para as transformações que você implementar.
- Abra PR com descrição do objetivo e resultados esperados.

Referências úteis
- Pandas documentation: https://pandas.pydata.org/
- SQLAlchemy: https://www.sqlalchemy.org/
- Prefect (orquestração): https://www.prefect.io/

Contato
- Projeto pessoal de estudos. Para dúvidas ou sugestões, abra uma issue ou PR.

Licença
- Use a licença que preferir (ex.: MIT) — caso não queira especificar, adicione arquivo `LICENSE`.
