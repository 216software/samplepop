# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import argparse
import random

def set_up_args():

    ap = argparse.ArgumentParser()
    ap.add_argument("sample_size", type=int)
    return ap.parse_args()

def build_pop(pop_size):

    for i in range(pop_size):

        if random.random() < 0.55:
            yield 'xx'

        else:
            yield 'xy'


if __name__ == "__main__":

    args = set_up_args()

    print("sample size: {0} ({0!r})".format(args.sample_size))

    xx_count = sum([1 for x in build_pop(args.sample_size) if x == "xx"])

    print("xx count for an {0}-element population is {1}, so {2:0.2f}%".format(
        args.sample_size,
        xx_count,
        xx_count/float(args.sample_size)))


"""

How big does the sample need to be before it resembles the population?
is it based on the percentage of the population?  The number of elements
in the sample?

"""
