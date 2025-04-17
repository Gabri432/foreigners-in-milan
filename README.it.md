# Stranieri di Milano
[See the English translation](https://github.com/Gabri432/foreigners-in-milan/blob/master/README.md)

Milano viene spesso considerata come una città internazionale, ma quanto lo è veramente?

In questo progetto noi cerchiamo di tenere traccia di esattamente quanto. Nello specifico, andremo ad analizzare il numero di stranieri, la loro origine, la loro distribuzione nella città, e la qualità della loro vita nel corso degli ultimi decenni.

L'obiettivo è quello di dare un'idea di quella che è la vera portata degli stranieri a Milano.

## Risorse (in italiano)
- [Stranieri: residenti per cittadinanza e genere (1987-2024)](https://www.dati.gov.it/view-dataset/dataset?id=936fe601-0f47-43d8-9642-bdaf064f57f3)
- [Popolazione calcolata - serie storica dal 1880](https://www.dati.gov.it/view-dataset/dataset?id=8d6d9168-2128-416f-910b-e76b29cdbf5c)
- [Popolazione: residenti per cittadinanza e quartiere (1999-2024)](https://www.dati.gov.it/view-dataset/dataset?id=8f2dd42b-23a5-439d-ab56-be02295f4290)

## Note
- Questo progetto ha usato Python 3.12.4, pip 24, plotly 6.0.1, pandas 2.2.3, numpy 2.2.3, matplotlib 3.10.1;
- Questo progetto è stato sviluppato usando Visual Studio Code;
- Il dataset originale (file csv) "Popolazione: residenti per cittadinanza e quartiere (1999-2024)" è di circa 144 Mb, superiore al limite di Github di 100 Mb. Dunque ho usato un dataset semplificato per non infrangere questo limite.
- Nel dataset semplificato, i nomi di molti quartieri sono stati semplificati per essere in linea con [questa lista](https://it.wikipedia.org/wiki/Categoria:Quartieri_di_Milano) di quartieri.