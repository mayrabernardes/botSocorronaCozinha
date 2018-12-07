import requests
from bs4 import BeautifulSoup as bs

url = requests.get('https://receitas.ig.com.br/busca/?q=arroz+de+forno.html')
s = bs(url.content,'html.parser')
ricos = s.findAll('ul',{'class': 'receitas'})

for x in ricos:
    print(x)