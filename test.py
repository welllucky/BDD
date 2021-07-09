from bs4 import BeautifulSoup
import requests
import time

request_twitter = requests.get('https://twitter.com/home')
requests_ton = requests.get('https://twitter.com/tonmedeiros')

print(f'Code Twitter-main = {request_twitter.status_code}\nCode Twitter-ton = {requests_ton.status_code}')

time.sleep(5)
print(request_twitter.text)
input('Continuar?: ')
print(requests_ton.text)