# Задачки для стажера

Для работы некоторых скриптов необходима установка дополнительных
библиотек. Для установки необходимо активировать виртуальное окружение и
установить зависимости:

Mac:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Win:
```
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

_**1. Какие шаги ты бы предпринял, если бы пользователь сказал, что API возвращает ему ошибку 500?**_

[Решение](https://github.com/pervukhina-anna/for_intern/blob/main/first_quest.py)

_**2. Какие ты видишь проблемы в следующем фрагменте кода? Как его следует исправить?
Исправь ошибку и перепиши код ниже с использованием типизации.**_

``` python
def create_handlers(callback):
    handlers = []
    for step in range(5):
    # добавляем обработчик для каждого шага (от 0 до 4)
        handlers.append(lambda: callback(step))
	return handlers


def execute_handlers(handlers):
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()
```

[Решение](https://github.com/pervukhina-anna/for_intern/blob/main/second_quest.py)

_**3. Сколько HTML-тегов в коде главной страницы сайта greenatom.ru? Сколько из них
содержит атрибуты? Напиши скрипт на Python, который выводит ответы на вопросы
выше.**_

[Решение](https://github.com/pervukhina-anna/for_intern/blob/main/third_quest.py)

_**4. Напиши функцию на Python, которая возвращает текущий публичный IP-адрес
компьютера (например, с использованием сервиса ifconfig.me).**_

[Решение](https://github.com/pervukhina-anna/for_intern/blob/main/fourth_quest.py)

_**5. Напиши функцию на Python, выполняющую сравнение версий. Условия:**_
```
Return -1 if version A is older than version B
Return 0 if version A and B are equivalent
Return 1 if version A is newer than version B
Each subsection is supposed to be interpreted as a number,
therefore 1.10 > 1.1.
```

[Решение](https://github.com/pervukhina-anna/for_intern/blob/main/fifth_quest.py)

## Разработчик:
[Первухина Анна](https://github.com/pervukhina-anna)
