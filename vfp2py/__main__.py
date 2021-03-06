# coding=utf-8
from __future__ import absolute_import, division, print_function

import argparse
import logging

from . import vfp2py

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Tool for rewriting Foxpro code in Python')
    parser.add_argument("--logging", help="file to convert", action='store_true')
    parser.add_argument("infile", help="file to convert - supported file types are prg, mpr, spr, scx, vcx, or pjx,", type=str)
    parser.add_argument("outpath", help="path to output converted code, will be a filename for all but pjx which will be a directory", type=str)
    parser.add_argument("search", help="directory to search for included files", type=str, nargs='*')
    return parser.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)
    if args.logging:
        logging.basicConfig(level=logging.DEBUG)
    vfp2py.SEARCH_PATH += args.search
    vfp2py.convert_file(args.infile, args.outpath)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
