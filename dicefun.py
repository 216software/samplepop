# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

"""
Show a histogram of what 4d6 looks like, rolled N times.
"""

import argparse
import collections
import logging
import random

log = logging.getLogger("show-entry")

def set_up_args():

    ap = argparse.ArgumentParser()

    ap.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Show debugging information, default %(default)s")

    ap.add_argument("XdY", default="4d6")
    ap.add_argument("number_rolls", type=int)

    return ap.parse_args()

if __name__ == "__main__":

    args = set_up_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    else:
        logging.basicConfig(level=logging.INFO)

    rolls = collections.defaultdict(int)
    d = list(range(1, 7))

    for roll_number in range(1, args.number_rolls+1):

        roll = random.choice(d)

        log.debug("Roll number {0}: {1}".format(roll_number, roll))

        rolls[roll] += 1


    for x in d:
        print("{0}: {1}".format(x, rolls[x]))
