# Какие ты видишь проблемы в следующем фрагменте кода?
# Как его следует исправить?
# Исправь ошибку и перепиши код ниже с использованием типизации.
#
# ``` python
# def create_handlers(callback):
# 	handlers = []
# 	for step in range(5):
# 		# добавляем обработчик для каждого шага (от 0 до 4)
# 		handlers.append(lambda: callback(step))
# 	return handlers
#
#
# def execute_handlers(handlers):
#   # запускаем добавленные обработчики (шаги от 0 до 4)
# 	for handler in handlers:
# 		handler()
# ```


# Функция lambda ссылается на одно и то же значение step
# Можно добавить 'lambda step=step: callback(step)'

from typing import Callable, List


def create_handlers(callback: Callable) -> List[Callable]:
    handlers = []
    for step in range(5):
        # добавляем обработчик для каждого шага (от 0 до 4)
        handlers.append(lambda step=step: callback(step))
    return handlers


def execute_handlers(handlers: List[Callable]) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()
