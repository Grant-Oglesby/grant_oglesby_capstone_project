import streamlit as st
import pandas as pd
import plotly.express as px
import os


# Page configuration
st.set_page_config(
    page_title="Correlation Analysis",
    layout="wide"
)

# import dataset as pd.DataFrame
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(
    script_dir, "..", "..", "data", "load", "go_capstone_data.csv"
)
df_countries = pd.read_csv(csv_path)

# Setup sidebar to provide functionality
st.sidebar.header("Correlation Options")
# Select region to narrow country options
selected_region = st.sidebar.multiselect(
    "Select Region",
    options=df_countries['region'].unique()
)
# Select countries to display
select_all_countries = st.sidebar.checkbox(
    "Select All Countries",
    value=False
)
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=(
        df_countries[df_countries['region'].isin(selected_region)]['country']
        .unique()
    )
)
if select_all_countries:
    selected_countries = (
        df_countries[df_countries['region'].isin(selected_region)]['country']
        .unique()
        .tolist()
    )
# Select what values to display on y axis
y_axis_options = df_countries.columns[2:].tolist()
y_axis_options.remove('gdp')
y_axis_options.remove('iso_code')
y_axis_options.remove('population')
y_axis_options.remove('region')
selected_y_axis = st.sidebar.selectbox(
    "Select Y Axis",
    options=y_axis_options
)
x_axis_options = ['gdp', 'population']
selected_x_axis = st.sidebar.selectbox(
    "Select X Axis",
    options=x_axis_options
)
# Slider to select what range of years to display
selected_year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=int(df_countries['year'].min()),
    max_value=int(df_countries['year'].max()),
    value=(int(df_countries['year'].min()),
           int(df_countries['year'].max())
           ),
    step=1
)

# Filter DataFrame based on selections
# Filtering chart directly is exclusive for time ranges
filtered_df = df_countries[
    (df_countries['country'].isin(selected_countries)) &
    (df_countries['year'] >= selected_year_range[0]) &
    (df_countries['year'] <= selected_year_range[1])
]

# Display selected chart options as scatter graph
fig = px.scatter(
    filtered_df,
    x=selected_x_axis,
    y=selected_y_axis,
    color='country',
    title="Correlation Analysis",
    trendline="ols"
)
st.plotly_chart(fig)
