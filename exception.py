class BaseError(Exception):
    message = 'oups'


class NoCapacityError(BaseError):
    message = 'no capacity'


class NoItemsError(BaseError):
    message = 'no items'


class ExcessProductsError(BaseError):
    message = 'too many products'


class BadRequestError(BaseError):
    message = 'bad request, try again'


class WrongStorageError(BaseError):
    message = 'wrong storage'