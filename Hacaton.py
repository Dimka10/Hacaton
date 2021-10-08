import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    category = soup.find('div', class_="search-results-table")
    models = category.find_all('div', class_='list-item list-label')
    models = category.find_all('div', class_='list-item list-label new-line')
    # print(mobiles[0].find('img').get('alt'))
    # print(mobiles[0].find('img').get('data-ssrc'))
    for model in models:
        try:
            image = models.find('img').get('src')
            image = models.find('img').get('src')
        except:
            image = ''
        try:
            title = models.find('h2', class_='name')
            title = models.find('h2', class_='name')

        except:
            title = ''
        try:
            price = models.find('p', class_='price')
            price = models.find('p', class_='price')
        except:
            price = ''
        
        data = {
            'title': title, 
            'image': image,
            'price': price
        }

        write_csv(data)

def write_csv(data):
    with open('models.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow((data['title'], data['image'], data['price']))

def main():
    # url = 'https://svetofor.info/sotovye-telefony-i-aksessuary/apple-iphone/'
    # html = get_html(url)
    # get_data(html)

    for page in range(1, 7):
        url = f'https://cars.kg/offers/{page}'
        html = get_html(url)
        data = get_data(html)

main()

