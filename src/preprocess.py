import pandas as pd

def load_and_preprocess(data_path):
    df = pd.read_csv(data_path)
    # Example preprocessing: drop duplicates, normalize features, etc.
    df = df.drop_duplicates()
    # More preprocessing steps can be added here
    return df

if __name__ == "__main__":
    df = load_and_preprocess("data/creditcard.csv")
    print(df.head())