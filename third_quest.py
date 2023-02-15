# Сколько HTML-тегов в коде главной страницы сайта greenatom.ru? Сколько из них
# содержит атрибуты? Напиши скрипт на Python, который выводит ответы на вопросы
# выше.
from http import HTTPStatus
from typing import Dict

import requests
from bs4 import BeautifulSoup
from colorama import Fore


def get_page_data(url: str, headers: Dict) -> BeautifulSoup:
    """
    Функция осуществляет запрос к заданной странице, в случае успещного
    запроса возвращает экземпляр класса `BeautifulSoup` с данными страницы.
    """
    try:
        page = requests.get(url, headers=headers)
        if page.status_code != HTTPStatus.OK:
            raise ConnectionError(
                f'Проблемы с доступом к ресурсу {url}, '
                f'код ошибки - {page.status_code}.'
            )
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup
    except Exception:
        raise Exception(f'Адрес {url} недоступен!')



def count_tags(soup: BeautifulSoup) -> str:
    """
    Функция подсчитывает общее количество тегов на странице
    и количество тегов с атрибутами.
    """
    tags = soup.find_all()
    tags_with_attrs = [tag.attrs for tag in tags if tag.attrs]
    return (
        Fore.YELLOW +
        f'Количество HTML-тегов в коде страницы сайта {URL} - {len(tags)}. \n'
        f'Количество тегов с атрибутами - {len(tags_with_attrs)}.'
    )


if __name__ == '__main__':
    URL = 'https://greenatom.ru/'
    HEADERS = {
        'user-agent':
            ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
             '(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
    }

    page_data_soup = get_page_data(URL, HEADERS)
    print(count_tags(page_data_soup))
