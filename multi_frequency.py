import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

def plot_multiple_frequency_charts(dataframe, years, min_amount=10000):
    for year in years:
        recent_people = dataframe[dataframe['Anno'] == year]

        nationality_frequencies = recent_people.groupby('Cittadinanza')['Residenti'].sum().reset_index()
        nationality_frequencies = nationality_frequencies[nationality_frequencies['Residenti'] > min_amount]
        nationality_frequencies = nationality_frequencies.sort_values(by='Residenti', ascending=False)

        plt.figure(figsize=(12, 6))
        plt.bar(nationality_frequencies['Cittadinanza'], nationality_frequencies['Residenti'])
        plt.title(f"Foreigners per Country in Milan- {year} (min {min_amount} people)")
        plt.xlabel('Nationality')
        plt.ylabel('Residents')
        plt.tight_layout()
        plt.show()


people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)
years = [2014, 2019, 2024]

plot_multiple_frequency_charts(people, years)