# Generator

## Use generator expression - a comprehension like with (  )
$ python iter2/read_log_file.py iter2/log.txt iter2/result.txt

## Use object-oriented Iterator class with __iter__() return self and __next__() return next item in collection
$ python iter2/filter_warning_log.py iter2/log.txt iter2/result.txt

## Use non-object-oriented with yield in function
$ python iter2/filter_warning_log2.py iter2/log.txt iter2/result.txt

## Use generator to walk a tree of files
