import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Dashboard E-Commerce - Dadosfera Case",
    page_icon="📊",
    layout="wide"
)

# --- LEITURA DE DADOS ---
@st.cache_data
def load_data():
    # Caminho relativo considerando que rodamos o app da raiz
    path = 'data/olist_processed.parquet'
    
    # Verifica se existe o arquivo enriquecido (com IA), senão usa o normal
    if os.path.exists('data/olist_enriched_gemini.parquet'):
        path = 'data/olist_enriched_gemini.parquet'

    if not os.path.exists(path):
        return None
        
    df = pd.read_parquet(path)
    return df

df = load_data()

# --- SIDEBAR (FILTROS) ---
# st.sidebar.image("https://dadosfera.ai/wp-content/uploads/2022/08/logo-dadosfera-1.png", width=200)
st.sidebar.header("Filtros Globais")

if df is not None:
    # Filtro de Estado
    todos_estados = sorted(df['customer_state'].unique())
    estado_selecionado = st.sidebar.multiselect(
        "Selecione o Estado (UF):",
        options=todos_estados,
        default=todos_estados[:5] # Seleciona os 5 primeiros por padrão
    )
    
    # Aplicando Filtro
    if estado_selecionado:
        df_filtered = df[df['customer_state'].isin(estado_selecionado)]
    else:
        df_filtered = df # Se nada selecionado, mostra tudo

    # --- CORPO DO DASHBOARD ---
    st.title("📊 Painel de Vendas e Inteligência - Olist")
    st.markdown("---")

    # 1. KPIs (Indicadores Chave)
    col1, col2, col3, col4 = st.columns(4)
    
    total_vendas = df_filtered['price'].sum()
    total_pedidos = df_filtered['order_id'].nunique()
    ticket_medio = total_vendas / total_pedidos if total_pedidos > 0 else 0
    
    col1.metric("Faturamento Total", f"R$ {total_vendas:,.2f}")
    col2.metric("Total de Pedidos", f"{total_pedidos}")
    col3.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")
    
    # Se tiver coluna de IA, mostra métrica de sentimento
    if 'sentimento_ia' in df_filtered.columns:
        pct_positivo = (df_filtered['sentimento_ia'] == 'positivo').mean() * 100
        col4.metric("% Satisfação (IA)", f"{pct_positivo:.1f}%")

    st.markdown("---")

    # 2. GRÁFICOS VISUAIS
    col_g1, col_g2 = st.columns(2)

    with col_g1:
        st.subheader("Evolução de Vendas no Tempo")
        # Agrupando por mês
        vendas_tempo = df_filtered.set_index('order_purchase_timestamp').resample('M')['price'].sum().reset_index()
        fig_tempo = px.line(vendas_tempo, x='order_purchase_timestamp', y='price', title="Faturamento Mensal")
        st.plotly_chart(fig_tempo, use_container_width=True)

    with col_g2:
        st.subheader("Top 10 Categorias")
        top_cat = df_filtered['product_category_name'].value_counts().head(10).reset_index()
        top_cat.columns = ['Categoria', 'Qtd Vendas']
        fig_bar = px.bar(top_cat, x='Qtd Vendas', y='Categoria', orientation='h', title="Categorias Mais Vendidas")
        st.plotly_chart(fig_bar, use_container_width=True)

    # 3. ANÁLISE DE IA (Se disponível)
    if 'sentimento_ia' in df_filtered.columns:
        st.markdown("---")
        st.header("🧠 Inteligência Artificial: Análise de Reviews")
        st.info("Classificação realizada via LLM (Simulação/Gemini) sobre comentários dos clientes.")
        
        col_ia1, col_ia2 = st.columns(2)
        
        with col_ia1:
            # Gráfico de Pizza - Sentimentos
            fig_pizza = px.pie(df_filtered, names='sentimento_ia', title="Distribuição de Sentimentos", hole=0.4)
            st.plotly_chart(fig_pizza, use_container_width=True)
            
        with col_ia2:
            # Gráfico de Barras - Motivos
            fig_motivos = px.histogram(df_filtered, x='motivo_ia', color='sentimento_ia', title="Principais Motivos dos Reviews")
            st.plotly_chart(fig_motivos, use_container_width=True)

        # Amostra de Dados
        with st.expander("Ver Detalhes dos Comentários Classificados"):
            st.dataframe(df_filtered[['review_score', 'review_comment_message', 'sentimento_ia', 'motivo_ia']].head(50))

else:
    st.error("⚠️ Arquivo de dados não encontrado. Rode os notebooks primeiro!")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("*Desenvolvido para o Case Técnico Dadosfera*")