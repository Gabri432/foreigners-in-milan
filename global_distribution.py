import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

year = 2024

people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)
nationality_frequencies = people[people['Anno'].eq(year)].groupby('Cittadinanza')['Residenti'].sum().reset_index()


fig = px.choropleth(nationality_frequencies,
                    locations="Cittadinanza",
                    locationmode="country names",
                    color="Residenti",
                    hover_name="Residenti",
                    color_continuous_scale=px.colors.sequential.tempo,
                    title=(f"Nationality of foreigners in Milan in {year}"))

fig.show()
