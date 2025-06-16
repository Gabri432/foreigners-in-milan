import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)

year = 2024

recent_people = people[people['Anno'].eq(year)]

men = (recent_people[recent_people["Genere"].eq("Maschi")]).groupby('Genere')['Residenti'].sum().iloc[0]
women = (recent_people[recent_people["Genere"].eq("Femmine")]).groupby('Genere')['Residenti'].sum().iloc[0]


ratios = pd.Series(
    [(men / (men + women)) * 100, (women / (men + women)) * 100],
    index=["Uomini", "Donne"]
    )

fig, ax = plt.subplots(figsize=(12, 12))
ratios.plot.pie(
    ax=ax,
    colors=["#0099FF", "skyblue"],
    startangle=90,
    labeldistance=None,
    wedgeprops={"alpha": 0.5},
    autopct='%1.2f%%',
    explode=[0.05] * len(ratios.values)
)

ax.legend(
    labels=ratios.index,
    title=f"Categorie ({year})",
    loc="center right",
    bbox_to_anchor=(1, 0, 0.3, 1),
    title_fontsize='large'
)

plt.tight_layout()
plt.show()