import sys

inname, outname = sys.argv[1:3]


class WarningFilter:
    def __init__(self, insequence):
        self.insequence = insequence

    def __iter__(self):
        return self

    def __next__(self):
        """ reads lines from the file, discarding them if they are not WARNING lines.
        When it encounters a WARNING line, remove the WARNING string and returns it"""
        line = self.insequence.readline()
        while line and 'WARNING' not in line:
            line = self.insequence.readline()

        if not line:
            raise StopIteration

        return line.replace(' WARNING', '')


with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = WarningFilter(infile)
        for line in filter:
            outfile.write(line)