#!/usr/bin/env python3
# template.py

# Import statements
# from . import blah


# Functions
def spam():
    return


def main_function():
    return


def main(argv):
    ''' Parse command line arguments etc.'''
    if len(argv) < 3 or len(argv) > 4:  # size for req and opt args
        raise SystemExit(f'Usage: {argv[0]} ' 'positional1 positional2',
                         '[optional1]')
    positional1 = argv[1]
    positional2 = argv[2]
    if len(argv) > 3:
        optional1 = argv[3]
    else:
        optional1 = 'default'
    main_function(positional1, positional2, optional1)


if __name__ == '__main__':
    import sys
    main(sys.argv)
