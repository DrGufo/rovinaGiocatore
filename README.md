# Rovina del Giocatore

Questo progetto presenta una simulazione del problema della **rovina del giocatore d'azzardo**, sviluppata con due modalita complementari:

- `main.py`: esecuzione di una simulazione singola con tracciamento testuale dell'evoluzione del capitale.
- `main.ipynb`: studio Monte Carlo su piu simulazioni, con analisi statistica e visualizzazioni.

## Finalita

L'obiettivo e analizzare l'andamento del capitale di un giocatore che effettua puntate a importo fisso, fino al verificarsi di una delle seguenti condizioni:

- **Rovina**: il capitale raggiunge il valore `0`.
- **Successo**: il capitale raggiunge la soglia `CMax`.
- **Arresto della simulazione**: viene raggiunto il limite massimo di partite prefissato.

## Struttura del repository

```text
rovinaGiocatore/
  main.py
  main.ipynb
  README.md
```

## Requisiti

Si raccomanda l'utilizzo di Python `3.10` o versione successiva.

Dipendenze principali:

- `numpy`
- `pandas`
- `plotly`
- `statsmodels`

Installazione:

```bash
pip install numpy pandas plotly statsmodels
```

## Esecuzione

### Script Python

Per eseguire la simulazione singola da terminale:

```bash
python main.py
```

Parametri principali configurabili nel file:

- `C_0`: capitale iniziale.
- `C_Max`: soglia di capitale per il successo.
- `δ` (delta): importo fisso scommesso a ogni partita.
- `P_max`: numero massimo di partite consentite.

### Notebook

Aprire `main.ipynb` in VS Code o Jupyter ed eseguire le celle in sequenza.

Il notebook include:

- simulazione Monte Carlo su un insieme di giocatori;
- stima empirica della probabilita di rovina;
- confronto con la probabilita teorica media;
- stima dei tempi medi di rovina e successo;
- analisi grafica (distribuzioni, scatter plot, regressione lineare).

## Note metodologiche

- In `main.py` la probabilita di vincita viene campionata a ogni partita.
- In `main.ipynb` la probabilita `p` viene campionata a ogni simulazione Monte Carlo.
- I risultati possono variare tra esecuzioni diverse, in quanto il processo e stocastico.

## Sviluppi futuri

- introdurre un `seed` per garantire la riproducibilita sperimentale;
- esportare risultati e grafici in formati standard (`.csv`, `.png`, `.html`);
- aggiungere test automatici per le funzioni principali;
- organizzare il codice in moduli Python separati per favorire riuso e manutenibilita.