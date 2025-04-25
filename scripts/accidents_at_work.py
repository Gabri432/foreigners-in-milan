import pandas as pd
import matplotlib.pyplot as plt

total_accidents = pd.read_csv("datasets/infortuni_sul_lavoro.csv", delimiter=',')

end_year = 2022
start_year = 2010

def count_accidents_per_year(year):
    accidents_per_year = total_accidents[total_accidents['Anno'].eq(year)]

    of_foreigners = accidents_per_year[accidents_per_year["Cittadinanza"].eq("Cittadinanza - Extra Unione Europea")]
    total_for_foreigners = of_foreigners.groupby('Cittadinanza')['infortuni'].sum().iloc[0]

    of_italians = accidents_per_year[accidents_per_year["Cittadinanza"].eq("Cittadinanza - Italiani")]
    total_for_italians = of_italians.groupby('Cittadinanza')['infortuni'].sum().iloc[0]

    of_europeans = accidents_per_year[accidents_per_year["Cittadinanza"].eq("Cittadinanza - Unione Europea ( esclusa Italia )")]
    total_for_europeans = of_europeans.groupby('Cittadinanza')['infortuni'].sum().iloc[0]

    return {'foreigners': total_for_foreigners + total_for_europeans, 'italians': total_for_italians}


def sequence(starting_year, ending_year):
    begin = starting_year
    amounts = {'year': [], 'total':{'foreigners':[], 'italians':[]}}
    while begin <= ending_year:
        details = count_accidents_per_year(begin)
        amounts["total"]["foreigners"].append(details["foreigners"])
        amounts["total"]["italians"].append(details["italians"])
        amounts["year"].append(begin)
        begin = begin+1

    return amounts

def display_data(starting_year, ending_year):
    amounts = sequence(starting_year, ending_year)


    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()

    ax1.set_xlabel("Anno")
    ax1.plot(amounts['year'], amounts['total']["italians"], color='skyblue', zorder=2, alpha=0.7, linestyle = 'dashed', label="Infortuni d'italiani")
    ax2.plot(amounts['year'], amounts['total']["foreigners"], color='blue', zorder=2, alpha=0.7, linestyle = 'dashed', label="Infortuni di stranieri")
    ax1.set_ylabel("Numero infortuni")

    fig.suptitle("Andamento infortuni sul lavoro (2010-2022)", fontsize=20)
    fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    plt.xticks(amounts['year'])
    y_labels = [2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000, 22500]
    ax1.set_yticks(y_labels)
    ax2.set_yticks(y_labels)
    plt.show()

display_data(start_year, end_year)
