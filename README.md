# Foreigners of Milan
[See the Italian translation](https://github.com/Gabri432/foreigners-in-milan/blob/master/README.it.md)

Milan is often considered as an international city, but how international is it really?

In this project we are going to track exactly how much. Specifically, we will find out the number of foreigner residents, their origins, their distribution within the city, and their quality of life during the last decades.

The goal is to give an idea of the actual impact of foreigners in Milan.

## Resources (in Italian)
- [Foreigners: residents per nationality and gender (1987-2024)](https://www.dati.gov.it/view-dataset/dataset?id=936fe601-0f47-43d8-9642-bdaf064f57f3)
- [Calculated/Estimated population - historical series since 1880](https://www.dati.gov.it/view-dataset/dataset?id=8d6d9168-2128-416f-910b-e76b29cdbf5c)
- [Population: residents per nationality and city zone (1999-2024)](https://www.dati.gov.it/view-dataset/dataset?id=8f2dd42b-23a5-439d-ab56-be02295f4290)
- [CURRENT local identity nuclei (NIL) - PGT 2030](https://www.dati.gov.it/view-dataset/dataset?id=c46c6fd8-93d0-4a19-94f2-fc226219b6b3)
- [High school students per nationality (2007-2024)](https://sisi.comune.milano.it/mistat/extensions/MiStat/MiStat_Analisi.html?IdFD_MenuNavigazione=qry_scuolesup_ac_alunni_cittad)
- [Crimes reported to the judicial authorities by the police force (2004-2023)](https://dati.comune.milano.it/dataset/ds564-reati-denunciati-all-autorita-giudiziaria-dalla-forze-di-polizia)
- [Inail: accidents at work reported by companies - Breakdown by citizenship](https://dati.comune.milano.it/dataset/ds1684-inail-infortuni-sul-lavoro-denunciati-dalle-aziende-suddivisione-per-cittadinanza-2010-avanti)

## Project structure
- Main folder

- datasets (folder)
    - ds75_stranieri_sesso_citt.csv
    - ds1494_popolazione-calcolata-dal-1880.csv
    - simplified_dataset.csv
    - milan.geojson
    - Alunni_Scuole_Secondarie_di_Secondo_Grado_per_cittadinanza_(2007_08-2023_24).csv
    - detenuti_stranieri_2010_2020.csv
    - infortuni_sul_lavoro.csv
    - Reati totali serie storica.csv

- graphs (folder)
    - [Amount of foreigners within the population](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Amount%20of%20foreigners%20within%20the%20population.png)
    - [Foreigners in 2024](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Foreigners%20in%202024.png)
    - [Foreigners between 2004 and 2024](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Foreigners%20between%202004%20and%202024%20in%20Milan.png)
    - [global_plot (Global Distribution of foreigners)](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/global_plot.png)
    - [Pie chart of nationalities above 10k](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Pie%20chart%20of%20nationalities%20above%2010k.png)
    - [Distribution of foreigners within Milan in 2024](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Distribution%20of%20Foreigners%20in%20Milan%202024.png)
    - [Ratio foreigners Italians 2004](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Ratio%20foreigners%20Italians%202004.png)
    - [Ratio foreigners Italians 2024](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Ratio%20foreigners%20Italians%202024.png)
    - [Foreign Students 2024](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Foreign%20Students%202024.png)
    - [Foreign men and women pie chart](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Foreign%20men%20and%20women%20pie%20chart.png)
    - [Foreigners and Crimes](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Foreigners%20and%20Crimes.png)
    - [Evolution of foreign detainees](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Evolution%20of%20foreign%20detainees.png)
    - [Comparison accidents at work for foreigners and Italians](https://github.com/Gabri432/foreigners-in-milan/blob/master/graphs/Comparison%20accidents%20at%20work%20for%20foreigners%20and%20Italians.png)

- .gitignore
- [Presentazione Visualizzazione Scientifica.pdf](https://github.com/Gabri432/foreigners-in-milan/blob/master/Presentazione%20Visualizzazione%20Scientifica.pdf)
- scripts (folder)
    - [global_distribution.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/global_distribution.py)
    - [ratio_foreigners_pop.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/ratio_foreigners_pop.py)
    - [pie_chart_with_legend.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/pie_chart_with_legend.py)
    - [yearly_foreigners.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/yearly_foreigners.py)
    - [frequency_of_nationalities.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/frequency_of_nationalities.py)
    - [foreigners_per_age.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/foreigners_per_age.py)
    - [pie_chart_for_ages.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/pie_chart_for_ages.py)
    - [high_school_foreigners.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/high_school_foreigners.py)
    - [foreign_detainees.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/foreign_detainees.py)
    - [evolution_of_crimes.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/evolution_of_crimes.py)
    - [foreigners_by_gender.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/foreigners_by_gender.py)
    - [accidents_at_work.py](https://github.com/Gabri432/foreigners-in-milan/blob/master/scripts/accidents_at_work.py)

## Notes
- This project used Python 3.12.4, pip 24, plotly 6.0.1, pandas 2.2.3, numpy 2.2.3, matplotlib 3.10.1;
- This project was developped using Visual Studio Code;
- The original dataset (csv file) "Population: residents per nationality and city zone (1999-2024)" is about 144 Mb, exceeding the limit of Github of 100 Mb. Therefore on github it is present a simplified dataset to fit within such contraints.