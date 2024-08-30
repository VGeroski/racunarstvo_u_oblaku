import os
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Učitaj promenljive iz okruženja
csv_file = os.environ['CSV_FILE']
ciljna_kolona_naziv = os.environ['TARGET_COLUMN']
k = int(os.environ['K'])
fold_index = int(os.environ['FOLD_INDEX'])

# lokalno testiranje
# csv_file = 'HousingData.csv'
# ciljna_kolona_naziv = 'MEDV'
# k = 5
# fold_index = 1

# Učitavanje podataka iz CSV fajla
data = pd.read_csv(csv_file)

# popunjavanje nedostajucih vrednosti (prosecna za tu kolonu)
data = data.fillna(data.mean())

X = data.drop(columns=[ciljna_kolona_naziv])
y = data[ciljna_kolona_naziv]

# Inicijalizacija k-fold cross validacije
kf = KFold(n_splits=k, shuffle=True, random_state=42)
model = LinearRegression()

# Izvršavanje jednog fold-a cross validacije
folds = list(kf.split(X))
train_index, test_index = folds[fold_index]

X_train, X_test = X.iloc[train_index], X.iloc[test_index]
y_train, y_test = y.iloc[train_index], y.iloc[test_index]

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Prikaz rezultata za trenutni fold
print(f'Fold {fold_index + 1}/{k} - RMSE: {rmse}')
