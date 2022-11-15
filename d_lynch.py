import requests
from bs4 import BeautifulSoup
import csv

page_one = "https://www.brainyquote.com/authors/david-lynch-quotes"
page_two = "https://www.brainyquote.com/authors/david-lynch-quotes_2"
headers = ["quote_number", "quote_text"]

def gather_quotes(url_list):
    quotes = []
    num = 32
    for url in url_list:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        pretty = soup.prettify()
        for d in soup.find_all('div', attrs={'style': 'display: flex;justify-content: space-between'}):
            quotes.append([num, d.text.strip()])
            num += 1
        
        return quotes

####
####
data = gather_quotes([page_one])

with open('DL_quotes.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    if data:
        writer.writerows(data)
