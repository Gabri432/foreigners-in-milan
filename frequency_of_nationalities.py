import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)

starting_year = 2024
ending_year = 2024
min_value = 5000

recent_people = people[people['Anno'].between(starting_year, ending_year)]

nationality_frequencies = recent_people.groupby('Cittadinanza')['Residenti'].sum().reset_index()

filtered_nationalities = nationality_frequencies[nationality_frequencies['Residenti'] > min_value]

filtered_nationalities = filtered_nationalities.sort_values(by='Residenti', ascending=True) #ascending=False

plt.figure(figsize=(12, 6))
plt.barh(filtered_nationalities['Cittadinanza'], filtered_nationalities['Residenti'], 
        color=["#22EEFF", "#22EEFF", "#22EEFF", "#00ABFF", "#0088FF", "#0055EE", "#0044CC", "#0033AB", "#0022AB", "#0011AA", "#001188", "#000066"], 
        height=0.3)
#plt.bar(...width=0.3)
plt.ylabel('Nazionalità')
plt.xlabel('Cittadini')
plt.xticks(fontsize=12)
plt.title(f'Nazionalità che superano le {min_value} persone')
plt.tight_layout()
plt.show()
