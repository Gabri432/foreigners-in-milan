import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

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
        amounts["total"].append(count_people_per_year(begin))
        amounts["year"].append(begin)
        begin = begin+jump_years

    #a = pd.DataFrame(amounts)
    plt.figure(figsize=(12, 6))
    plt.bar(amounts['year'], amounts['total'], color='skyblue')
    #a.plot(legend=False)
    plt.xlabel('Year')
    plt.ylabel('Citizens')
    plt.title(f'Foreigners between {starting_year} and {ending_year} in Milan')
    plt.tight_layout()
    plt.show()

sequence(starting_year, ending_year, jump_years)
