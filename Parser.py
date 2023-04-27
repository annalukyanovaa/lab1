import xlsxwriter
from bs4 import BeautifulSoup
import requests
out_xlsx_filename='out.xlsx'

def parse():
    url='https://www.labirint.ru/search/python/'
    page=requests.get(url)
    print(page.status_code)
    soup=BeautifulSoup(page.text,"html.parser")
    name=soup.findAll('a', class_='product-title-link')
    list1=[]
    for data in name:
        if data.find('span', class_='product-title'):
            list1.append(data.text.strip())


    price=soup.findAll('span', class_='price-val')
    list2 = []
    for data in price:
        if data.find('span'):
           list2.append(data.text.strip())


    author = soup.findAll('div', class_='product-author')
    list3 = []
    for data in author:
        if data.find('span'):
            list3.append(data.text.strip())
    with xlsxwriter.Workbook(out_xlsx_filename) as workbook:
        ws = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        headers = ['Название', 'Автор', 'Цена']


        for col, h in enumerate(headers):
            ws.write_string(0, col, h, cell_format=bold)

        for row, item in enumerate(list1, start=1):
            ws.write_string(row, 0, item)
        for row, item in enumerate(list3, start=1):
            ws.write_string(row, 1, item)
        for row, item in enumerate(list2, start=1):
            ws.write_string(row, 2, item)



def main():
    parse()









