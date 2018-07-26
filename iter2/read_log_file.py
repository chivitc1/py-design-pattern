import sys


inname = sys.argv[1]
outname = sys.argv[2]

with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings = (line for line in infile if 'WARNING' in line)
        for line in warnings:
            outfile.write(line)