def default_arugments_func(arg1, arg2, arg3=5, arg4="hello"):
    pass


def get_pages(*links):
    for link in links:
        #download the link with urllib
        print(link)


class Options:
    default_options = {
        'port': 21,
        'host': 'localhost',
        'username': None,
        'password': None,
        'debug': False,
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]

