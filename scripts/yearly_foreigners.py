import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)

starting_year = 2004
ending_year = 2024
jump_years = 1

def count_people_per_year(year):
    people_per_year = people[people['Anno'].eq(year)]
    total_per_country = people_per_year.groupby('Cittadinanza')['Residenti'].sum()
    sum = 0
    for country in total_per_country:
        sum += country
    return sum

def sequence(starting_year, ending_year, jump_years):
    begin = starting_year
    amounts = {'year': [], 'total':[]}
    while begin < ending_year+jump_years:
        amounts["total"].append(count_people_per_year(begin)/1000)
        amounts["year"].append(begin)
        begin = begin+jump_years

    plt.figure(figsize=(12, 6))
    plt.plot(amounts['year'], amounts['total'], color='skyblue', zorder=2, alpha=0.5, linestyle = 'dashed')
    plt.xlabel('Anno')
    plt.ylabel('Cittadini (in migliaia)')
    plt.xticks(amounts['year'])
    plt.tight_layout()
    plt.show()

sequence(starting_year, ending_year, jump_years)
