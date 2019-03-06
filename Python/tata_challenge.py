import requests
from bs4 import BeautifulSoup
import csv

source=requests.get('http://tatainnoverse.com/').text

soup=BeautifulSoup(source,'lxml')


csv_file=open('challenge_data.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Problem Name','Content'])

for challenge in soup.find_all('div',class_='content'):
    header=challenge.h3.text
    content=challenge.p.text
    csv_writer.writerow([header,content])


csv_file.close()







