# Observer pattern

- Useful for state monitoring and event handling situations.

- Allows a given object to be monitored by an unknown and dynamic group of "observer" objects.

Whenever a value on the core object changes, it lets all the observer objects know
that a change has occurred, by calling an update() method. Each observer may
be responsible for different tasks whenever the core object changes; the core object
doesn't know or care what those tasks are, and the observers don't typically know
or care what other observers are doing.

## The observer will have to implement __call__() to process the update
```python
def _update_observers(self):
    for observer in self.observers:
        observer()
```
```python
class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)
```