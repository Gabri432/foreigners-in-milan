import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)

starting_year = 2024
ending_year = 2024
min_value = 1000

recent_people = people[people['Anno'].between(starting_year, ending_year)]

nationality_frequencies = recent_people.groupby('Cittadinanza')['Residenti'].sum().reset_index()

filtered_nationalities = nationality_frequencies[nationality_frequencies['Residenti'] > min_value]

filtered_nationalities = filtered_nationalities.sort_values(by='Residenti', ascending=False)

print(filtered_nationalities)

plt.figure(figsize=(12, 6))
plt.bar(filtered_nationalities['Cittadinanza'], filtered_nationalities['Residenti'], color='skyblue')
plt.xlabel('Nationalities')
plt.ylabel('Citizens')
plt.title(f'Nationalities exceeding {min_value} people')
plt.xticks(rotation=80)
plt.tight_layout()
plt.show()
