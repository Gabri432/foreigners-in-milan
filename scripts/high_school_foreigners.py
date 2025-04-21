import pandas as pd
import matplotlib.pyplot as plt

people = pd.read_csv("datasets/Alunni_Scuole_Secondarie_di_Secondo_Grado_per_cittadinanza_(2007_08-2023_24).csv", delimiter=',')

academic_year = "2023/2024"

recent_people = people[people['Anno scolastico'].eq(academic_year)]

total_italians = recent_people[recent_people["Cittadinanza"].eq("Italiani")].sum()["Alunni - Anno scolastico"]

total_foreigners = recent_people[recent_people["Cittadinanza"].ne("Italiani")].sum()["Alunni - Anno scolastico"]

first_year_foreigners = recent_people[recent_people["Cittadinanza"].ne("Italiani") & recent_people["Anno di corso"].eq("1° Anno")].sum()["Alunni - Anno scolastico"]
second_year_foreigners = recent_people[recent_people["Cittadinanza"].ne("Italiani") & recent_people["Anno di corso"].eq("2° Anno")].sum()["Alunni - Anno scolastico"]
third_year_foreigners = recent_people[recent_people["Cittadinanza"].ne("Italiani") & recent_people["Anno di corso"].eq("3° Anno")].sum()["Alunni - Anno scolastico"]
fourth_year_foreigners = recent_people[recent_people["Cittadinanza"].ne("Italiani") & recent_people["Anno di corso"].eq("4° Anno")].sum()["Alunni - Anno scolastico"]
fifth_year_foreigners = recent_people[recent_people["Cittadinanza"].ne("Italiani") & recent_people["Anno di corso"].eq("5° Anno")].sum()["Alunni - Anno scolastico"]


sizes1 = [total_italians / (total_italians + total_foreigners), total_foreigners / (total_italians + total_foreigners)]
labels1 = [f'Italiani - {sizes1[0]:.2f}%', f'Stranieri - {sizes1[1]:.2f}%']

sizes2 = [first_year_foreigners / total_foreigners, 
          second_year_foreigners / total_foreigners, 
          third_year_foreigners / total_foreigners,
          fourth_year_foreigners / total_foreigners,
          fifth_year_foreigners / total_foreigners]
labels2 = [f'1° anno - {sizes2[0]:.2f}%',
           f'2° anno - {sizes2[1]:.2f}%',
           f'3° anno - {sizes2[2]:.2f}%',
           f'4° anno - {sizes2[3]:.2f}%',
           f'5° anno - {sizes2[4]:.2f}%']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.pie(sizes1, labels=labels1, wedgeprops={'width': 0.4}, startangle=90, colors=["#22EEFF", "#00ABFF"])
ax1.set_title('Rapporto tra studenti stranieri ed italiani delle scuole superiori')

ax2.pie(sizes2, labels=labels2, wedgeprops={'width': 0.4}, startangle=90, colors=["#00ABFF", "#0055EE", "#0044CC", "#0033AB", "#0022AB"])
ax2.set_title('Percentuali alunni stranieri delle scuole superiori per anno di corso')

plt.tight_layout()
plt.show()