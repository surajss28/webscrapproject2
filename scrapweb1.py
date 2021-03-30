# In this code i have scrap the services page content.
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://surajice28.herokuapp.com/services").text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
# title = soup.find('div',class_='card bg-info').p.text
# print(title)
csv_file = open('ice_services_scrap.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'text'])

for icecreame in soup.find_all('div',class_='card bg-info'):
    title = icecreame.h5.text
    print(title)
    text = icecreame.p.text
    print(text)
    
    print()
    csv_writer.writerow([title, text])

csv_file.close
