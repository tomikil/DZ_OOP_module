class ProductException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка с продуктом'

    def __str__(self):
        return self.message


class ProductQuantityZeroError(ProductException):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Ошибка с количеством товара.'
