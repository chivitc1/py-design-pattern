class OneOnly:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        """When __new__ is called, it normally constructs a new instance of that class. When we
        override it, we first check if our singleton instance has been created; if not, we create
        it using a super call. Thus, whenever we call the constructor on OneOnly, we always
        get the exact same instance"""
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)

        return cls._singleton


def test():
    o1 = OneOnly()
    o2 = OneOnly()
    print(o1 == o2)
    print(id(o1))
    print(id(o2))


if __name__ == '__main__':
    test()