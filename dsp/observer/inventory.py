class Inventory:
    def __init__(self):
        self.observers = []
        self._products = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._products

    @product.setter
    def product(self, value):
        self._products = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            # The observer will have to implement __call__ to process the update
            observer()


class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)


def test_console_observer():
    i = Inventory()
    c = ConsoleObserver(i)
    i.attach(c)
    i.product = "Nokia"
    i.quantity = 5


if __name__ == '__main__':
    test_console_observer()
