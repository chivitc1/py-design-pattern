# Basic iterator pattern

- An iterator must implement __next__() for the for-loop to call to get a next new item from a sequence
- Any class implement __iter__() is a iterable
- The __iter__() must return an iterator which cover all the elements in that class.

## example

Defines an CapitalIterable class whose job is to loop over each of the
words in a string and output them with the first letter capitalized. Most of the work
of that iterable is passed to the CapitalIterator implementation