import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/'
data = requests.get(url)

soup = BeautifulSoup(data.content, "html.parser")


book_title = soup.find_all('h3')

# print(book_title[0])

Bookname = []
for i in range(len(book_title)):
    Bookname.append(book_title[i].find('a').attrs["title"])

book_price = soup.find_all('p', class_ = 'price_color')


Bookprice = []
for i in range(len(book_price)):
    Bookprice.append(book_price[i].text)

book_buy_link = soup.find_all('h3') 

Booklinks = []
complete_url = 'http://books.toscrape.com/'
for i in range(len(book_buy_link)):
    Booklinks.append(complete_url + book_buy_link[i].find('a').attrs['href'])

library_dict = {"Name": Bookname, 
                "Price" : Bookprice, 
                "Link" : Booklinks
                }

books_df = pd.DataFrame(library_dict)
print(books_df)
