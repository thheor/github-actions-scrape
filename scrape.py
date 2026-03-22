from bs4 import BeautifulSoup
import requests
import csv

file = open('quotes.csv', 'a')

page_to_scrape = requests.get('http://quotes.toscrape.com')

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

quotes = soup.find_all('span', attrs={'class':'text'})

authors = soup.find_all('small', attrs={'class','author'})

for quote, author in zip(quotes, authors):
    print(quote.get_text() + '\nby ' + author.get_text())
    with open("quotes.csv", "a") as f:
        f.write(f"{quote.get_text()}, {author.get_text()} \n")

file.close()
