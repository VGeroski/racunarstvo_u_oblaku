from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle

app = Flask(__name__)

# Putanja do CSV fajla i modela
CSV_PATH = "/mnt/data/wine_dataset.csv"  # /mnt/data u PersistanVolume
MODEL_PATH = "/mnt/data/wine_model.pkl"  # Putanja do sacuvanog modela

def train_model(activation, solver):
    # Učitavanje podataka
    df = pd.read_csv(CSV_PATH)
    
    # Iz skupa za treniranje izbacujemo type kolonu (koja je ciljna)
    X = df.drop('type', axis=1)
    y = df['type']

    # Podela na trening i test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # pre-procesiranje
    sc = StandardScaler()

    scaler = sc.fit(X_train)
    trainX_scaled = scaler.transform(X_train)
    testX_scaled = scaler.transform(X_test)

    # Definisanje modela
    model = MLPClassifier(
        activation=activation,
        solver=solver,
        max_iter=1000
    )

    # Treniranje modela
    model.fit(trainX_scaled, y_train)

    # Predikcije na test setu
    y_pred = model.predict(testX_scaled)

    # Metričke performanse
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')

    # Čuvanje modela
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)

    return precision, recall, f1

@app.route('/train', methods=['POST'])
def train():
    data = request.get_json()

    # Dohvatanje parametara iz POST zahteva
    activation = data.get('activation', 'relu')
    solver = data.get('solver', 'adam')

    # Treniranje modela
    precision, recall, f1 = train_model(activation, solver)

    # Povratak rezultata
    return jsonify({'precision': precision, 'recall': recall, 'f1_score': f1})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Učitavanje modela
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

    # Ulazni podaci treba da odgovaraju X
    X_new = pd.DataFrame([data['features']])

    # Predikcija
    prediction = model.predict(X_new)

    # Povratak predikcije
    # napomena: ne moze direktno da se serijalizuje u json, 
    # pa je numpy niz potrebno pretvoriti u listu, a onda uzeti element
    # (postoji samo jedan izlaz)
    return jsonify({'prediction': prediction.tolist()[0]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

