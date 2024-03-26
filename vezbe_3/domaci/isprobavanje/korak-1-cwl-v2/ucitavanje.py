import sys
import pandas as pd

dataset = sys.argv[1]
data = pd.read_csv(dataset)

# popunjavanje nedostajucih vrednosti (prosecna za tu kolonu)
data = data.fillna(data.mean())

# uklanjanje outlier-a

# upisivanje filtriranih podataka
data.to_csv('output.csv')