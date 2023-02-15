# Задачки для стажера

_**1. Какие шаги ты бы предпринял, если бы пользователь сказал, что API возвращает ему ошибку 500?**_

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

_**3. Сколько HTML-тегов в коде главной страницы сайта greenatom.ru? Сколько из них
содержит атрибуты? Напиши скрипт на Python, который выводит ответы на вопросы
выше.**_

_**4. Напиши функцию на Python, которая возвращает текущий публичный IP-адрес
компьютера (например, с использованием сервиса ifconfig.me).**_

_**5. Напиши функцию на Python, выполняющую сравнение версий. Условия:**_
```
Return -1 if version A is older than version B
Return 0 if version A and B are equivalent
Return 1 if version A is newer than version B
Each subsection is supposed to be interpreted as a number,
therefore 1.10 > 1.1.
```


# Задачка для DE

* _**Написать сервис/скрипт, который загружает данные из 
[GraphQL API](https://studio.apollographql.com/public/SpaceX-pxxbxen/home) в базу данных Postgres.**_
* _**Спроектировать модель данных с витринами данных. Например [тут](https://www.diagrams.net/).**_
* _**Написать сервис/скрипт, который наполняет спроектированные таблицы.**_
* _**Создать витрину данных, которая подсчитывает количество публикаций по миссиям,
ракетам и пускам (missions, rockets and launches).**_
* _**Написать Dockerfile и docker-compose.yml, которые позволят нам запустить твой код и
делать запросы к БД (docker compose up -d).**_
* _**Залить проект на GitHub и поделиться с нами ссылкой на него (сделать публичным). А также ссылкой на модель данных.**_

