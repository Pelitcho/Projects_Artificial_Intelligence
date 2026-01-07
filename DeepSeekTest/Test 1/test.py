import pandas as pd
import numpy as np

# Génération des données
np.random.seed(42)
n_customers = 1000

data = {
    'customer_id': range(n_customers),
    'age': np.random.normal(45, 15, n_customers).astype(int),
    'annual_income': np.random.lognormal(mean=4.0, sigma=0.5, size=n_customers),
    'spending_score': np.random.randint(1, 101, n_customers),
    'membership_years': np.random.exponential(5, n_customers).astype(int),
    'churn': np.random.binomial(1, 0.2, n_customers)
}

df = pd.DataFrame(data)
df['age'] = np.clip(df['age'], 18, 80)
df['annual_income'] = np.round(df['annual_income'] * 10, 2)
df['membership_years'] = np.clip(df['membership_years'], 0, 20)