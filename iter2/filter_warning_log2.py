import sys

inname, outname = sys.argv[1:3]


def filter_warnings(insequence):
    for line in insequence:
        if 'WARNING' in line:
            yield line.replace(' WARNING', '')


with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = filter_warnings(infile)
        for line in filter:
            outfile.write(line)