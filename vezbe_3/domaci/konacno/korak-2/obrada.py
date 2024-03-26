import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

dataset = sys.argv[1]
ciljna_kolona_naziv = sys.argv[2]
procenat_za_trening = float(sys.argv[3])

data = pd.read_csv(dataset)

Y = data[ciljna_kolona_naziv]
X = np.array(data.drop(columns=[ciljna_kolona_naziv]))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1 - procenat_za_trening, random_state=5)
lin_model = LinearRegression()
lin_model.fit(X_train, Y_train)

# evaluacija modela za trening set
y_train_predict = lin_model.predict(X_train)
rmse = (np.sqrt(mean_squared_error(Y_train, y_train_predict)))
r2 = r2_score(Y_train, y_train_predict)

with open("out.txt", "a") as text_file:
    text_file.write("The model performance for training set\n")
    text_file.write("--------------------------------------\n")
    text_file.write('RMSE is {}'.format(rmse))
    text_file.write('\nR2 score is {}'.format(r2))
    text_file.write("\n")
    text_file.write("--------------------------------------\n")

# print("The model performance for training set")
# print("--------------------------------------")
# print('RMSE is {}'.format(rmse))
# print('R2 score is {}'.format(r2))
# print("\n")

# evaluacija modela za test set
y_test_predict = lin_model.predict(X_test)
rmse = (np.sqrt(mean_squared_error(Y_test, y_test_predict)))
r2 = r2_score(Y_test, y_test_predict)

with open("out.txt", "a") as text_file:
    text_file.write("\nThe model performance for testing set\n")
    text_file.write("--------------------------------------\n")
    text_file.write('RMSE is {}'.format(rmse))
    text_file.write('\nR2 score is {}'.format(r2))
    text_file.write("\n")
    text_file.write("--------------------------------------\n")

# print("The model performance for testing set")
# print("--------------------------------------")
# print('RMSE is {}'.format(rmse))
# print('R2 score is {}'.format(r2))

