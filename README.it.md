# Stranieri di Milano
[See the English translation](https://github.com/Gabri432/foreigners-in-milan/blob/master/README.md)

Milano viene spesso considerata come una città internazionale, ma quanto lo è veramente?

In questo progetto noi cerchiamo di tenere traccia di esattamente quanto. Nello specifico, andremo ad analizzare il numero di stranieri, la loro origine, la loro distribuzione nella città, e la qualità della loro vita nel corso degli ultimi decenni.

L'obiettivo è quello di dare un'idea di quella che è la vera portata degli stranieri a Milano.

## Risorse (in italiano)
- [Stranieri: residenti per cittadinanza e genere (1987-2024)](https://www.dati.gov.it/view-dataset/dataset?id=936fe601-0f47-43d8-9642-bdaf064f57f3)
- [Popolazione calcolata - serie storica dal 1880](https://www.dati.gov.it/view-dataset/dataset?id=8d6d9168-2128-416f-910b-e76b29cdbf5c)
- [Popolazione: residenti per cittadinanza e quartiere (1999-2024)](https://www.dati.gov.it/view-dataset/dataset?id=8f2dd42b-23a5-439d-ab56-be02295f4290)
- [Nuclei d'Identità Locale (NIL) VIGENTI - PGT 2030](https://www.dati.gov.it/view-dataset/dataset?id=c46c6fd8-93d0-4a19-94f2-fc226219b6b3)

## Struttura del progetto
- Cartella principale

- datasets (cartella)
    - ds75_stranieri_sesso_citt.csv
    - ds1494_popolazione-calcolata-dal-1880.csv
    - simplified_dataset.csv

- graphs (cartella)
    - [Amount of foreigners within the population](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Amount%20of%20foreigners%20within%20the%20population.png)
    - [Foreigners in 2024](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Foreigners%20in%202024.png)
    - [Foreigners between 2004 and 2024](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Foreigners%20between%202004%20and%202024%20in%20Milan.png)
    - [global_plot (Global Distribution of foreigners)](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/global_plot.png)
    - [Pie chart of nationalities above 10k](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Pie%20chart%20of%20nationalities%20above%2010k.png)
    - [Distribution of foreigners within Milan in 2024](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Distribution%20of%20Foreigners%20in%20Milan%202024.png)

- .gitignore
- [presentazione.pdf](https://github.com/Gabri432/foreigners-in-milan/blob/master/presentazione.pdf)
- [global_distribution.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/global_distribution.py)
- [ratio_foreigners_pop.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/ratio_foreigners_pop.py)
- [pie_chart_with_legend.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/pie_chart_with_legend.py)
- [yearly_foreigners.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/yearly_foreigners.py)
- [frequency_of_nationalities.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/frequency_of_nationalities.py)

## Note
- Questo progetto ha usato Python 3.12.4, pip 24, plotly 6.0.1, pandas 2.2.3, numpy 2.2.3, matplotlib 3.10.1;
- Questo progetto è stato sviluppato usando Visual Studio Code;
- Il dataset originale (file csv) "Popolazione: residenti per cittadinanza e quartiere (1999-2024)" è di circa 144 Mb, superiore al limite di Github di 100 Mb. Dunque ho usato un dataset semplificato per non infrangere questo limite.
- Nel dataset semplificato, i nomi di molti quartieri sono stati semplificati per essere in linea con [questa lista](https://it.wikipedia.org/wiki/Categoria:Quartieri_di_Milano) di quartieri.