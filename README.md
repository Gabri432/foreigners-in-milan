# Foreigners of Milan
[See the Italian translation](https://github.com/Gabri432/foreigners-in-milan/blob/master/README.it.md)

Milan is often considered as an international city, but how international is it really?

In this project we are going to track exactly how much. Specifically, we will find out the number of foreigner residents, their origins, their distribution within the city, and their quality of life during the last decades.

The goal is to give an idea of the actual impact of foreigners in Milan.

## Resources (in Italian)
- [Foreigners: residents per nationality and gender (1987-2024)](https://www.dati.gov.it/view-dataset/dataset?id=936fe601-0f47-43d8-9642-bdaf064f57f3)
- [Calculated/Estimated population - historical series since 1880](https://www.dati.gov.it/view-dataset/dataset?id=8d6d9168-2128-416f-910b-e76b29cdbf5c)
- [Population: residents per nationality and city zone (1999-2024)](https://www.dati.gov.it/view-dataset/dataset?id=8f2dd42b-23a5-439d-ab56-be02295f4290)

## Notes
- This project used Python 3.12.4, pip 24, plotly 6.0.1, pandas 2.2.3, numpy 2.2.3, matplotlib 3.10.1;
- This project was developped using Visual Studio Code;
- The original dataset (csv file) "Population: residents per nationality and city zone (1999-2024)" is about 144 Mb, exceeding the limit of Github of 100 Mb. Therefore I have used a simplified dataset to fit within such contraints.
- In the simplified dataset, most neighborhood names were simplified to match [this list](https://it.wikipedia.org/wiki/Categoria:Quartieri_di_Milano) of neiborhood.