import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
# Sets the page title, icon, and layout to ocupate the entire width.
st.set_page_config(
  page_title="Salary Dashboard in the Data Area",
  page_icon='📊',
  layout='wide'
)

# --- Data loading ---
df = pd.read_csv('./data-final-version.csv')

# --- Sidebar (Filters) ---
st.sidebar.header("🔍 Filters")

# Year Filter
available_years = sorted(df['year'].unique())
selected_years = st.sidebar.multiselect("Year", available_years, default=available_years)

# Seniority Filter
available_seniorities = sorted(df['seniority'].unique())
selected_seniorities = st.sidebar.multiselect("Seniority", available_seniorities, default=available_seniorities)

# Contract Type Filter
available_contracts = sorted(df['employment_contract'].unique())
selected_contracts = st.sidebar.multiselect("Contract Type", available_contracts, default=available_contracts)

# Company Size Filter
available_sizes = sorted(df['company_size'].unique())
selected_sizes = st.sidebar.multiselect("Company Size", available_sizes, default=available_sizes)

# Job Position Filter
available_positions = sorted(df['job_position'].unique())
selected_positions = st.sidebar.multiselect("Job Position", available_positions, default=available_positions)

# --- DataFrame Filtering ---
# The main dataframe is filtered based on the sidebar selections.
df_filtered = df[
    (df['year'].isin(selected_years)) &
    (df['seniority'].isin(selected_seniorities)) &
    (df['employment_contract'].isin(selected_contracts)) &
    (df['company_size'].isin(selected_sizes)) &
    (df['job_position'].isin(selected_positions))
]

# --- Main Content ---
st.title("🎲 Salary Analysis Dashboard in the Data Area")
st.markdown("Explore salary data in the data area over the past few years. Use the filters on the left to refine your analysis.")

# --- Main Metrics (KPIs) ---
st.subheader("General metrics (Annual salary in USD)")

if not df_filtered.empty:
    average_salary = df_filtered['usd_salary'].mean()
    max_salary = df_filtered['usd_salary'].max()
    total_records = df_filtered.shape[0]
    most_frequent_position = df_filtered['job_position'].mode()[0]
else:
    average_salary, salario_mediano, max_salary, total_records, cargo_mais_comum = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("Average salary", f"${average_salary:,.0f}")
col2.metric("Maximum salary", f"${max_salary:,.0f}")
col3.metric("Total records", f"{total_records:,}")
col4.metric("Most frequent position", most_frequent_position)

st.markdown("---")

# --- Visual Analysis with Plotly ---
st.subheader("Charts")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtered.empty:
        top_cargos = df_filtered.groupby('job_position')['usd_salary'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd_salary',
            y='job_position',
            orientation='h',
            title="Top 10 jobs by average salary",
            labels={'usd_salary': "Average annual salary (USD)", 'job_position': ""}
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("No data to display in the job chart.")

with col_graf2:
    if not df_filtered.empty:
        grafico_hist = px.histogram(
            df_filtered,
            x='usd_salary',
            nbins=30,
            title="Distribution of annual salaries",
            labels={'usd_salary': "Salary range (USD)", 'count': ""}
        )
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("No data to display distribution graphs.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtered.empty:
        remoto_contagem = df_filtered['work_modality'].value_counts().reset_index()
        remoto_contagem.columns = ['work_modality', 'quantity']
        remote_chart = px.pie(
            remoto_contagem,
            names='work_modality',
            values='quantity',
            title="Proportion of work modalities",
            labels={'work_modality': "Job modality", 'quantity': "Quantity"},
            hole=0.5
        )
        remote_chart.update_traces(textinfo='percent+label')
        remote_chart.update_layout(title_x=0.1)
        st.plotly_chart(remote_chart, use_container_width=True)
    else:
        st.warning("No data to display in the job types chart.")

with col_graf4:
    if not df_filtered.empty:
        df_ds = df_filtered[df_filtered['job_position'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residence_iso3')['usd_salary'].mean().reset_index()
        grafico_paises = px.choropleth(media_ds_pais,
            locations='residence_iso3',
            color='usd_salary',
            color_continuous_scale='rdylgn',
            title='Average Data Scientist salary by country',
            hover_name='residence_iso3',
            hover_data={'residence_iso3': False},
            labels={'usd_salary': "Average annual salary (USD)", 'residence_iso3': "Country"})
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("No data to display in country chart.")

# --- Detailed Data Table ---
st.subheader("Detailed Data")
st.dataframe(df_filtered)