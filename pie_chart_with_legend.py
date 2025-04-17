import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)

starting_year = 2024
ending_year = 2024
minimum_amount = 10000

recent_people = people[people['Anno'].between(starting_year, ending_year)]

nationality_frequencies = recent_people.groupby('Cittadinanza')['Residenti'].sum().reset_index()

filtered_nationalities = nationality_frequencies[nationality_frequencies['Residenti'] >= minimum_amount]
other_nationalities = nationality_frequencies[nationality_frequencies['Residenti'] < minimum_amount]

if not other_nationalities.empty:
    other_total = other_nationalities['Residenti'].sum()
    other_row = pd.DataFrame([{'Cittadinanza': 'Other', 'Residenti': other_total}])
    pie_data = pd.concat([filtered_nationalities, other_row], ignore_index=True)
else:
    pie_data = filtered_nationalities.copy()

pie_data = pie_data.sort_values(by='Residenti', ascending=False)

total = pie_data['Residenti'].sum()
pie_data['Percent'] = pie_data['Residenti'] / total * 100

legend_labels = [
    f"{row['Cittadinanza']} - {row['Percent']:.2f}%" for _, row in pie_data.iterrows()
]

fig, ax = plt.subplots(figsize=(12, 12))
wedges, _ = ax.pie(
    pie_data['Residenti'],
    labels=None,
    startangle=90,
    wedgeprops={'edgecolor': 'black'},
    #colors=["red", "orange", "yellow", "lightgreen", "green", "blue", "skyblue", "purple", "pink", "brown", "gray", "lightgrey"]
    colors=["white", "#000066", "#001188", "#0011AA", "#0022AB", "#0033AB", "#0044CC", "#0055EE", "#0088FF", "#00ABFF", "#22EEFF"]
)

fig.suptitle(
    f"Nazionalità più comuni a Milano sopra le {minimum_amount} persone, nel {starting_year}",
    x=0.5,
    y=0.95,
    fontsize=16,
    fontweight='bold'
)

ax.legend(wedges, legend_labels, title="Nazionalità", loc="center", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()
