import streamlit as st
import pandas as pd
import plotly.express as px
import os


# Page configuration
st.set_page_config(
    page_title="Country Data",
    page_icon=":bar_chart:",
    layout="wide"
)

# import dataset as pd.DataFrame
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(
    script_dir, "..", "..", "data", "load", "go_capstone_data.csv"
)
df_countries = pd.read_csv(csv_path)

# Setup sidebar to provide functionality
st.sidebar.header("Country Options")
# Select countries to display
select_all_countries = st.sidebar.checkbox(
    "Select All Countries",
    value=False
)
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=df_countries['country'].unique()
)
if select_all_countries:
    selected_countries = df_countries['country'].unique().tolist()
# Select what values to display on y axis
y_axis_options = df_countries.columns[
    (df_countries.dtypes != 'object') & (df_countries.columns != 'year')
].tolist()
selected_y_axis = st.sidebar.selectbox(
    "Select Y Axis",
    options=y_axis_options
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

# Display selected chart option as line graph
fig = px.line(
    df_countries[df_countries['country'].isin(selected_countries)],
    x='year',
    y=selected_y_axis,
    title='CO2 Emissions per Capita Over Time',
    labels={'year': 'Year'},
    color='country',
    range_x=selected_year_range
)
st.plotly_chart(fig)

# Display select option in geographical format
fig_geo = px.choropleth(
    df_countries[df_countries['country'].isin(selected_countries)],
    locations='iso_code',
    color=selected_y_axis,
    hover_name='country',
    animation_frame='year',
    title=(
        f'Geographical Distribution of {selected_y_axis}'
    ),
    color_continuous_scale=px.colors.sequential.Plasma,
    scope="world"
)
st.plotly_chart(fig_geo, use_container_width=True)
