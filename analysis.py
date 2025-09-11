# --- Import libraries ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# --- Task 1: Load and Explore the Dataset ---
try:
    iris_data = load_iris(as_frame=True)
    df = iris_data.frame
    print("Dataset loaded successfully!\n")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Show first 5 rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Info about dataset
print("Dataset Info:")
print(df.info(), "\n")

# Check missing values
print("Missing values:")
print(df.isnull().sum(), "\n")

# Fill missing values if any
df = df.fillna(df.mean(numeric_only=True))

# --- Task 2: Basic Data Analysis ---
print("Descriptive Statistics:")
print(df.describe(), "\n")

# Grouping by species (target = 0,1,2)
grouped = df.groupby("target").mean()
print("Average values per species:")
print(grouped, "\n")

# Add readable species names
df["species"] = df["target"].map(dict(zip(range(3), iris_data.target_names)))

print("Finding:")
print("→ Iris-virginica generally has the largest petals compared to the other species.\n")

# --- Task 3: Data Visualizations ---
plt.style.use("seaborn-v0_8")

# 1. Line chart
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None, palette="Set2")
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="Set1")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
