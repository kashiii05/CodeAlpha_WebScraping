import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

books = []

for book in soup.select("article.product_pod"):
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text

    rating = book.p["class"][1]

    books.append({
        "Title": title,
        "Price": price,
        "Rating": rating
    })

df = pd.DataFrame(books)
df.to_csv("books_data.csv", index=False)

print("\nWeb Scraping Completed Successfully!\n")
print(df.head())
print(f"\nTotal Books Scraped: {len(df)}")
print("CSV File Saved as books_data.csv")
