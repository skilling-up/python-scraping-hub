import requests
from bs4 import BeautifulSoup
import csv


url = "https://books.toscrape.com"
response = requests.get(url=url)

soup = BeautifulSoup(response.text,"html.parser")
books = soup.find_all("article", class_ = "product_pod")

all_books_data =[]

for book in books:
    title = book.h3.a['title']


    stock = book.find('p', class_ = 'instock availability').text.strip()

    price =  book.find('p',class_='price_color').text
    data = {
        "title":title,
        "price":price,
        "stock":stock
    }
    all_books_data.append(data)

with open("data.csv","w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "price", "stock"])
    writer.writeheader() # Пишем заголовки
    writer.writerows(all_books_data) # Пишем строки
