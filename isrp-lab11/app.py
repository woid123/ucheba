import requests


def add(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print('Готово:', add(2, 3), requests.__version__)
