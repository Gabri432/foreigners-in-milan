import pandas as pd
import matplotlib.pyplot as plt

foreigners = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)
population = pd.read_csv('datasets/ds1494_popolazione-calcolata-dal-1880.csv', sep=';', index_col=False)

year = 2024

def foreigners_pop(year):
    people_per_year = foreigners[foreigners['Anno'].eq(year)]
    total_per_country = people_per_year.groupby('Cittadinanza')['Residenti'].sum()
    sum = 0
    for country_pop in total_per_country:
        sum += country_pop
    
    return sum

def tot_pop(year):
    return population[population['Anno'].eq(year)]["Popolazione"].item()

ratios = pd.Series(
    [(foreigners_pop(year) / tot_pop(year)) * 100, ((tot_pop(year) - foreigners_pop(year)) / tot_pop(year)) * 100],
    index=["Stranieri", "Italiani"]
    )


fig, ax = plt.subplots(figsize=(12, 12))
ratios.plot.pie(
    ax=ax,
    colors=["#22EEFF", "#0099FF"],
    startangle=90,
    labeldistance=None,
    autopct='%1.2f%%'
)

ax.legend(
    labels=ratios.index,
    title=f"Categorie ({year})",
    loc="center right",
    bbox_to_anchor=(1, 0, 0.2, 1),
    title_fontsize='x-large'
)

plt.tight_layout()
plt.show()