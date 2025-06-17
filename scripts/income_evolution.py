import pandas as pd
import matplotlib.pyplot as plt

incomes = pd.read_csv("datasets/classi_reddito_complessivo.csv", delimiter=',')

employment_rates = pd.read_csv("datasets/Tasso_di_occupazione.csv", delimiter=',')
unemployment_rates = pd.read_csv("datasets/Tasso_di_disoccupazione.csv", delimiter=',')

end_year = 2022
start_year = 2008

def income_ranges_per_year(year):
    this_year_incomes = incomes[incomes['Anno'].eq(year)]
    below_10k = this_year_incomes[this_year_incomes["Classi di reddito complessivo in euro"].eq("da 0 a 10.000")]
    between_10k_15k = this_year_incomes[this_year_incomes["Classi di reddito complessivo in euro"].eq("da 10.000 a 15.000")]
    between_15k_26k = this_year_incomes[this_year_incomes["Classi di reddito complessivo in euro"].eq("da 15.000 a 26.000")]
    between_26k_55k = this_year_incomes[this_year_incomes["Classi di reddito complessivo in euro"].eq("da 26.000 a 55.000")]
    between_55k_75k = this_year_incomes[this_year_incomes["Classi di reddito complessivo in euro"].eq("da 55.000 a 75.000")]
    between_75k_120k = this_year_incomes[this_year_incomes["Classi di reddito complessivo in euro"].eq("da 75.000 a 120.000")]
    above_120k = this_year_incomes[this_year_incomes["Classi di reddito complessivo in euro"].eq("oltre 120.000")]
    return {"<10k":below_10k, "10-15k":between_10k_15k, "15-26k":between_15k_26k, "26-55k":between_26k_55k, "55-75k":between_55k_75k,
            "75-120k":between_75k_120k, ">120k":above_120k}

def sequence(starting_year, ending_year):
    begin = starting_year
    amounts = {'year': [], 'total':{"<10k":[], "10-15k":[], "15-26k":[], "26-55k":[], "55-75k":[], "75-120k":[], ">120k":[]}}
    while begin <= ending_year:
        details = income_ranges_per_year(begin)
        amounts["total"]["<10k"].append(details["<10k"].groupby("Classi di reddito complessivo in euro")["Frequenza persone fisiche"].sum())
        amounts["total"]["10-15k"].append(details["10-15k"].groupby("Classi di reddito complessivo in euro")["Frequenza persone fisiche"].sum())
        amounts["total"]["15-26k"].append(details["15-26k"].groupby("Classi di reddito complessivo in euro")["Frequenza persone fisiche"].sum())
        amounts["total"]["26-55k"].append(details["26-55k"].groupby("Classi di reddito complessivo in euro")["Frequenza persone fisiche"].sum())
        amounts["total"]["55-75k"].append(details["55-75k"].groupby("Classi di reddito complessivo in euro")["Frequenza persone fisiche"].sum())
        amounts["total"]["75-120k"].append(details["75-120k"].groupby("Classi di reddito complessivo in euro")["Frequenza persone fisiche"].sum())
        amounts["total"][">120k"].append(details[">120k"].groupby("Classi di reddito complessivo in euro")["Frequenza persone fisiche"].sum())
        amounts["year"].append(begin)
        begin = begin+1

    return amounts 

def display_data(starting_year, ending_year):
    amounts = sequence(starting_year, ending_year)

    plt.figure(figsize=(12, 6))
    plt.xlabel("Anno")
    plt.plot(amounts['year'], amounts['total']["<10k"], color='skyblue', zorder=2, alpha=0.7, label="<10k")
    plt.plot(amounts['year'], amounts['total']["10-15k"], color='orange', zorder=2, alpha=0.7, label="10-15k")
    plt.plot(amounts['year'], amounts['total']["15-26k"], color='purple', zorder=2, alpha=0.7, label="15-26k")
    plt.plot(amounts['year'], amounts['total']["26-55k"], color='green', zorder=2, alpha=0.7, label="26-55k")
    plt.plot(amounts['year'], amounts['total']["55-75k"], color='red', zorder=2, alpha=0.7, label="55-75k")
    plt.plot(amounts['year'], amounts['total']["75-120k"], color='grey', zorder=2, alpha=0.7, label="75-120k")
    plt.plot(amounts['year'], amounts['total'][">120k"], color='blue', zorder=2, alpha=0.7, label=">120k")
    plt.ylabel("Popolazione per fascia di reddito")

    plt.title("Andamento fasce di reddito (2008-2022)", fontsize=20)
    plt.legend(loc="upper left", title="Reddito in euro")
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.xticks(amounts['year'])
    plt.show()

display_data(start_year, end_year)
