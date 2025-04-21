import pandas as pd
import matplotlib.pyplot as plt

people = pd.read_csv("datasets/ds27_pop_sto_quartiere.csv", delimiter=';')

year = 2024

recent_people = people[people['Anno'].eq(year) & people["Cittadinanza"].ne("Italia") & people["Eta"].ne("100 e più")]

recent_people['Eta'] = pd.to_numeric(recent_people['Eta'], errors='coerce')

recent_people = recent_people.dropna(subset=['Eta'])

age_frequencies = recent_people.groupby('Eta')['Residenti'].sum().reset_index()

labels =["0-17", "18-34", "35-49", "50-64", "65-100"]
age_frequencies['bins'] = pd.cut(age_frequencies["Eta"],bins=[0, 18, 35, 50, 65, 101], labels=labels)
bins = age_frequencies.groupby('bins', observed=True)['Residenti'].sum()

total = bins.values.sum()

legend_labels = [
    f"{label} - {value:.2f}%" for label, value in zip(bins.index, (bins.values / total * 100))
]


fig, ax = plt.subplots(figsize=(12, 12))
wedges, _ = ax.pie(
    bins.values,
    labels=None,
    startangle=90,
    wedgeprops={'edgecolor': 'black'},
    colors=["#22EEFF", "#00ABFF", "#0055EE", "#0044CC", "#0033AB", "#0022AB", "#0011AA", "#001188", "#000066"]
)

fig.suptitle(
    f"Peso di ciascuna fascia d'età dei stranieri nel {year}",
    x=0.5,
    y=0.95,
    fontsize=16,
    fontweight='bold'
)

ax.legend(wedges, legend_labels, title="Fasce d'età", loc="center", bbox_to_anchor=(1, 0, 0.5, 1))
plt.tight_layout()
plt.show()


