import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import geopandas as gpd

plt.style.use('default')

year = 2024

people = pd.read_csv('datasets/simplified_dataset.csv', sep=';', index_col=False)
city_map = gpd.read_file('datasets/milan.geojson')
foreigners_per_area = people[people['Anno'].eq(year) & people["Cittadinanza"].ne("Italy")].groupby('IdNil')['Residenti'].sum().reset_index()

merged_data = city_map.merge(foreigners_per_area, left_on='ID_NIL', right_on='IdNil')


fig = px.choropleth_map(
    merged_data,
    geojson=merged_data.geometry,
    locations=merged_data.index,
    color='Residenti',
    color_continuous_scale=px.colors.sequential.tempo,
    center={'lat': 45.4642, 'lon': 9.19},
    zoom=10,
    opacity=0.8,
    hover_name='NIL'
)

fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
fig.show()