# Sales Forecasting | End-to-End Machine Learning Pipeline



##  Project Overview

A complete machine learning project focused on predicting future revenue from sales transaction data. 



**Key Result**: Gradient Boosting model achieving **R² = 0.957** (explaining 95.7% of revenue variance).



##  Technical Process



### 1. Data Preparation & Feature Engineering

- **Data Cleaning**: Handled missing values and standardized data formats

- **Feature Creation**: Engineered temporal features (Year, Month) and business metrics (Revenue = Price × Quantity)

- **Categorical Encoding**: Applied and compared Label Encoding vs. One-Hot Encoding techniques



### 2. Model Development & Benchmarking

Systematically implemented and evaluated 5 regression algorithms:

- Linear Regression (Baseline)

- Decision Tree Regressor

- Random Forest Regressor

- **Gradient Boosting Regressor** (Best performer)

- AdaBoost Regressor



### 3. Model Optimization & Evaluation

- **Hyperparameter Tuning**: GridSearchCV for optimal Gradient Boosting parameters

- **Cross-Validation**: 5-fold CV ensuring robust performance estimation

- **Multi-Metric Evaluation**: R², Mean Squared Error (MSE), Mean Absolute Error (MAE)

- **Feature Importance Analysis**: Identified key drivers of revenue predictions



##  Key Findings & Insights

- **Best Model**: Optimized GradientBoostingRegressor with R² = 0.957

- **Critical Features**: Price and quantity were strongest predictors, with additional value from temporal patterns

- **Algorithm Insight**: Ensemble methods (Random Forest, Gradient Boosting) significantly outperformed simpler linear models on this non-linear sales data



##  Tech Stack

- **Languages**: Python

- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

- **Tools**: Jupyter Notebook, Git
