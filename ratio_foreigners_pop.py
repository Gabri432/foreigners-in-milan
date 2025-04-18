import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)
population = pd.read_csv('datasets/ds1494_popolazione-calcolata-dal-1880.csv', sep=';', index_col=False)

starting_year = 2004
ending_year = 2024
jump_years = 1

def foreigners_pop(year):
    people_per_year = people[people['Anno'].eq(year)]
    total_per_country = people_per_year.groupby('Cittadinanza')['Residenti'].sum()
    sum = 0
    for country_pop in total_per_country:
        sum += country_pop
    
    return sum

def tot_pop(year):
    return population[population['Anno'].eq(year)]["Popolazione"].item()

def sequence(starting_year, ending_year, jump_years):
    begin = starting_year
    amounts = {'year': [], 'tot_pop':[], 'foreigners_pop':[]}
    while begin < ending_year+jump_years:
        #amounts["tot_pop"].append(round(foreigners_pop(begin) / tot_pop(begin), 3))
        amounts["tot_pop"].append((tot_pop(begin) - foreigners_pop(begin)) / 1e6)
        amounts["foreigners_pop"].append(foreigners_pop(begin) / 1e6)
        amounts["year"].append(begin)
        begin = begin+jump_years

    plt.figure(figsize=(12, 6))
    plt.grid(True, axis='y',zorder=0)
    plt.bar(amounts['year'], amounts["foreigners_pop"], color='dodgerblue', label='Stranieri', zorder=2)
    plt.bar(amounts['year'], amounts["tot_pop"], bottom=amounts["foreigners_pop"], color='skyblue', label='Italiani', zorder=2)
    #plt.bar(amounts['year'], amounts['ratio_pop'], color='skyblue')
    plt.legend(loc='upper left')
    plt.xlabel('Anno')
    plt.ylabel('Popolazione totale (in milioni)')
    #plt.title(f'Popolazione straniera rispetto a quella totale tra il {starting_year} e il {ending_year} a Milano')
    plt.tight_layout()
    plt.show()

sequence(starting_year, ending_year, jump_years)
