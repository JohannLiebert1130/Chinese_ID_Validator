import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from src.utils import Utils


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
    def get_1995_addr_code_html():
        addr_code_url = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220913.html'
        return AddressCode.get_html(addr_code_url)

    @staticmethod
    def get_latest_addr_code(base_url):
        content = AddressCode.get_latest_addr_code_html(base_url)

        soup = BeautifulSoup(content, 'html.parser')
        tds = soup.find_all('td')

        dic = {}
        iter_tds = iter(tds)

        for td in iter_tds:
            if Utils.represents_int(td.string):
                dic[td.string] = next(iter_tds).string

        return dic

    @staticmethod
    def get_1995_addr_code():
        content = AddressCode.get_1995_addr_code_html()

        soup = BeautifulSoup(content, 'html.parser')
        tds = soup.find_all('td')

        dic = {}
        iter_tds = iter(tds)

        for td in iter_tds:
            if Utils.represents_int(td.string):
                dic[td.string] = next(iter_tds).string

        return dic

    @staticmethod
    def save_addr_code_to_json(file_name=None, base_url=None, old=False):
        file_name = 'addr_code.json' if file_name is None else file_name

        with open('../data/' + file_name, 'w') as file:
            addr_code_dict = AddressCode.get_latest_addr_code(base_url) if not old else AddressCode.get_1995_addr_code()
            file.write(json.dumps(addr_code_dict, ensure_ascii=False))

    @staticmethod
    def read_addr_code_from_local(file_name=None):
        file_name = 'addr_code.json' if file_name is None else file_name

        try:
            file = open('../data/' + file_name, 'r')
        except FileNotFoundError as err:
            print(err)
        except OSError as err:
            print(err)
        else:
            content = json.load(file)
            file.close()
            return content


if __name__ == '__main__':
    url = 'http://www.mca.gov.cn/article/sj/xzqh//1980/'
    # AddressCode.save_addr_code_to_json(url)
    pprint(AddressCode.read_addr_code_from_local())

    AddressCode.save_addr_code_to_json(file_name='1995_addr_code.json', old=True)
