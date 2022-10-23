from exception import BadRequestError, WrongStorageError


class Request:
    def __init__(self, request, storages):
        list_from_req = request.strip().lower().split(' ')
        if len(list_from_req) != 7:
            raise BadRequestError

        if list_from_req[4] not in storages or list_from_req[6] not in storages:
            raise WrongStorageError
        else:
            self.amount = int(list_from_req[1])
            self.product = list_from_req[2]
            self.sender = list_from_req[4]
            self.receiver = list_from_req[6]







