class EvenOnly(list):
    """adds items
    to a list only if they are even numbered integers"""

    def append(self, item):
        if not isinstance(item, int):
            raise TypeError("Only integers can be added")
        if not item % 2 == 0:
            raise ValueError("Only even numbers can be added")
        super().append(item)