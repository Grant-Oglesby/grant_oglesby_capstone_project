import streamlit as st
import pandas as pd
import plotly.express as px
import os


# Page configuration
st.set_page_config(
    page_title="Regional Data",
    page_icon=":bar_chart:",
    layout="wide"
)


# Function to aggregate by region and year with a variable aggregate function
def aggregate_by_region_year(df, agg_func):
    return df.groupby(['region', 'year'], as_index=False).agg(
        agg_func, numeric_only=True
    )


# import dataset as pd.DataFrame
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(
    script_dir, "..", "..", "data", "load", "go_capstone_data.csv"
)
df = pd.read_csv(csv_path)

# Create region DataFrames with different aggregate functions
df_regions_mean = aggregate_by_region_year(df, 'mean')
df_regions_sum = aggregate_by_region_year(df, 'sum')
df_regions_median = aggregate_by_region_year(df, 'median')
df_regions_min = aggregate_by_region_year(df, 'min')
df_regions_max = aggregate_by_region_year(df, 'max')

# list of each df_regions
df_regions = {
    "Mean": df_regions_mean,
    "Sum": df_regions_sum,
    "Median": df_regions_median,
    "Min": df_regions_min,
    "Max": df_regions_max
}

# Get list of regions and countries
region_countries = df.groupby('region')['country'].unique().to_dict()
countries = df['country'].unique().tolist()

# Setup sidebar to provide functionality
st.sidebar.header("Aggregation Options")
# Select what values to display on y axis
y_axis_options = df.columns[
    (df.dtypes != 'object') & (df.columns != 'year')
].tolist()
selected_y_axis = st.sidebar.selectbox(
    "Select Y Axis",
    options=y_axis_options
    )
# Select aggregate function to display
selected_aggregation = st.sidebar.selectbox(
    "Select Aggregation",
    options=["Mean", "Sum", "Median", "Min", "Max"]
)
# Slider to select what range of years to display
selected_year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=int(df['year'].min()),
    max_value=int(df['year'].max()),
    value=(int(df['year'].min()), int(df['year'].max())),
    step=1
)

# Display selected chart option as line graph
fig = px.line(
    df_regions[selected_aggregation],
    x='year',
    y=selected_y_axis,
    title='CO2 Emissions per Capita Over Time',
    labels={'year': 'Year'},
    color='region',
    range_x=selected_year_range
)
st.plotly_chart(fig)

# Display select option in geographical format
fig_geo = px.choropleth(
    df_regions[selected_aggregation],
    locations='iso_code',
    color=selected_y_axis,
    hover_name='region',
    animation_frame='year',
    title=(
        f'Geographical Distribution of {selected_aggregation} '
        f'{selected_y_axis}'
    ),
    color_continuous_scale=px.colors.sequential.Plasma
)
st.plotly_chart(fig_geo)
