import requests
from bs4 import BeautifulSoup
import time
import csv

url = 'https://apod.nasa.gov/apod/ap201223.html'

res = requests.get(url)

res.encoding = res.apparent_encoding

soup=BeautifulSoup(res.text,'html.parser')

imgurl = soup.select('body > center:nth-child(1) > p:nth-child(3) > a')

