import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='search-results-table')
    cars = catalog.find_all('div', class_='last-title last-label')
    # print(cars)
    for car in cars:
        try:
            title = car.find('h2', class_='name').text.strip()
            
        except: 
            title = ''
        try:
            price = car.find('p', class_='price').text.strip()
            
        except:
            price = ''
        try:
            img = car.find('img', class_='lazy-image visible').get('title src')
            
        except:
            img = ''
        try:
            des = car.find('p', class_='year-miles').text.strip()
            despa = car.find('p', class_='body-type').text.strip()
            despasito = car.find('p', class_='volume').text.strip()
        except:
            despasito = ''
            despa = ''
            des = ''
        data = {

            'title': title,
            'price': price,
            'img': img,
            'des': des,
            'despa': despa,
            'despasto': despasito
        }
        write_csv(data)

def write_csv(data):
    with open('cars.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow((data['title'], data['price'], data['img'], data['des'], data['despa'], data['despasito']))



    # print(cars)
def main():
    # url = 'https://cars.kg/offers'
    # html = get_html(url)
    # data = get_data(html)
    for page in range(1, 47):
        url = f'https://www.mashina.kg/commercialsearch/all/?type={page}'
        html = get_html(url)
        data = get_data(html)

main()