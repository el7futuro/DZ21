from abc import ABC

from typing import Dict

from base_storage import BaseStorage
from exception import ExcessProductsError


class Shop(BaseStorage):

    def add(self, name: str, amount: int ):
        if self.get_unique_items_count() == 5:

            raise ExcessProductsError
        else:
            super().add(name, amount)