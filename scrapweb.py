# In this code i have scrap the home page content.
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://surajice28.herokuapp.com/").text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

csv_file = open('icecreame_scrap.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'text'])

for flavors in soup.find_all('div',class_='card-body'):
    title = flavors.h5.text
    print(title)
    text = flavors.p.text
    print(text)
    
    print()
    csv_writer.writerow([title, text])

csv_file.close