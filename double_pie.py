import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)

starting_year = 2024
ending_year = 2024
minimum_amount = 2000

recent_people = people[
    people['Anno'].between(starting_year, ending_year) &
    people['Residenti'].ge(minimum_amount)
]

people_continents = recent_people['Continente'].value_counts()
people_citizenships = recent_people['Cittadinanza'].value_counts()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 8))

people_continents.plot.pie(
    ax=ax1,
    colors=["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "lightgrey"],
    legend=False,
    autopct='%1.1f%%'
)
ax1.set_title("Continenti di provenienza a Milano")
ax1.set_ylabel("")  

people_citizenships.plot.pie(
    ax=ax2,
    colors=["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "lightgrey"],
    legend=False,
    autopct='%1.1f%%'
)
ax2.set_title("Paesi di provenienza a Milano (1000+ persone)")
ax2.set_ylabel("")

plt.tight_layout()
plt.show()
