import pandas as pd
import matplotlib.pyplot as plt

total_accidents = pd.read_csv("datasets/infortuni_sul_lavoro.csv", delimiter=',')

employment_rates = pd.read_csv("datasets/Tasso_di_occupazione.csv", delimiter=',')
unemployment_rates = pd.read_csv("datasets/Tasso_di_disoccupazione.csv", delimiter=',')

end_year = 2022
start_year = 2004

def employment_and_unemployment_rates_per_year(year):
    employment_rate_per_year = employment_rates[employment_rates['Anno'].eq(year)]
    unemployment_rate_per_year = unemployment_rates[unemployment_rates['Anno'].eq(year)]

    return {"employment": employment_rate_per_year["Milano"], "unemployment": unemployment_rate_per_year["Milano"]}

def sequence(starting_year, ending_year):
    begin = starting_year
    amounts = {'year': [], 'total':{'employment':[], 'unemployment':[]}}
    while begin <= ending_year:
        details = employment_and_unemployment_rates_per_year(begin)
        amounts["total"]["employment"].append(details["employment"])
        amounts["total"]["unemployment"].append(details["unemployment"])
        amounts["year"].append(begin)
        begin = begin+1

    return amounts 

def display_data(starting_year, ending_year):
    amounts = sequence(starting_year, ending_year)


    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()

    ax1.set_xlabel("Anno")
    ax1.plot(amounts['year'], amounts['total']["employment"], color='skyblue', zorder=2, alpha=0.8, label="Occupazione")
    ax2.plot(amounts['year'], amounts['total']["unemployment"], color='blue', zorder=2, alpha=0.7, label="Disoccupazione")
    ax1.set_ylabel("Percentuali occupazione e disoccupazione")

    fig.suptitle("Andamento occupazione e disoccupazione (2004-2022)", fontsize=20)
    fig.legend(loc="upper left", bbox_to_anchor=(0, 1), bbox_transform=ax2.transAxes)
    plt.xticks(amounts['year'])
    y_labels = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
    ax1.set_yticks(y_labels)
    ax2.set_yticks(y_labels)
    plt.show()

display_data(start_year, end_year)
