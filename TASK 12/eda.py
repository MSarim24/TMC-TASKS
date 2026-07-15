import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")


np.random.seed(42)

n = 500

df = pd.DataFrame({
    'Age': np.random.randint(22, 60, n),
    'Experience': np.random.randint(0, 35, n),
    'Salary': np.random.randint(30000, 150000, n),
    'Department': np.random.choice(
        ['IT', 'HR', 'Finance', 'Marketing', 'Sales'],
        n
    ),
    'Gender': np.random.choice(
        ['Male', 'Female'],
        n
    ),
    'PerformanceScore': np.random.randint(50, 100, n)
})

df.to_csv('employee_data.csv', index=False)

print(df.head())

df = pd.read_csv('employee_data.csv')


print("Shape:")
print(df.shape)

print("\nInfo:")
print(df.info())

print("\nDescribe:")
print(df.describe())

print(df.isnull().sum())


numerical_cols = [
    'Age',
    'Experience',
    'Salary',
    'PerformanceScore'
]

for col in numerical_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], bins=20, kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()


for col in numerical_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()

plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Department')
plt.title('Department Distribution')
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Gender')
plt.title('Gender Distribution')
plt.show()


plt.figure(figsize=(7,5))
sns.scatterplot(
    data=df,
    x='Experience',
    y='Salary'
)

plt.title('Experience vs Salary')
plt.show()


plt.figure(figsize=(7,5))
sns.scatterplot(
    data=df,
    x='Age',
    y='Salary'
)

plt.title('Age vs Salary')
plt.show()


plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x='Department',
    y='Salary'
)

plt.title('Salary Distribution by Department')
plt.show()


corr = df.corr(numeric_only=True)

print(corr)


plt.figure(figsize=(8,6))

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Heatmap')

plt.show()