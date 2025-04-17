import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)

starting_year = 2024
ending_year = 2024
min_value = 5000

recent_people = people[people['Anno'].between(starting_year, ending_year)]

nationality_frequencies = recent_people.groupby('Cittadinanza')['Residenti'].sum().reset_index()

filtered_nationalities = nationality_frequencies[nationality_frequencies['Residenti'] > min_value]

filtered_nationalities = filtered_nationalities.sort_values(by='Residenti', ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(filtered_nationalities['Cittadinanza'], filtered_nationalities['Residenti'], 
        color=["#000066", "#001188", "#0011AA", "#0022AB", "#0033AB", "#0044CC", "#0055EE", "#0088FF", "#00ABFF", "#22EEFF", "#22EEFF", "#22EEFF"], 
        width=0.3)
plt.xlabel('Nazionalità')
plt.ylabel('Cittadini')
plt.xticks(fontsize=12)
plt.title(f'Nazionalità che superano le {min_value} persone')
plt.tight_layout()
plt.show()
