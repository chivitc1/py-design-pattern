import sys

"""Pass contact filename as first argument at command line"""
filename = sys.argv[1]

DELIMITER = '\t'

with open(filename) as file:
    # Read first line for header, and move iter over first line to get the data lines
    header = file.readline().strip().split(DELIMITER)

    # Loop over file from the second line
    contacts = [
        dict(zip(header, line.strip().split(DELIMITER))) for line in file
    ]

for contact in contacts:
    print("email: {email} -- {lastname}, {firstname}".format(**contact))