from timer import Timer
import datetime


def format_time(message, *args):
    now = datetime.datetime.now().strftime("%I:%M:%S")
    print(message.format(*args, now=now))

def func1(timer):
    format_time("{now}: called func1")


def func2(timer):
    format_time("{now}: called func2")


def func3(timer):
    format_time("{now}: called func3")


class Repeater:
    def __init__(self):
        self.count = 0

    def reapeater(self, timer):
        format_time("{now}: repeat {0}", self.count)
        self.count += 1
        timer.call_after(5, self.reapeater)


def main():
    timer = Timer()
    timer.call_after(1, func1)
    timer.call_after(2, func1)
    timer.call_after(2, func2)
    timer.call_after(4, func2)
    timer.call_after(3, func3)
    timer.call_after(6, func3)
    repeater = Repeater()
    timer.call_after(5, repeater.reapeater)
    format_time("{now}: Starting")
    timer.run()


if __name__ == '__main__':
    main()