# Statistics and Data Analysis — Assignment

---

| Field | Details |
|-------|---------|
| **Name** | Daksh Mehrotra |
| **SAP ID** | 500125960 |
| **Roll No** | R2142231932 |
| **Batch** | 2 CCVT |
| **Repository** | `Daksh-Mehrotra-Statistics-and-Data-Analysis` |

---

## Table of Contents

1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [Datasets](#datasets)
4. [Solutions](#solutions)
5. [Evaluation Metrics](#evaluation-metrics)
6. [Dependencies](#dependencies)
7. [How to Run](#how-to-run)
8. [References](#references)

---

## Overview

This repository documents the complete submission for the Statistics and Data Analysis assignment. The work encompasses two independent problem statements, each solved using Python, addressing core areas of applied statistics: exploratory data analysis, customer segmentation, and time-series forecasting with quantitative error evaluation.

The datasets used — `Mall_Customers.csv` and `train.csv` — provide real-world context for the application of statistical techniques, including descriptive statistics, data visualisation, and predictive modelling. Model performance is assessed using industry-standard regression evaluation metrics: **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**.

---

## Repository Structure

```
Daksh-Mehrotra-Statistics-and-Data-Analysis/
│
├── Answer-1.py                   # Solution — Question 1 (EDA & Customer Analysis)
├── Answer-2.py                   # Solution — Question 2 (Forecasting & Error Evaluation)
├── Mall_Customers.csv            # Dataset — Mall customer demographics & spending
├── train.csv                     # Dataset — Training data for predictive modelling
└── README.md                     # Project documentation (this file)
```

---

## Datasets

### Mall_Customers.csv

A structured retail dataset capturing demographic attributes and spending behaviour of mall customers. This dataset is commonly employed in clustering and customer segmentation tasks to identify distinct consumer profiles for business decision-making.

| Column | Data Type | Description |
|--------|-----------|-------------|
| `CustomerID` | Integer | Unique identifier for each customer |
| `Genre` | Categorical | Gender of the customer (Male / Female) |
| `Age` | Integer | Age of the customer in years |
| `Annual Income (k$)` | Float | Annual income expressed in thousands of dollars |
| `Spending Score (1–100)` | Integer | Score (1–100) assigned based on customer spending behaviour and purchase patterns |

**Use in assignment:** Exploratory data analysis, distribution analysis, and identification of patterns across demographic and spending variables.

---

### train.csv

A time-indexed training dataset containing historical observations used to train and evaluate a forecasting model. The dataset is split into training and test subsets to simulate real-world predictive scenarios.

**Use in assignment:** Fitting a forecasting or regression model, generating future predictions, and evaluating model accuracy against held-out test values.

---

## Solutions

### Answer-1.py — Exploratory Data Analysis

This script addresses the first problem statement by performing a comprehensive statistical examination of the `Mall_Customers.csv` dataset.

**Key operations:**

- Data loading, inspection, and null value treatment
- Computation of descriptive statistics: mean, median, variance, and standard deviation
- Frequency distributions and histogram analysis for numerical features
- Visualisation of relationships between income, age, and spending score
- Identification of demographic segments within the customer base

---

### Answer-2.py — Forecasting and Model Evaluation

This script addresses the second problem statement by implementing a predictive model on `train.csv` and evaluating its accuracy using two complementary error metrics.

**Core evaluation block:**

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

mae  = mean_absolute_error(test, forecast)
rmse = np.sqrt(mean_squared_error(test, forecast))

print("MAE: ", mae)
print("RMSE:", rmse)
```

**What each metric captures:**

| Metric | Full Name | Formula | Behaviour |
|--------|-----------|---------|-----------|
| MAE | Mean Absolute Error | `mean(|actual − forecast|)` | Treats all errors equally; robust to outliers |
| RMSE | Root Mean Squared Error | `√mean((actual − forecast)²)` | Penalises large errors heavily; sensitive to outliers |

---

## Evaluation Metrics

### Mean Absolute Error (MAE)

MAE measures the average magnitude of errors between predicted and actual values, without regard to direction. Because all errors are weighted uniformly, it provides a straightforward, interpretable measure of average prediction deviation — expressed in the same units as the target variable.

A lower MAE indicates a model whose predictions are, on average, closer to the true values.

### Root Mean Squared Error (RMSE)

RMSE is derived by squaring each individual error, computing the mean, and taking the square root. The squaring operation disproportionately penalises larger errors, making RMSE the preferred metric in contexts where significant deviations are especially undesirable — such as financial forecasting or supply chain prediction.

### Interpreting Both Together

| Condition | Interpretation |
|-----------|----------------|
| RMSE ≈ MAE | Errors are uniformly distributed; no significant outlier predictions |
| RMSE >> MAE | A subset of predictions contains large errors; the model struggles at extremes |
| Both low | Model is performing well across all test observations |

Using both metrics in conjunction provides a more complete and reliable evaluation of model performance than either metric alone.

---

## Dependencies

All required packages are part of the standard Python data science ecosystem.

```
numpy
pandas
scikit-learn
matplotlib
seaborn
```

Install all dependencies in one command:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

Alternatively, if a `requirements.txt` is present:

```bash
pip install -r requirements.txt
```

> Python 3.8 or above is recommended.

---

## How to Run

**Step 1 — Clone the repository**

```bash
git clone https://github.com/DakshMehrotra/Daksh-Mehrotra-Statistics-and-Data-Analysis.git
cd Daksh-Mehrotra-Statistics-and-Data-Analysis
```

**Step 2 — Install dependencies**

```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

**Step 3 — Run the solution scripts**

```bash
python Answer-1.py
python Answer-2.py
```

> Both `.csv` dataset files must remain in the same directory as the scripts for file paths to resolve correctly.

---

## References

1. Hyndman, R.J. & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice*, 3rd Edition. OTexts. Available at: https://otexts.com/fpp3/
2. Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825–2830.
3. Scikit-learn Developers. *sklearn.metrics — Model Evaluation Metrics*. https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
4. Willmott, C.J. & Matsuura, K. (2005). Advantages of the Mean Absolute Error (MAE) over the Root Mean Square Error (RMSE) in assessing average model performance. *Climate Research*, 30, 79–82.
5. McKinney, W. (2010). Data Structures for Statistical Computing in Python. *Proceedings of the 9th Python in Science Conference*, 51–56.

---

## Author

**Daksh Mehrotra**  
SAP ID: 500125960 | Roll No: R2142231932 | Batch: 2 CCVT  
GitHub: [github.com/DakshMehrotra](https://github.com/DakshMehrotra)

---

*Submitted in partial fulfilment of the Statistics and Data Analysis course requirements.*
