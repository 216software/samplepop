# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

"""
Show a histogram of what 4d6 looks like, rolled N times.
"""

import argparse
import collections
import logging
import random

log = logging.getLogger("dicefun")

def set_up_args():

    ap = argparse.ArgumentParser()

    ap.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Show debugging information, default %(default)s")

    ap.add_argument("xdy", default="4d6")
    ap.add_argument("number_rolls", type=int)

    return ap.parse_args()

def roll(s):

    """
    >>> roll("1d4") in [1,2,3,4]
    True
    """

    if "d" not in s:
        raise ValueError("Sorry, I need a string like 1d4 or 8d8")

    else:

        num_dice, sides = [int(thing) for thing in s.split("d")]

        log.debug("Parsed {0} into {1}d{2}.".format(s, num_dice, sides))

        one_die_values = list(range(1, sides+1))

        log.debug("1d{0} has these possible values: {1}.".format(
            sides, one_die_values))

        return sum(random.choice(one_die_values) for roll in range(num_dice))

if __name__ == "__main__":

    args = set_up_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    else:
        logging.basicConfig(level=logging.INFO)

    rolls = collections.defaultdict(int)

    for roll_number in range(1, args.number_rolls+1):

        result = roll(args.xdy)

        rolls[result] += 1

    for k in sorted(rolls.keys()):

        print("{0}: {1}".format(k, rolls[k]))

