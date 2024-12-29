import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('books.csv')
rating_counts = df['Rating'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(rating_counts.index, rating_counts.values, color='skyblue')
plt.title('Distribution of Book Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Books')
plt.xticks(rotation=45)
plt.show()
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
price_bins = [0, 10, 20, 30, 40, 50, 100]
price_labels = ['<10', '10-20', '20-30', '30-40', '40-50', '50+']
df['price_range'] = pd.cut(df['Price'], bins=price_bins, labels=price_labels, right=False)
plt.figure(figsize=(10, 6))
price_counts = df['price_range'].value_counts().sort_index()  # Sort the bins for better clarity
plt.bar(price_counts.index, price_counts.values, color='lightcoral')
plt.title('Books by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Number of Books')
plt.xticks(rotation=45)
plt.show()