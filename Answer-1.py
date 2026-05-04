# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer


# Load dataset
df = pd.read_csv('/content/Mall_Customers.csv')

# Show first 5 rows
df.head()


# Drop customer ID
df = df.drop('CustomerID', axis=1)


# Convert Gender into numeric
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})


# Missing values
print(df.isnull().sum())


# Fill missing values using mean
imputer = SimpleImputer(strategy='mean')

df_imputed = pd.DataFrame(
    imputer.fit_transform(df),
    columns=df.columns
)


# Feature scaling
scaler = StandardScaler()

scaled_data = scaler.fit_transform(df_imputed)


# Apply PCA
pca = PCA()

pca_data = pca.fit_transform(scaled_data)


# Explained variance ratio
explained_variance = pca.explained_variance_ratio_

# Plot
plt.figure(figsize=(8,5))
plt.plot(
    range(1, len(explained_variance)+1),
    explained_variance.cumsum(),
    marker='o'
)

plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Explained Variance by PCA Components')
plt.grid(True)

plt.show()


# PCA with 2 components
pca_2 = PCA(n_components=2)

principal_components = pca_2.fit_transform(scaled_data)

# Create dataframe
pca_df = pd.DataFrame(
    data=principal_components,
    columns=['PC1', 'PC2']
)

pca_df.head()


# Scatter plot
plt.figure(figsize=(8,6))

sns.scatterplot(
    x='PC1',
    y='PC2',
    data=pca_df
)

plt.title('2D Visualization using PCA')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.show()


from mpl_toolkits.mplot3d import Axes3D

# PCA with 3 components
pca_3 = PCA(n_components=3)

pca_result_3d = pca_3.fit_transform(scaled_data)

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    pca_result_3d[:,0],
    pca_result_3d[:,1],
    pca_result_3d[:,2]
)

ax.set_title("3D PCA Visualization")

plt.show()


