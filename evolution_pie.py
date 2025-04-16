import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)


starting_year = 1994
ending_year = 2024
min_value = 10000


years = list(range(starting_year, ending_year + 1))


plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(8, 8))

def get_yearly_data(year):
    
    year_data = people[people['Anno'] == year]
    nationality_freq = year_data.groupby('Cittadinanza')['Residenti'].sum().reset_index()
    filtered = nationality_freq[nationality_freq['Residenti'] > min_value]
    other_nationalities = nationality_freq[nationality_freq['Residenti'] < min_value]
    
    if not other_nationalities.empty:
        other_total = other_nationalities['Residenti'].sum()
        other_row = pd.DataFrame([{'Cittadinanza': 'Other', 'Residenti': other_total}])
        pie_data = pd.concat([filtered, other_row], ignore_index=True)
    else:
        pie_data = filtered.copy()


    pie_data = pie_data.sort_values(by='Residenti', ascending=False)
    print(pie_data)
    return pie_data.sort_values(by='Residenti', ascending=False)

def update(frame):
    ax.clear()
    year = years[frame]
    data = get_yearly_data(year)

    wedges, texts, autotexts = ax.pie(
        data['Residenti'],
        labels=data['Cittadinanza'],
        pctdistance=0.9,
        autopct='%1.2f%%',
        startangle=90,
        colors=["red", "orange", "yellow", "lightgreen","green", "blue", "skyblue", "purple", "pink", "brown", "gray", "lightgrey"]
    )
    ax.set_title(f'Nationalities in Milan in {year} (>{min_value} people)', fontsize=14)

ani = FuncAnimation(fig, update, frames=len(years), repeat=False, interval=750)

plt.tight_layout()
plt.show()
