# Pipeline de Dados e Dashboard: Oficina Bobo Benz

Este projeto demonstra a construção de um pipeline completo de Engenharia e Análise de Dados, desde a extração de dados brutos até a criação de um dashboard executivo no Power BI. O objetivo é transformar dados desorganizados de uma oficina mecânica em insights de negócio acionáveis.

## Arquitetura do Projeto
O fluxo de dados foi construído da seguinte forma:
1. **Extração e Limpeza (Python/Pandas):** Leitura de um arquivo CSV bruto, tratamento de valores nulos (NaN), padronização de strings e conversão de tipos de dados.
2. **Modelagem Relacional (MySQL):** Criação de um banco de dados normalizado (1FN, 2FN, 3FN) com chaves primárias e estrangeiras para garantir a integridade dos dados.
3. **Carga de Dados (Python/MySQL Connector):** Inserção automatizada dos dados limpos nas tabelas relacionais.
4. **Visualização (Power BI):** Conexão direta ao banco MySQL para a criação de um dashboard interativo.

## Tecnologias Utilizadas
- **Python 3** (Pandas para ETL)
- **MySQL** (Banco de dados relacional)
- **Jupyter Notebook** (Ambiente de desenvolvimento e testes)
- **Power BI** (Visualização de dados)

## Modelagem de Dados
O banco de dados foi estruturado para evitar redundâncias e permitir a ligação correta entre entidades (N:N).
- **Clients:** Cadastro de clientes (PF e PJ).
- **Vehicle:** Veículos vinculados aos clientes.
- **Mechanic:** Cadastro de mecânicos e seus níveis de experiência.
- **Services:** Registro central de todas as ordens de serviço, custos e tempos.
- **Material:** Catálogo único de peças (extraído da coluna multivalorada do CSV).
- **ServicesMaterial:** Tabela associativa que resolve o relacionamento N:N entre Serviços e Peças.

![Modelo Relacional](\images\Modelo_relacional.png)

## Principais Desafios Superados
- **Limpeza de Dados:** Tratamento de strings inconsistentes (ex: "30k" em vez de 30000) e valores nulos que quebravam a inserção no banco.
- **Normalização N:N:** O CSV original continha as peças usadas em uma única célula de texto (ex: "Oil filter, Brake pads"). Foi necessário usar manipulação de strings no Pandas para explodir essas listas e criar registros únicos na tabela `Material`, relacionando-os via `ServicesMaterial`.

## Dashboard e Insights de Negócio
O dashboard foi desenhado para responder às principais perguntas do gestor da oficina:
- **Custo ao Longo do Tempo:** Sazonalidade dos serviços.
- **Top Mecânicos:** Quem gera mais receita.
- **Distribuição de Serviços:** Quais serviços são o "pão com manteiga" da loja.
- **Marcas mais presentes:** Quais serviços são o "pão com manteiga" da loja (Barras e Pizza).

![Dashboard Power BI](\images\Grafico_PowerBI.png)

## Como Executar o Projeto
1. Clone o repositório.
2. Execute o notebook `Clean_table.ipynb` para limpar os dados brutos.
3. Execute o notebook `Create_Table.ipynb` para criar a estrutura no MySQL.
4. Execute o notebook `Insert_Table.ipynb` para popular o banco de dados.
5. Abra o arquivo do Power BI e atualize a conexão com o seu banco local.