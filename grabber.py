import os
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
import requests
from colorama import init
init()


class Grabber:
    # Тип парсера на выбор: lxml html5lib html.parser
    parser = "html.parser"

    def __init__(self, url):
        self._url = url
        # Отделяем первые 4 символа для определения типа (Из файла, с сайта по ссылке)
        if url[:4] != "http":
            self.config(url, type_="file")
        else:
            self.config(url, type_="link")

    def config(self, url="index.html", type_="file") -> None:
        # Базовые настройки для сборщика
        self._url = url
        match type_:
            case "file":
                # Получаем информацию из файла
                with open(self._url) as fp:
                    self._soup = BeautifulSoup(fp, self.parser)
            case "link":
                # Получаем информацию по ссылке
                self._page = requests.get(self._url)
                self._soup = BeautifulSoup(self._page.text, self.parser)

    def get_element(self, tag_: str, class_: str, attr_: str) -> list:
        # Получить список элементов по HTML тэгу, классу и необходимый атрибут
        # Пример получения id у div с классом contener
        # get_element("div", "contener", "id")
        links = self._soup.find_all(tag_, class_=class_)
        result = []
        for link in links:
            result.append(
                link.get(attr_)
            )
        return result

    def download(self, url, name, path=''):
        # метод для скачивания файлов
        # Пример скачивания страницы google.com
        # download(url='https://www.google.com/', name='google_page.html', path="")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                if not os.path.exists(path + name):
                    with open(path + name, 'wb') as file:
                        file.write(response.content)
                        print(f'{Fore.GREEN + "[+]"}{url}|{path +
                                                           name}|downloaded successfully')
                else:
                    print(f"{Fore.YELLOW}[-]|{url}|{path + name}|File exists")
            else:
                print(
                    f"{Fore.RED}[-]|{url}|{path + name}|Error status code: {str(response.status_code)}")
        except Exception as e:
            print(
                f"{Fore.RED}[-]|{url}|{path + name}|{e}"
            )
