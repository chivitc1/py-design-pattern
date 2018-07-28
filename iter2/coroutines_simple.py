"""We then call next() on each of the coroutine objects. This does the same thing as
calling next on any generator, which is to say, it executes each line of code until it
encounters a yield statement, returns the value at that point, and then pauses until
the next next() call."""


def tally():
    """return generator"""
    score = 0
    while True:
        increment = yield score
        score += increment


# construct two tally objects, one for each team
white_sox = tally()
blue_jay = tally()

"""
call to a method called send().
The send() method does exactly the same thing as next() except that in addition
to advancing the generator to the next yield statement. It also allows you to pass
in a value from outside the generator. This value is assigned to the left side of the
yield statement.
"""
print(next(white_sox))
print(next(blue_jay))
print()
print(white_sox.send(3))
print(blue_jay.send(2))
print()
print(white_sox.send(2))
print(blue_jay.send(4))