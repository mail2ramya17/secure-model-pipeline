import os, pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200).fit(X, y)
os.makedirs("model", exist_ok=True)
pickle.dump(model, open("model/model.pkl", "wb"))
print("saved model/model.pkl")
