from evenonly import EvenOnly

e = EvenOnly()


def test_append_string():
    e.append("a string")


def test_append_odd_num():
    e.append(3)


def test_append_even_num():
    e.append(4)


def success():
    print("SUCCESS")

def main():
    try:
        test_append_even_num()
    except Exception as ex:
        print(ex)
    else:
        success()
    finally:
        print("This code is always run for clean up task")

    try:
        test_append_string()
        success()
    except Exception as ex:
        print('Error: ', ex)

    try:
        test_append_odd_num()
        success()
    except Exception as ex:
        print('Error: ', ex)


if __name__ == '__main__':
    main()
