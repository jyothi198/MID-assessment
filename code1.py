import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
books_data = []
for book in soup.find_all('article', class_='product_pod'):
    title = book.find('h3').find('a').attrs['title']
    price = book.find('p', class_='price_color').text
    rating = book.find('p', class_='star-rating').attrs['class'][1]
    books_data.append({
        'Title': title,
        'Price': price,
        'Rating': rating
    })
df = pd.DataFrame(books_data)
print(df.head())
df.to_csv('books.csv',index=False)
print("Data saved")