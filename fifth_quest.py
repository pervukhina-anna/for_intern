# Напиши функцию на Python, выполняющую сравнение версий. Условия:
# Return -1 if version A is older than version B
# Return 0 if version A and B are equivalent
# Return 1 if version A is newer than version B
# Each subsection is supposed to be interpreted as a number,
# therefore 1.10 > 1.1
import re
from typing import List


def transform_version(version: str) -> List[int]:
    """
    Функция принимает на вход версию в виде строки и преобразовывает в список.
    """
    version = re.split(r'_|\W+', version)
    transformed_version = []
    for elem in version:
        if not elem.isdigit():
            raise ValueError(
                'Версия должна быть представлена в формате "число.число.число"'
            )
        transformed_version.append(int(elem))
    return transformed_version


def compare_versions(version_a: List[int], version_b: List[int]) -> int:
    """
    Функция принимает на вход две версии; определяет, какая старше. Возвращает:
    1, если версия В старше версии А;
    0, если версии равны;
    -1, если версия А старше версии В.
    """
    max_length = max(len(version_a), len(version_b))
    for i in range(max_length):
        v_a = version_a[i] if i < len(version_a) else 0
        v_b = version_b[i] if i < len(version_b) else 0
        if v_a > v_b:
            return 1
        elif v_a < v_b:
            return -1
    return 0


if __name__ == '__main__':
    for version_a, version_b in [
        ('1.1.1', '1.1.1'),
        ('1.0.1', '1.1'),
        ('1.10', '1.1'),
        ('1.1', '1.1.0'),
        ('1', '0')
    ]:
        print(compare_versions(
            transform_version(version_a),
            transform_version(version_b)
        )
        )
