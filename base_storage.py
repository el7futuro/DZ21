
from typing import Dict
from exception import BaseError, NoCapacityError, NoItemsError

from abs_storage import AbstractStorage


class BaseStorage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int):
        if self.get_free_space() < amount:

            raise NoCapacityError
        else:
            if name in self.__items:
                self.__items[name] += amount
            else:
                self.__items[name] = amount

    def remove(self, name: str, amount: int ): #(<название>, <количество>) - уменьшает запас items
        if name not in self.__items or self.__items[name] < amount:
            raise NoItemsError
        else:
            self.__items[name] -= amount
            if self.__items[name] == 0:
                self.__items.pop(name)

    def get_free_space(self): #- вернуть количество свободных мест
        return self.__capacity - sum(self.__items.values())

    def get_items(self): #- возвращает сожержание склада в словаре {товар: количество}
        return self.__items

    def get_unique_items_count(self): # - возвращает количество уникальных товаров.
        return len(self.__items)
