# Generator

## Use generator expression - a comprehension like with (  )
$ python iter2/read_log_file.py iter2/log.txt iter2/result.txt

## Use object-oriented Iterator class with __iter__() return self and __next__() return next item in collection
$ python iter2/filter_warning_log.py iter2/log.txt iter2/result.txt

## Use non-object-oriented with yield in function
$ python iter2/filter_warning_log2.py iter2/log.txt iter2/result.txt

## Use generator to walk a tree of files

# Log2.txt parsing with coroutines
## Log messages
- There are a whole bunch of interspersed kernel log messages, some of which pertain
to hard disks.

- The hard disk messages might be interspersed with other messages,
but they occur in a predictable format and order

- A specific drive with a known serial number is associated with a bus identifier (such as 0:0:0:0)

eg:

sd 3:0:1:8 (SERIAL=WW11111)

- A block device identifier (such as sda) is associated with that bus.

eg:

sd 3:0:1:8 [sdc] Options

- The drive has a corrupt filesystem, it might fail with an XFS error

eg:

XFS ERROR [sdc]

## Problem to solve
Obtain the serial number of any drives that have XFS errors on them.

This serial number
might later be used by a data center technician to identify and replace the drive.

We know we can identify the individual lines using regular expressions, but we'll
have to change the regular expressions as we loop through the lines, since we'll be
looking for different things depending on what we found previously.

The other
difficult bit is that if we find an error string, the information about which bus
contains that string, and what serial number is attached to the drive on that bus
has already been processed. This can easily be solved by iterating through the
lines of the file in reverse order.

## Run
$ cd design-pattern/
$ python iter2/coroutines_log2_parsing.py