#!/usr/bin/env python
#coding=utf8

"""maelstrom

Usage:
  maelstrom init <directory> ...
  maelstrom (-h | --help)
  maelstrom (-v | --version)

Commands:
  init          Initialize a new collection.

Options:
  -h --help     Show this message.
  -v --version  Show version.
"""

from docopt import docopt
from glob import iglob
import os.path


def run(args):
    """Iterate over the keys and values in args and call the appropriate
    function."""
    for key, val in args.iteritems():
        if val:
            try:
                globals()[key](args)
                return
            except KeyError:
                pass


def init(args):
    """Initialize a new collection."""
    movies = []
    for path in args['<directory>']:
        for movie in iglob(os.path.join(path, '*')):
            movies.append(os.path.split(movie))
    # TODO Save items to a database in the working directory.


def main():
    """Parse commands and run the relevant function."""
    run(docopt(__doc__, version='0.0'))


if __name__ == '__main__':
    main()
