# Credit Card Fraud Detection

Detect fraudulent credit card transactions using machine learning.

## Overview

This project aims to build a machine learning model that can predict whether a credit card transaction is fraudulent based on transaction data. 

Uses the [Kaggle Credit Card Fraud Detection dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud) and demonstrates best practices for preprocessing, model building, and evaluation.

## Project Structure

```
credit-card-fraud-detection/
├── data/              # Dataset goes here
├── notebooks/         # Jupyter notebooks for EDA and experimentation
├── src/               # Python scripts for preprocessing, training, and prediction
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── .gitignore         # Files/folders to ignore in version control
```

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset**

   Download `creditcard.csv` from [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud) and place it in the `data/` folder.

4. **Run exploratory analysis**

   Open and run `notebooks/eda.ipynb` to explore and understand the data.

5. **Train the model**

   Run the training script:
   ```bash
   python src/train_model.py
   ```

## Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Fraud detection using machine learning models (e.g., Logistic Regression, Random Forest, XGBoost)
- Model evaluation with metrics suitable for imbalanced data (Precision, Recall, ROC-AUC)
- (Optional) Deployment script for predictions

## Requirements

See `requirements.txt` for Python dependencies.

## License

MIT License