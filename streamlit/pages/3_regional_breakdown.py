import streamlit as st
import pandas as pd
import plotly.express as px
import os


# Page configuration
st.set_page_config(
    page_title="Region Breakdown",
    layout="wide"
)

# import dataset as pd.DataFrame
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(
    script_dir, "..", "..", "data", "load", "go_capstone_data.csv"
)
df = pd.read_csv(csv_path)

# Get list of regions and countries
region_countries = df.groupby('region')['country'].unique().to_dict()
countries = df['country'].unique().tolist()

# Setup sidebar for functionality
st.sidebar.header("Region Breakdown")
# Select what region to display
selected_region = st.sidebar.selectbox(
    "Select Region",
    options=list(region_countries.keys())
)
# Select what countries to display
select_all_countries = st.sidebar.checkbox(
    "Select All Countries",
    value=False
)
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=df[df['region'] == selected_region]['country'].unique()
)
if select_all_countries:
    selected_countries = (
        df[df['region'] == selected_region]['country']
        .unique()
        .tolist()
    )
# Select what values to display on y axis
y_axis_options = df.columns[
    (df.dtypes != 'object') & (df.columns != 'year')
].tolist()
selected_y_axis = st.sidebar.selectbox(
    "Select Y Axis",
    options=y_axis_options,
    index=2
)
# Slider to select what range of years to display
selected_year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=int(df['year'].min()),
    max_value=int(df['year'].max()),
    value=(int(df['year'].min()),
           int(df['year'].max())
           ),
    step=1
)

# Filter DataFrame based on selections
# Filtering chart directly is exclusive for time ranges
filtered_df = df[
    (df['country'].isin(selected_countries)) &
    (df['year'] >= selected_year_range[0]) &
    (df['year'] <= selected_year_range[1])
]

# Bar chart with direct comparisons of two selected countries
fig = px.bar(
    filtered_df,
    x='year',
    y=selected_y_axis,
    color='country',
    barmode='group',
    title=(
        f'Comparison of {selected_y_axis} for '
        f'{", ".join(selected_countries)}'
    ),
)
st.plotly_chart(fig)

# Display select option in pie chart format
fig_pie = px.pie(
    filtered_df,
    names='country',
    values=selected_y_axis,
    title=f'{selected_y_axis} of {selected_region}',
)
fig_pie.update_traces(
    textposition='inside',
    textinfo='percent',
    insidetextorientation='radial'
)
fig_pie.update_layout(
    uniformtext_minsize=12,
    uniformtext_mode='hide'
)
st.plotly_chart(fig_pie)
