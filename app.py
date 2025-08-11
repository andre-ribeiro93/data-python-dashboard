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
selected_years = st.sidebar.multiselect(
    "Year",
    options=available_years,
    default=available_years
)

# Seniority Filter
available_seniorities = sorted(df['seniority'].unique())
selected_seniorities = st.sidebar.multiselect(
    "Seniority",
    options=available_seniorities,
    default=available_seniorities
)

# Contract Type Filter
available_contracts = sorted(df['employment_contract'].unique())
selected_contracts = st.sidebar.multiselect(
    "Contract Type", 
    options=available_contracts,
    default=available_contracts
)

# Company Size Filter
available_sizes = sorted(df['company_size'].unique())
selected_sizes = st.sidebar.multiselect(
    "Company Size",
    options=available_sizes,
    default=available_sizes
)

# Job Position Filter
available_positions = sorted(df['job_position'].unique())
all_positions_option = 'All positions'
position_options = [all_positions_option] + available_positions

# Map Job Selection
selected_positions = st.sidebar.multiselect(
    "Job position",
    options=position_options,
    default=all_positions_option,
    help="Select one or more job positions."
)

if all_positions_option in selected_positions:
    filtered_positions = available_positions
else:
    filtered_positions = selected_positions


# --- DataFrame Filtering ---
# The main dataframe is filtered based on the sidebar selections.
df_filtered = df[
    (df['year'].isin(selected_years)) &
    (df['seniority'].isin(selected_seniorities)) &
    (df['employment_contract'].isin(selected_contracts)) &
    (df['company_size'].isin(selected_sizes)) &
    (df['job_position'].isin(filtered_positions))
]

# --- Main Content ---
st.title("🎲 Salary Analysis Dashboard in the Data Area")
st.markdown("Explore salary data in the data area over the past few years. Use the filters on the left to refine your analysis.")

# --- Main Metrics (KPIs) ---
st.subheader("General metrics (Annual salary in USD)")

if not df_filtered.empty:
    average_salary = df_filtered['usd_salary'].mean()
    median_salary = df_filtered['usd_salary'].median()
    max_salary = df_filtered['usd_salary'].max()
    total_records = df_filtered.shape[0]
    most_frequent_position = df_filtered['job_position'].mode()[0]
else:
    # standard values to avoid error
    average_salary, median_salary, max_salary, total_records, most_frequent_position = 0, 0, 0, 0, "-"
    # message to user
    st.warning("⚠️ No data to display in the main metrics - select at least one option for each filter.")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Average salary", f"${average_salary:,.0f}")
col2.metric("Median salary", f"${median_salary:,.0f}")
col3.metric("Maximum salary", f"${max_salary:,.0f}")
col4.metric("Total records", f"{total_records:,}")
col5.metric("Most frequent position", most_frequent_position)

st.markdown("---")

# --- Visual Analysis with Plotly ---
st.subheader("Charts")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtered.empty:
        top_positions = df_filtered.groupby('job_position')['usd_salary'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        position_chart = px.bar(
            top_positions,
            x='usd_salary',
            y='job_position',
            orientation='h',
            title="Top 10 jobs by average salary",
            labels={'usd_salary': "Average annual salary (USD)", 'job_position': ""}
        )
        position_chart.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(position_chart, use_container_width=True)
    else:
        st.warning("No data to display in the job chart.")

with col_graf2:
    if not df_filtered.empty:
        hist_chart = px.histogram(
            df_filtered,
            x='usd_salary',
            nbins=30,
            title="Distribution of annual salaries",
            labels={'usd_salary': "Salary range (USD)", 'count': ""}
        )
        hist_chart.update_layout(title_x=0.1)
        st.plotly_chart(hist_chart, use_container_width=True)
    else:
        st.warning("No data to display distribution graphs.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtered.empty:
        count_remote = df_filtered['work_modality'].value_counts().reset_index()
        count_remote.columns = ['work_modality', 'quantity']
        remote_chart = px.pie(
            count_remote,
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
        df_map = df_filtered.copy()
        mean_contry = df_map.groupby('residence_iso3')['usd_salary'].mean().reset_index()

        if set(filtered_positions) == set(available_positions):
            title_display = "Average salary by country"
        elif len(filtered_positions) == 1:
            title_display = f"Average {filtered_positions[0]} salary by country"
        else:
            title_display = "Average salary (selected positions) by country"

        country_chart = px.choropleth(
            mean_contry,
            locations='residence_iso3',
            color='usd_salary',
            color_continuous_scale='rdylgn',
            title=title_display,
            hover_name='residence_iso3',
            hover_data={
                'usd_salary': ':,.0f',
                'residence_iso3': False
            },
            labels={'usd_salary': "Average annual salary (USD)", 'residence_iso3': "Country"})
        country_chart.update_layout(title_x=0.1)
        st.plotly_chart(country_chart, use_container_width=True)
    else:
        st.warning("No data to display in country chart.")

# --- Detailed Data Table ---
st.subheader("Detailed Data")
st.dataframe(df_filtered)