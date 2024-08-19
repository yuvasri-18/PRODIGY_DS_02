import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('titanic_clean.csv') 
# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())
# Check for missing values in the dataset
print("\nMissing values in the dataset:")
print(df.isnull().sum())
# Get basic statistics of the dataset
print("\nBasic statistics of the dataset:")
print(df.describe(include='all'))
# Univariate Analysis - Distribution of the 'Survived' variable
plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df)
plt.title('Distribution of Survival')
plt.show()
# Bivariate Analysis - Survival rate by Passenger Class
plt.figure(figsize=(6,4))
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Passenger Class')
plt.show()
# Bivariate Analysis - Survival rate by Gender
plt.figure(figsize=(6,4))
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.show()
# Bivariate Analysis - Survival rate by Embarkation Port
plt.figure(figsize=(6,4))
sns.barplot(x='Embarked', y='Survived', data=df)
plt.title('Survival Rate by Embarkation Port')
plt.show()
# Multivariate Analysis - Survival rate by Passenger Class and Gender
plt.figure(figsize=(8,6))
sns.catplot(x='Pclass', y='Survived', hue='Sex', kind='bar', data=df)
plt.title('Survival Rate by Passenger Class and Gender')
plt.show()
# Multivariate Analysis - Survival rate by Group Size
plt.figure(figsize=(8,6))
sns.catplot(x='GrpSize', y='Survived', kind='bar', data=df)
plt.title('Survival Rate by Group Size')
plt.show()
# Correlation Matrix for Numerical Columns Only
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
plt.figure(figsize=(10,8))
sns.heatmap(df[numerical_columns].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()
