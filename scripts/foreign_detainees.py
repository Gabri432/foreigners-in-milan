import pandas as pd
import matplotlib.pyplot as plt

total_detainees = pd.read_csv("datasets/detenuti_stranieri_2010_2020.csv", delimiter=',')

year = 2020
start_year = 2010

def get_detainees_per_year(starting_year, last_year):
    amounts = {'year': [], 'total':[]}
    while starting_year <= last_year:
        detainees_this_year = total_detainees[total_detainees["anno_rilevazione_detenuti"].eq(starting_year) &
                                              total_detainees["indicatori"].eq("detenuti stranieri totale")] 
        detainees_sum = detainees_this_year.groupby('indicatori')['detenuti'].sum()
        total = 0
        for detainees in detainees_sum:
            total+=detainees
        
        amounts["total"].append(total)
        amounts["year"].append(starting_year)
        starting_year = starting_year+1
    
    plt.figure(figsize=(12, 6))
    #plt.bar(amounts['year'], amounts['total'], color='skyblue', zorder=2, alpha=0.5)
    plt.plot(amounts['year'], amounts['total'], color='skyblue', zorder=2, alpha=0.8)
    plt.xlabel('Anno')
    plt.ylabel('Detenuti Stranieri')
    plt.tight_layout()
    plt.show()

get_detainees_per_year(start_year, year)
