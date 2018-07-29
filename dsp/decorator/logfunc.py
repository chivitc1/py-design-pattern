import time

def log_calls(func):
    def wrapper(*args, **kargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format(func.__name__, args, kargs))
        return_val = func(*args, **kargs)
        print("Executed {0} in {1} ms".format(func.__name__, time.time() - now))
        return return_val
    return wrapper

def func1(a, b, c):
    print("\tfunc1 called")

def func2(a, b):
    print("\tfunc2 called")

def func3(a, b):
    print("\tfunc3 called")
    time.sleep(1)

@log_calls
def func4(a, b):
    print("\tfunc4 called")

def test():
    f1 = log_calls(func1)
    f2 = log_calls(func2)
    f3 = log_calls(func3)

    f1(1, 2, 3)
    f2(4, b=5)
    f3(6, 7)

    func4(8, 9)

if __name__ == '__main__':
    test()
