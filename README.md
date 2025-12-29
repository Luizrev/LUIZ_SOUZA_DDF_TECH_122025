# Desafio Técnico - Dadosfera (Case Olist)

Este repositório contém a solução para o case técnico de Engenharia e Ciência de Dados, focado na otimização de e-commerce utilizando a base pública da Olist.

## 🛠 Arquitetura da Solução (Abstração)

Devido a restrições de acesso ao ambiente proprietário, a solução foi arquitetada utilizando uma stack Cloud-Native moderna e reprodutível:

- **Ingestão & Processamento:** Python (Pandas/DuckDB) via Notebooks.

- **Qualidade de Dados:** Great Expectations.
- **Inteligência Artificial:** OpenAI API (GPT) para análise de sentimento em reviews.
- **Visualização & Data App:** Streamlit.

## 📂 Estrutura do Projeto

- `/src`: Código fonte da aplicação Streamlit.
- `/notebooks`: Notebooks para análise exploratória (EDA), ETL e testes de IA.
- `/docs`: Documentação de planejamento (Kanban/Gantt) e evidências.
- `/data`: (Ignorado no Git) Local para armazenamento dos datasets brutos.

## 🚀 Como Executar

1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o app: `streamlit run src/app.py`