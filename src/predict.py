import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def predict(input_data):
    model = joblib.load("model.pkl")
    return model.predict(input_data)

# Example usage
if __name__ == "__main__":
    df = pd.read_csv("data/creditcard.csv")
    sample = df.drop("Class", axis=1).iloc[:5]
    print(predict(sample))
