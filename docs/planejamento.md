# Planejamento do Projeto

## Metodologia

Este projeto segue uma abordagem Ágil, com entregas iterativas focadas em: Engenharia, Qualidade, Enriquecimento com IA e Visualização.

## Kanban Board

### 📋 To Do (A Fazer)

- [ ] Desenvolver App Streamlit
- [ ] Gravar vídeo de apresentação
- [ ] Escrever documentação final

### 🚧 Doing (Em Progresso)

- [x] Implementar Validação de Dados (Great Expectations)

### ✅ Done (Feito)

- [x] Leitura e Interpretação do Case Técnico
- [x] Criar Pipeline de Ingestão de Dados (ETL)
- [x] Configuração do Ambiente e Repositório
- [x] Definição da Arquitetura (Colab + Streamlit)
- [x] Download e Análise Inicial da Base Olist

```mermaid
gantt
    title Cronograma Macro do Projeto
    dateFormat  YYYY-MM-DD
    section Setup
    Configuração Git          :done,    des1, 2025-12-29, 1d
    Coleta de Dados (Olist)   :done,    des2, 2025-12-29, 1d
    section Engenharia
    Limpeza e Qualidade       :done,  des3, after des2, 2d
    Enriquecimento (GenAI)    :active,des4, after des3, 1d
    section Entrega
    Dashboard (Streamlit)     :         des5, after des4, 2d
    Gravação do Vídeo         :         des6, after des5, 1d
```
