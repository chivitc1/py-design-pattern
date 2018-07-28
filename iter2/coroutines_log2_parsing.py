import re

def match_regex(filename, regex):
    with open(filename) as file:
        lines = file.readlines()

    for line in reversed(lines):
        match = re.match(regex, line)
        if match:
            regex = yield match.groups()[0]

def get_serials(filename):
    ERROR_RE = 'XFS ERROR (\[sd[a-z]\])'

    # Create generator of XFS ERROR
    matcher = match_regex(filename, ERROR_RE)
    device = next(matcher)

    while True:
        # Create regex pattern for BUS INFO base on DEVICE got ERROR
        bus_regex = '(sd \S+) {}.*'.format(re.escape(device))
        print('bus_regex:', bus_regex)


        # Send BUS regex to generator to get BUS info of ERROR
        bus = matcher.send(bus_regex)

        # Send SERIAL regex to generator to get SERIAL NO of DEVICE in ERROR
        serial_regex = '{} \(SERIAL=([^)]*)\)'.format(bus)
        print('serial_regex:', serial_regex)
        serial = matcher.send(serial_regex)
        yield serial

        # Send ERROR regex to generator to get next DEVICE in ERROR
        device = matcher.send(ERROR_RE)

def main():
    filename = 'iter2/log2.txt'
    print('List of serial no found: ')
    for serial in get_serials(filename=filename):
        print(serial)

if __name__ == '__main__':
    main()