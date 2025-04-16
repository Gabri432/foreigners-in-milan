import pandas as pd
import matplotlib.pyplot as plt
import math

plt.style.use('fivethirtyeight')

def plot_multiple_pie_charts(dataframe, years, min_amount=10000):
    num_years = len(years)
    charts = 3 
    rows = math.ceil(num_years / charts)

    fig, axes = plt.subplots(rows, charts, figsize=(charts * 6, rows * 6))
    axes = axes.flatten()

    for i, year in enumerate(years):
        ax = axes[i]
        
        yearly_data = dataframe[dataframe['Anno'] == year]
        nationality_frequencies = yearly_data.groupby('Cittadinanza')['Residenti'].sum().reset_index()

        filtered = nationality_frequencies[nationality_frequencies['Residenti'] >= min_amount]
        others = nationality_frequencies[nationality_frequencies['Residenti'] < min_amount]

        if not others.empty:
            other_total = others['Residenti'].sum()
            other_row = pd.DataFrame([{'Cittadinanza': 'Other', 'Residenti': other_total}])
            pie_data = pd.concat([filtered, other_row], ignore_index=True)
        else:
            pie_data = filtered.copy()

        pie_data = pie_data.sort_values(by='Residenti', ascending=False)

        ax.pie(
            pie_data['Residenti'],
            labels=pie_data['Cittadinanza'],
            pctdistance=0.8,
            autopct='%1.2f%%',
            startangle=90,
            wedgeprops={'edgecolor': 'black'},
            colors=["red", "orange", "yellow", "lightgreen","green", "blue", "skyblue", "purple", "pink", "brown", "gray", "lightgrey"]
        )
        ax.set_title(f"{year}", fontsize=14)

    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    plt.suptitle(f"Foreigners per country in Milan per Year (min {min_amount} people)", fontsize=18)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)

years = [1994, 2000, 2006, 2012, 2018, 2024]

plot_multiple_pie_charts(people, years)
