import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)

books = soup.find_all("article", class_="product_pod")

print(len(books))

print(books[0].h3.a["title"])

print(books[0].find("p", class_="price_color").text)

print(books[0].find("p", class_="star-rating")["class"][1])

book_data = []

dic={}
for book in books:
    title = book.h3.a["title"]
    price=book.find("p",class_="price_color").text
    rating=book.find("p",class_="star-rating")["class"][1]
    book_info = {
    "title": title,
    "price": price,
    "rating": rating
    }
    
    book_data.append(book_info)

import csv

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["title", "price", "rating"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(book_data)

print("Books exported to CSV successfully!")

print(book_data[0]["title"])
print(book_data[0]["rating"])

for book in book_data:
    if not book["title"] or not book["price"] or not book["rating"]:
        print("Missing data:", book)

print("Data quality check completed!")

titles = [book["title"] for book in book_data]

print(len(titles))
print(len(set(titles)))
        
    
import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        price REAL,
        rating TEXT
    )
""")

import re

cursor.execute("DELETE FROM books")
conn.commit()


for book in book_data:
    price_text = book["price"]
    price = float(re.sub(r"[^0-9.]", "", price_text))

    
    cursor.execute("""
        INSERT INTO books (title, price, rating)
        VALUES (?, ?, ?)
    """, (book["title"], price, book["rating"]))
conn.commit()

print("Books saved successfully!")  

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM books")
print("Total books:", cursor.fetchone()[0])

cursor.execute("""
    SELECT title, price
    FROM books
    ORDER BY price DESC
    LIMIT 5
""")

results = cursor.fetchall()

for row in results:
    print(row)


print("Books cost above 40")
cursor.execute("""
    SELECT title , price
    FROM books
    WHERE price>40
    """)

results = cursor.fetchall()

for row in results:
    print(row) 

print("Books price in Ascending order")

cursor.execute("""
    SELECT title , price
    FROM books
    ORDER BY price ASC
    """)

results = cursor.fetchall()


for row in results:
    print(row)  

print("cost more than 40 in a order")
cursor.execute("""
    SELECT title , price
    FROM books
    WHERE price>40 ORDER BY price ASC
    """)

results = cursor.fetchall()

for row in results:
    print(row)     

cursor.execute("""
    SELECT COUNT(*)
    FROM books
    """)

results = cursor.fetchone()
print(results[0])

print("Book with MAX price")
cursor.execute("""
    SELECT title ,MAX(price)
    FROM books
    
    """)

results = cursor.fetchone()

print(results[0])     

cursor.execute("""
    SELECT title ,price 
    FROM books ORDER BY price DESC LIMIT 1
    
    """)

results = cursor.fetchone()

print("BOOK:",results[0])
print("PRICE:",results[1])
print("Book with 5 star rating")
cursor.execute("""
    SELECT title
    FROM books WHERE rating='Five'
    """)

results = cursor.fetchall()

for row in results:
    print(row) 


cursor.execute("""
    SELECT COUNT(*)
    FROM books WHERE rating='Five'
    """)

results = cursor.fetchone()
print(results[0])


cursor.execute("""
    SELECT rating,COUNT(*)
    FROM books GROUP BY rating ORDER BY COUNT(*) DESC
    """)

results = cursor.fetchall()

for row in results:
    print(row) 
print()
cursor.execute("""
    SELECT rating,ROUND(AVG(price), 2)
    FROM books GROUP BY rating ORDER BY AVG(price) DESC
    """)

results = cursor.fetchall()

for row in results:
    print(row)     

print("Find the most expensive book in each rating group")

cursor.execute("""
    SELECT rating,MAX(price)
    FROM books GROUP BY rating ORDER BY rating
    """)

results = cursor.fetchall()

for row in results:
    print(row) 

print("sort these rating groups by their maximum price, from highest to lowest?")  

cursor.execute("""
    SELECT rating,MAX(price)
    FROM books GROUP BY rating ORDER BY MAX(price) DESC
    """)

results = cursor.fetchall()

for row in results:
    print(row) 


conn.close()


 


conn.close()
    



