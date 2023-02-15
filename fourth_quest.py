# Напиши функцию на Python, которая возвращает текущий публичный IP-адрес
# компьютера (например, с использованием сервиса ifconfig.me).
import requests
from colorama import Fore

OUTPUT_TEXT = Fore.YELLOW + 'Текущий публичный IP-адрес компьютера: '


def get_ip_from_ifconfig(url: str) -> str:
    """Запрос публичного IP с использованием ifconfig.me непосредственно."""
    return requests.get(url).text


if __name__ == '__main__':
    URL = 'https://ifconfig.me/'
    print(OUTPUT_TEXT + get_ip_from_ifconfig(URL))


# # Ниже представлены альтернативные способы
# from typing import Dict
# # ifconfig.me через json:
# def get_IP(url: str, headers: Dict) -> str:
#     page = requests.get(url, headers=headers)
#     return page.json().get('ip_addr')
#
#
# if __name__ == '__main__':
#     URL = 'https://ifconfig.me/all.json'
#     HEADERS = {
#         'user-agent':
#             ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
#              '(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
#     }
#
#     print(OUTPUT_TEXT + get_IP(URL, HEADERS))
#
#
# # С использованием библиотеки pystun3 (pip install pystun3):
# from stun import get_ip_info
#
#
# print(OUTPUT_TEXT + get_ip_info()[1])
