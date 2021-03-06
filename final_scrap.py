
import requests 
from bs4 import BeautifulSoup 
import csv 
  
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
  
quotes=[]  # a list to store quotes 
  
table = soup.find('div', attrs = {'id':'portfolio'}) 
  
for row in table.findAll('div', attrs = {'class':'portfolio-image'}): 
    quote = {} 
    quote['theme'] = row.a['href'] 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quotes.append(quote) 

print(quotes)

filename = 'inspirational_quotes.csv'
with open(filename, 'wb') as f: 
    w = csv.DictWriter(f,['theme','url','img','lines','author']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote) 



