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

plt.figure(figsize=(8, 8))
plt.pie(
    pie_data['Residenti'],
    labels=pie_data['Cittadinanza'],
    pctdistance=0.8,
    autopct='%1.2f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'black'},
    colors=["red", "orange", "yellow", "lightgreen","green", "blue", "skyblue", "purple", "pink", "brown", "gray", "lightgrey"],
)
plt.title(f"Foreigners per country in Milan above {minimum_amount} people")

plt.show()