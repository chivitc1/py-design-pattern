"""model a few folders and files in a Unix filesystem so we can
    use yield from to walk them effectively"""

class File:

    def __init__(self, name):
        self.name = name


class Folder(File):
    def __init__(self, name):
        super().__init__(name)
        self.children = []


def setup_data():
    root = Folder('')
    etc = Folder('etc')
    root.children.append(etc)
    etc.children.append(File('passwd'))
    etc.children.append(File('groups'))
    httpd = Folder('httpd')
    etc.children.append(httpd)
    httpd.children.append(File('http.conf'))
    var = Folder('var')
    root.children.append(var)
    log = Folder('log')
    var.children.append(log)
    log.children.append(File('messages'))
    log.children.append(File('kernel'))
    return root


def walk(file):
    """If this code encounters a directory, it recursively asks walk() to generate a list of
    all files subordinate to each of its children, and then yields all that data plus its
    own filename."""
    if isinstance(file, Folder):
        yield file.name + '/'
        for f in file.children:
            yield from walk(f)

    elif isinstance(file, File):
        yield file.name
    else:
        raise ValueError(file)


def main():
    root_dir = setup_data()
    for name in walk(root_dir):
        print(name)


if __name__ == '__main__':
    main()