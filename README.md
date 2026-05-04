# Statistics and Data Analysis Assignment

**Author:** Daksh Mehrotra  
**SapID:** 500125960
**Roll no:** R2142231932
**Batch:** 2 CCVT 
**Repository:** `Daksh-Mehrotra-Statistics-and-Data-Analysis`  
**Visibility:** Public

---

## Overview

This repository contains solutions to a Statistics and Data Analysis assignment. The work covers data preprocessing, exploratory analysis, and predictive modelling with quantitative evaluation. Two solution scripts are provided, each addressing a distinct problem using real-world datasets.

---

## Repository Structure

```
Daksh-Mehrotra-Statistics-and-Data-Analysis/
├── Answer-1.py                          # Solution to Question 1
├── Answer-2.py                          # Solution to Question 2
├── Mall_Customers.csv                   # Dataset — customer segmentation
├── train.csv                            # Dataset — model training data
└── README.md                            # Project documentation
```

---

## Datasets

### Mall_Customers.csv
A retail customer dataset containing demographic and spending behaviour attributes. Commonly used for clustering and segmentation tasks to identify distinct customer profiles.

| Column | Description |
|--------|-------------|
| CustomerID | Unique customer identifier |
| Genre | Customer gender |
| Age | Age of the customer |
| Annual Income (k$) | Annual income in thousands |
| Spending Score (1-100) | Score assigned based on spending behaviour |

### train.csv
A structured training dataset used to build and evaluate a predictive model. Contains historical records used to fit the forecasting pipeline.

---

## Solutions

### Answer-1.py
Addresses the first problem statement. Involves data loading, cleaning, and exploratory statistical analysis on the provided datasets.

**Key operations include:**
- Data ingestion and null value treatment
- Descriptive statistics (mean, median, standard deviation)
- Visualisation of distributions and correlations

### Answer-2.py
Implements a forecasting or regression model with error-based evaluation. The script computes two primary evaluation metrics:

**Mean Absolute Error (MAE)**
```python
mae = mean_absolute_error(test, forecast)
```
Measures the average absolute deviation between predicted and actual values. A lower MAE indicates better overall prediction accuracy.

**Root Mean Squared Error (RMSE)**
```python
rmse = np.sqrt(mean_squared_error(test, forecast))
```
Penalises larger errors more heavily by squaring residuals before averaging. Particularly useful for detecting outlier predictions.

```python
print("MAE:", mae)
print("RMSE:", rmse)
```

| Metric | Interpretation |
|--------|----------------|
| MAE | Average prediction error magnitude |
| RMSE | Penalised error — sensitive to large deviations |

> A large gap between RMSE and MAE indicates the presence of significant outlier errors in the forecast.

---

## Dependencies

```txt
numpy
pandas
scikit-learn
matplotlib
seaborn
```

Install via pip:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

---

## How to Run

**Clone the repository:**
```bash
git clone https://github.com/DakshMehrotra/Daksh-Mehrotra-Statistics-and-Data-Analysis.git
cd Daksh-Mehrotra-Statistics-and-Data-Analysis
```

**Run the solution scripts:**
```bash
python Answer-1.py
python Answer-2.py
```

Ensure the `.csv` dataset files are present in the same directory as the scripts before execution.

---

## Evaluation Metrics — Theoretical Background

### Why two metrics?

MAE and RMSE both measure prediction error but behave differently in the presence of outliers.

- **MAE** treats all errors equally. It is robust to outliers and gives a straightforward interpretation: the average error in the same units as the target variable.
- **RMSE** amplifies larger errors due to squaring. It is more appropriate when large deviations carry a higher practical cost.

Using both metrics together provides a more complete picture of model performance than either metric alone.

---

## References

- Hyndman, R.J. & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice*, 3rd Edition. OTexts.
- Scikit-learn Developers. *sklearn.metrics — Model Evaluation*. https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
- Willmott, C.J. & Matsuura, K. (2005). Advantages of the mean absolute error (MAE) over the root mean square error (RMSE) in assessing average model performance. *Climate Research*, 30, 79–82.

---

## Author

**Daksh Mehrotra**  
GitHub: [@DakshMehrotra](https://github.com/DakshMehrotra)

---

*Submitted as part of a Statistics and Data Analysis course assignment.*
