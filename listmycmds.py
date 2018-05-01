#!/usr/bin/env python3
# coding: utf-8
#
"""
Print the commands in some ("my") directories of the ones listed in PATH

These "my" directories are determined as:
(1) directories beginning with my home directory
    (for something like /home/me/bin)
(2) additional directories explicitly specified
    in the environment variable MYCMDSPATH
"""

import sys
import os
import os.path as osp
import fnmatch

import argh


def dirs_starting_with_HOME():
    """
    find all directories in PATH which contain HOME
    :return: list of directories
    """
    try:
        path = os.environ['PATH']
        home = os.environ['HOME']
        return [d for d in path.split(':') if d.startswith(home)]
    except KeyError:
        return []

def dirs_from_MYCMDSPATH():
    """
    find all directories in MYCMDSPATH
    :return: list of directories
    """
    try:
        path = os.environ['PATH']
        mycmdspath = os.environ['MYCMDSPATH']
        return [d for d in path.split(':') if d in mycmdspath.split(':')]
    except KeyError:
        return []


def combine_new_with_master_list(new, master):
    """
    add elements of a new list to a master list if an element is new,
    i.e. does not exist in the master list
    :param new: list with new elements
    :param master: list the elements are added to
    :return: combined list
    """
    res = master
    for el in new:
        if not el in res:
            res.append(el)
    return res


class ColumnPrinter():
    """
    A class which takes collects print entries and issues
    a print line to stdout when all columns are filled
    """
    def __init__(self, col_num, full_width):
        self.cols_in_row = col_num
        self.col_width = full_width // col_num

        # setup
        self.entries_in_row = []
        self.entry_format_str = '{0:%s}' % self.col_width


    def print(self, entry=None, flush=False):
        """
        Print an entry. None entries print nothing.
        flush=True enforces leftover entries are printed
        """

        # add entry
        if entry is not None:
            self.entries_in_row.append(entry)

        # possibly print entries and reset
        if flush or len(self.entries_in_row) >= self.cols_in_row:
            printed = False
            for e in self.entries_in_row:
                print(self.entry_format_str.format(e), end="")
                printed = True
            if printed:
                print()
            # clear entries_in_row for start of a new row
            self.entries_in_row = []


def print_if_pattern_match(fname, patterns, printer):
    for p in patterns:
        q = p if '*' in p else ('*%s*' % p)
        if fnmatch.fnmatch(fname, q):
            printer.print(fname)
            break


@argh.arg('patterns', nargs='*', metavar='PATTERN',
          help="(file glob) pattern to filter commands on")
@argh.arg('-a', '--all-files',
          help="list not only executable commands, but all files")
#@argh.arg('-l', '--with-location',
#         help="list commands plus their path")
@argh.arg('-1', '--single-column',
          help="list one command per line")
def listmycmds(patterns,
               all_files=False,
               #with_location=False,
               single_column=False):
    # defaults
    if patterns == []:
       patterns.append('*')

    cols_in_row = 2
    if single_column or not sys.stdout.isatty():
        cols_in_row = 1
    try:
        full_width = int(os.environ['COLUMNS'])
    except (ValueError, KeyError):
        full_width = 80

    # setup column printing
    printer = ColumnPrinter(cols_in_row, full_width)

    dirs = combine_new_with_master_list(dirs_starting_with_HOME(), [])
    dirs = combine_new_with_master_list(dirs_from_MYCMDSPATH(), dirs)
    for d in dirs:
        for fname in os.listdir(d):
            fpath = osp.join(d, fname)
            if os.path.isfile(fpath):
                if all_files or os.access(fpath, os.X_OK):
                    print_if_pattern_match(fname, patterns, printer)

    printer.print(flush=True)


if __name__ == '__main__':
    argh.dispatch_command(listmycmds)

