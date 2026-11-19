# Portfólio de Engenharia e Análise de Dados

Bem-vindo ao meu repositório central de projetos de Dados. Aqui documento soluções completas (End-to-End) envolvendo extração, tratamento (ETL), modelagem relacional, automação e visualização de dados para tomada de decisão.

## Stack Tecnológica

* **Linguagens:** Python (Pandas, Requests), SQL (DDL, DML, DQL)
* **Bancos de Dados:** MySQL, PostgreSQL, MariaDB
* **Orquestração & Infraestrutura:** Apache Airflow, Docker, Linux (Termux), Cloudflare Tunnels, Tailscale
* **Modelagem & Fundamentos:** Diagrama ER, Modelo Lógico, Normalização (1FN, 2FN, 3FN), Álgebra Relacional
* **Visualização & BI:** Power BI, Metabase
* **Ferramentas:** Jupyter Notebook, Git/GitHub

---

## Projetos em Destaque

### [Homelab Data Pipeline: Clima RJ](./homelab-clima-rj)
Pipeline de dados de ponta a ponta orquestrado com Apache Airflow (Docker) e hospedado em um servidor caseiro de baixo custo (tablet Android com Termux).
* **Destaques técnicos:** Automação diária de ETL (extração via API Open-Meteo, transformação com Pandas e carga no MariaDB); infraestrutura resiliente com `termux-services`; conexão segura via VPN Tailscale; script watchdog em Python para monitoramento de túneis Cloudflare e notificações via e-mail; visualização de dados no Metabase.
* **Tecnologias:** `Apache Airflow` `Python` `MariaDB` `Metabase` `Docker` `Termux`

---

### [Pipeline ETL e Dashboard Executivo: Oficina Bobo Benz](./oficina-bobo-benz-etl)
Pipeline completo (End-to-End) que transforma registros brutos e desnormalizados de uma oficina mecânica em um banco de dados relacional estruturado, alimentando um dashboard executivo.
* **Destaques técnicos:** Limpeza de strings inconsistentes com Pandas, normalização de relacionamentos N:N (tabela associativa para catálogo de peças), carga automatizada via Python e conexão direta para BI.
* **Tecnologias:** `Python (Pandas)` `MySQL` `Jupyter` `Power BI`

---

### [Modelagem e Banco de Dados Relacional: Pizzaria Barriguda](./pizzaria-barriguda-db)
Projeto de engenharia de banco de dados focado na modelagem, normalização e implementação de um sistema robusto para substituir controles manuais na operação de uma pizzaria.
* **Destaques técnicos:** Modelagem ER e Lógica com herança (superclasse/especializações), normalização validada até a 3FN, restrições avançadas de integridade (`CHECK`, `ENUM`, `ON DELETE CASCADE`) e consultas analíticas baseadas em Álgebra Relacional.
* **Tecnologias:** `PostgreSQL` `SQL` `Modelagem ER`