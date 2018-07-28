import csv
from random import random
import math
from collections import Counter

dataset_filename = 'colors.csv'


def load_colors(filename):
    with open(filename) as file:
        lines = csv.reader(file)
        for line in lines:
            yield tuple(float(y) for y in line[0:3]), line[3]


def generate_colors(count=100):
    for i in range(count):
        yield (random(), random(), random())


def color_distance(color1, color2):
    channels = zip(color1, color2)
    sum_distance_squared = 0
    for c1, c2 in channels:
        sum_distance_squared += (c1 - c2) ** 2
        print(c1, c2)
    return math.sqrt(sum_distance_squared)
    # Optimize with generator expression
    # return math.sqrt(sum(x[0] - x[1]) ** 2 for x in zip(color1, color2))


def nearest_neighbours(model_colors, num_neighbours):
    model = list(model_colors)
    target = yield
    while True:
        distances = sorted(
            ((color_distance(c[0], target), c) for c in model),
        )
        target = yield [
            d[1] for d in distances[0:num_neighbours]
        ]


def test_nearest_neighbours():
    model_colors = load_colors(filename=dataset_filename)
    target_colors = generate_colors(count=3)
    get_neighbours = nearest_neighbours(model_colors=model_colors, num_neighbours=5)
    next(get_neighbours)

    for color in target_colors:
        distances = get_neighbours.send(color)
        print(color)
        for d in distances:
            print(color_distance(color, d[0], d[1]))


def write_results(filename="output.csv"):
    with open(filename, "w") as file:
        writer = csv.writer(file)
        while True:
            color, name = yield
            writer.writerow(list(color) + [name])


def test_write_results():
    results = write_results()
    next(results)
    for i in range(3):
        print(i)
        results.send((i, i, i), i * 10)


def name_colors(get_neighbours):
    color = yield
    while True:
        near = get_neighbours.send(color)
        name_guess = Counter(
            n[1] for n in near).most_common(1)[0][0]
        color = yield name_guess


def process_colors(dataset_filename="colors.csv"):
    # construct a generator
    model_colors = load_colors(filename=dataset_filename)

    # construct three coroutines
    get_neighbours = nearest_neighbours(model_colors=model_colors, num_neighbours=5)
    get_color_name = name_colors(get_neighbours)
    output = write_results()

    # advance three coroutines to their first yield statement
    next(output)
    next(get_neighbours)
    next(get_color_name)

    """Once all the pipes are created, we use a for loop to send each of the generated colors
    into the get_color_name coroutine, and then we pipe each of the values yielded by
    that coroutine to the output coroutine, which writes it to a file."""
    for color in generate_colors():
        name = get_color_name.send(color)
        output.send((color, name))


if __name__ == '__main__':
    process_colors()
