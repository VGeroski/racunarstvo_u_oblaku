import sys
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt

# Učitaj argumente
train_file = sys.argv[2]
test_file = sys.argv[3]
target_column = sys.argv[4]  # Ciljna kolona kao argument

# Učitaj podatke za treniranje i testiranje
train_data = pd.read_csv(train_file)
test_data = pd.read_csv(test_file)

# Odvoji ulazne i ciljnu varijablu na osnovu naziva ciljne kolone
X_train = train_data.drop(columns=[target_column])
y_train = train_data[target_column]

X_test = test_data.drop(columns=[target_column])
y_test = test_data[target_column]

# Treniraj model
model = LinearRegression()
model.fit(X_train, y_train)

# Predvidi test set i izračunaj RMSE
y_pred = model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, y_pred))

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
    
# Sačuvaj metriku performansi
with open("performance.txt", "w") as f:
    f.write(f"RMSE: {rmse}\n")

print(f"RMSE: {rmse}")
