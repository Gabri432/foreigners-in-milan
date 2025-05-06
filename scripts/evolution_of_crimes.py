import pandas as pd
import matplotlib.pyplot as plt

total_crimes = pd.read_csv("datasets/Reati_totali_serie_storica.csv", delimiter=',')
people = pd.read_csv('datasets/ds75_stranieri_sesso_citt.csv', sep=';', index_col=False)

year = 2023
start_year = 2004

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

    return amounts

def get_crimes_per_year(starting_year, last_year):
    amounts = {'year': [], 'total':[]}
    foreigners_amount = sequence(starting_year, last_year, 1)
    while starting_year <= last_year:
        crimes_this_year = total_crimes[total_crimes["anno_rilevamento_reato"].eq(starting_year) &
                                              total_crimes["Reati_denunciati_tipologia"].eq("Reati totale")] 
        crimes_sum = crimes_this_year.groupby('Reati_denunciati_tipologia')['reati_denunciati'].sum()
        total = 0
        for crimes in crimes_sum:
            total+=int(crimes)
        
        amounts["total"].append(total/1000)
        amounts["year"].append(starting_year)
        starting_year = starting_year+1

    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()

    ax1.set_xlabel("Anno")
    ax1.plot(amounts['year'], amounts['total'], color='skyblue', zorder=2, alpha=0.8, label="Crimini")
    ax2.plot(foreigners_amount['year'], foreigners_amount['total'], color='blue', zorder=2, alpha=0.7, label="Popolazione straniera")
    ax1.set_ylabel("Crimini (in migliaia)")
    ax2.set_ylabel("Popolazione straniera (in migliaia)")

    fig.suptitle("Andamento popolazione stranieria e criminalità", fontsize=20)
    fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    #plt.figure(figsize=(12, 6))
    #plt.plot(amounts['year'], amounts['total'], color='skyblue', zorder=2, alpha=0.7)
    #plt.xlabel('Anno')
    plt.xticks(amounts['year'])
    #plt.ylabel('Crimini (in migliaia)')
    #plt.tight_layout()
    plt.show()

get_crimes_per_year(start_year, year)
