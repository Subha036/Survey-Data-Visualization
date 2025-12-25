import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("survey_data.csv")

# Bar chart: Satisfaction levels
plt.figure(figsize=(6,4))
sns.countplot(x='satisfaction', data=data)
plt.title("Customer Satisfaction Levels")
plt.show()

# Pie chart: Recommendation
recommend_counts = data['recommend'].value_counts()

plt.figure(figsize=(6,6))
recommend_counts.plot(kind='pie', autopct='%1.1f%%', title='Recommendation Distribution')
plt.ylabel("")
plt.show()

# Heatmap: Ratings correlation
ratings = data[['satisfaction', 'service_quality']]
plt.figure(figsize=(6,4))
sns.heatmap(ratings.corr(), annot=True, cmap="coolwarm")
plt.title("Survey Ratings Correlation")
plt.show()

print("Survey Data Summary:")
print(data.describe())
