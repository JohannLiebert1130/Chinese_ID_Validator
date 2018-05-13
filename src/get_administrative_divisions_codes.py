from pprint import pprint

import requests

from bs4 import BeautifulSoup


class AddressCode:

    @staticmethod
    def get_html(url):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            html = r.text
            return html
        except:
            print("Some error occurred when getting html")

    @staticmethod
    def get_latest_addr_code_url(base_url):
        base_html = AddressCode.get_html(base_url)
        soup = BeautifulSoup(base_html, 'html.parser')
        a = soup.find('a', class_='artitlelist')

        temp_url = 'http://www.mca.gov.cn' + a['href']
        temp_html = AddressCode.get_html(temp_url)

        soup = BeautifulSoup(temp_html, 'html.parser')
        div = soup.find('div', class_='content')

        addr_code_url = div('a')[0]['href']
        return addr_code_url

    @staticmethod
    def get_latest_addr_code_html(base_url):
        addr_code_url = AddressCode.get_latest_addr_code_url(base_url)
        return AddressCode.get_html(addr_code_url)

    @staticmethod
    def save_add_code_html_text(base_url):
        with open('../data/adrr_code_html_text.txt', 'w') as file:
            file.write(AddressCode.get_latest_addr_code_html(base_url))

    @staticmethod
    def read_addr_code_from_local():
        try:
            file = open('../data/adrr_code_html_text.txt', 'r')
        except FileNotFoundError as err:
            print(err)
        except OSError as err:
            print(err)
        else:
            content = file.read()
            file.close()
            return content

    @staticmethod
    def get_latest_addr_code(base_url):
        pass


if __name__ == '__main__':
    url = 'http://www.mca.gov.cn/article/sj/xzqh//1980/'
    print(AddressCode.get_latest_addr_code_url(url))
    AddressCode.get_latest_addr_code(url)
