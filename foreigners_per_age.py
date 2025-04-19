import pandas as pd
import matplotlib.pyplot as plt

people = pd.read_csv("datasets/ds27_pop_sto_quartiere.csv", delimiter=';')

year = 2024

recent_people = people[people['Anno'].eq(year) & people["Cittadinanza"].ne("Italia") & people["Eta"].ne("100 e più")]

recent_people['Eta'] = pd.to_numeric(recent_people['Eta'], errors='coerce')

recent_people = recent_people.dropna(subset=['Eta'])

age_frequencies = recent_people.groupby('Eta')['Residenti'].sum().reset_index()

labels =["0-9", "10-17", "18-24", "25-34", "35-44","45-54", "55-64", "65-100"]
age_frequencies['bins'] = pd.cut(age_frequencies["Eta"],bins=[0, 10, 18, 25, 35, 45, 55, 65, 101], labels=labels)
bins = age_frequencies.groupby('bins', observed=True)['Residenti'].sum()


plt.figure(figsize=(12, 6))
plt.grid(True, axis='y',zorder=0)
plt.bar(bins.index.astype(str), bins.values, 
        color=["#22EEFF", "#22EEFF", "#22EEFF", "#00ABFF", "#0088FF", "#0055EE", "#0044CC", "#0033AB", "#0022AB", "#0011AA", "#001188", "#000066"], 
        width=0.3, zorder=2)
plt.ylabel('Cittadini')
plt.xlabel('Anni di età')
plt.xticks(fontsize=12)
plt.tight_layout()
plt.show()
