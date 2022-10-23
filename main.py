from typing import Dict

from abs_storage import AbstractStorage
from curier import Courier
from exception import BaseError
from request import Request
from shop import Shop
from store import Store

store = Store(
    items={'печеньки': 3,
           'собачки': 2,
           'коробки': 5,
           },
    capacity=100,
)
shop = Shop(
    items={'собачки': 2,
           'коробки': 5,
           'корм': 1,
           'молоко': 5,
           'игрушки': 5
           },
    capacity=20,
)
storages: Dict[str, AbstractStorage] = {
    'склад': store,
    'магазин': shop,
}


def main():
    print('Добрый день \n')
    while True:
        for name, storage in storages.items():
            print(f'В {name} хранится: \n{storage.get_items()}')
        req = input(
            'Введите запрос в формате "Доставить 3 собачки из склад в магазин"'
        )
        try:
            request = Request(request=req, storages=storages)
        except BaseError as e:
            print(e.message)
            continue
        courier = Courier(request=request, storages=storages)
        try:
            courier.transport()
        except BaseError as e:
            print(e.message)



if __name__ == '__main__':
    main()