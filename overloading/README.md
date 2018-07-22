The first argument is a target folder,
and the default behavior is to move all remaining non-keyword argument files into
that folder. Then there is a keyword-only argument, verbose, which tells us whether
to print information on each file processed. Finally, we can supply a dictionary
containing actions to perform on specific filenames; the default behavior is to move
the file, but if a valid string action has been specified in the keyword arguments, it can
be ignored or copied instead. Notice the ordering of the parameters in the function;
first the positional argument is specified, then the *filenames list, then any specific
keyword-only arguments, and finally, a **specific dictionary to hold remaining
keyword arguments.

$ cd overloading/
$ into python console
>>> from combine import augmented_move
>>> augmented_move("path2", "one.txt", "two.txt")

>>> augmented_move("path2", "three.txt", verbose=True)

>>> augmented_move("path2", "four.txt", "five.txt", "six.txt", four.txt="copy", five.txt="ignore")