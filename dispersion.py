import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)

print(people.columns)
starting_year = 2004
ending_year = 2024

men = people.loc[(people['Genere']=='Maschi') & (people['Anno'].between(starting_year, ending_year))]
citizenships_of_men = men["Anno"]
print(citizenships_of_men.describe())

women = people.loc[(people['Genere']=='Femmine') & (people['Anno'].between(starting_year, ending_year))]
citizenships_of_women = women["Anno"]
print(citizenships_of_women.describe())

plt.subplot(1, 2, 1)
plt.ylabel('Citizenships of men')
citizenships_of_men.plot.box(whis=(0, 100))
plt.subplot(1, 2, 2)
plt.ylabel('Citizenships of women')
citizenships_of_women.plot.box(whis=(0, 100))
plt.show()