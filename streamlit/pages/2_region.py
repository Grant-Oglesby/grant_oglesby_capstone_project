import streamlit as st
import pandas as pd
import plotly.express as px
import os


# Page configuration
st.set_page_config(
    page_title="Regional Data",
    layout="wide"
)


# Function to aggregate by region and year with a variable aggregate function
def aggregate_by_region_year(df, agg_func):
    return df.groupby(['region', 'year'], as_index=False).agg(
        agg_func, numeric_only=True
    )


# import dataset as pd.DataFrame
file_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(
    file_dir, "..", "..", "data", "load", "go_capstone_data.csv"
)
df = pd.read_csv(csv_path)

# Create region DataFrames with different aggregate functions
df_regions_mean = aggregate_by_region_year(df, 'mean')
df_regions_sum = aggregate_by_region_year(df, 'sum')
df_regions_median = aggregate_by_region_year(df, 'median')
df_regions_min = aggregate_by_region_year(df, 'min')
df_regions_max = aggregate_by_region_year(df, 'max')

# list of each df_regions aggregate
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
st.sidebar.header("Region Options")
# Select what values to display on y axis
y_axis_options = df.columns[
    (df.dtypes != 'object') & (df.columns != 'year')
].tolist()
selected_y_axis = st.sidebar.selectbox(
    "Select Y Axis",
    options=y_axis_options,
    index=2
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

# Filter DataFrame based on selections
# Filtering chart directly is exclusive for time ranges
filtered_df = df_regions[selected_aggregation][
    (df_regions[selected_aggregation]['year'] >= selected_year_range[0]) &
    (df_regions[selected_aggregation]['year'] <= selected_year_range[1])
]

# Display selected chart option as line graph
fig = px.line(
    filtered_df,
    x='year',
    y=selected_y_axis,
    title=f'{selected_aggregation} of {selected_y_axis} Over Time',
    labels={'year': 'Year'},
    color='region',
    range_x=selected_year_range
)
st.plotly_chart(fig)

# Display select option in pie chart format
fig_pie = px.pie(
    filtered_df,
    names='region',
    values=selected_y_axis,
    title=f'{selected_aggregation} of {selected_y_axis} by Region'
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
st.plotly_chart(fig_pie, use_container_width=True)
