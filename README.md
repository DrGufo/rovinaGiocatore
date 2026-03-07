# Rovina del Giocatore

Simulazione della **rovina del giocatore d'azzardo** con due approcci:

- `main.py`: simulazione singola, passo-passo, con output testuale.
- `main.ipynb`: analisi Monte Carlo con grafici e stime statistiche.

## Obiettivo del progetto

Studiare il comportamento del capitale di un giocatore che scommette una somma fissa ad ogni partita, fino a uno di questi eventi:

- **Rovina**: il capitale arriva a `0`.
- **Successo**: il capitale raggiunge una soglia massima `CMax`.
- **Stop tecnico**: viene raggiunto il numero massimo di partite.

## Struttura del progetto

```text
rovinaGiocatore/
	main.py       # simulazione singola da terminale
	main.ipynb    # simulazioni Monte Carlo + analisi e grafici
	README.md
```

## Requisiti

Python `3.10+` consigliato.

Librerie usate nel notebook:

- `numpy`
- `pandas`
- `plotly`
- `statsmodels`

Installazione dipendenze:

```bash
pip install numpy pandas plotly statsmodels
```

## Come eseguire

### 1) Script Python (`main.py`)

Esegue una simulazione singola con log di ogni partita.

```bash
python main.py
```

Nel file puoi modificare i parametri principali:

- `C_0`: capitale iniziale
- `C_Max`: capitale obiettivo
- `delta`: puntata fissa per partita (nel codice e indicata come `δ`)
- `P_max`: numero massimo di partite

### 2) Notebook (`main.ipynb`)

Apri il notebook in VS Code o Jupyter e lancia le celle in ordine.

Nel notebook trovi:

- simulazione Monte Carlo su piu giocatori;
- stima empirica della probabilita di rovina;
- confronto con probabilita teorica media;
- tempi attesi di rovina/successo;
- istogrammi e scatter plot con regressione lineare.

## Note metodologiche

- In `main.py` la probabilita di vincita viene randomizzata ad ogni partita.
- In `main.ipynb` la probabilita `p` viene randomizzata ad ogni simulazione Monte Carlo.
- I risultati possono cambiare tra diverse esecuzioni a causa della componente casuale.

## Miglioramenti possibili

- Impostare un `seed` per rendere i risultati riproducibili.
- Salvare grafici e metriche in file (`.csv`, `.png`, `.html`).
- Aggiungere test automatici sulle funzioni di simulazione.
- Separare la logica in moduli Python riutilizzabili.