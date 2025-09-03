import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("travel_pricing_data.csv")  # Features: season, destination, demand, availability
X = df[["season", "destination", "demand", "availability"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = XGBRegressor()
model.fit(X_train, y_train)

def predict_price(input_data):
    return model.predict(pd.DataFrame([input_data]))

# Example
print(predict_price({"season": "Summer", "destination": "Paris", "demand": 0.8, "availability": 0.6}))
