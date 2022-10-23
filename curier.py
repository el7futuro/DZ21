from typing import Dict

from abs_storage import AbstractStorage
from exception import BaseError


class Courier:
    def __init__(self, request, storages: Dict[str, AbstractStorage]):
        self._request = request
        self.sender = storages[self._request.sender]
        self.receiver = storages[self._request.receiver]

    def transport(self):
        self.sender.remove(name=self._request.product, amount=self._request.amount)
        print(f'Курьер забирает {self._request.amount} {self._request.product} из {self._request.sender}')
        print(f'Курьер везет {self._request.amount} {self._request.product} со {self._request.sender} в {self._request.receiver}')
        try:
            self.receiver.add(name=self._request.product, amount=self._request.amount)
            print(f'Курьер доставил {self._request.amount} в {self._request.receiver}')
        except BaseError as e:
            self.sender.add(name=self._request.product, amount=self._request.amount)
            print(e.message)
            print(
                f'Курьер вернул {self._request.amount} {self._request.product} в {self._request.sender}')

