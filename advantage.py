# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import collections
import pprint
import random

def _1d20():
    return random.choice(range(1, 21))

def roll_with_advantage():

    return max([_1d20(), _1d20()])

if __name__ == "__main__":

    score = collections.defaultdict(int)
    nat20s = collections.defaultdict(int)

    for _ in range(1000*1000):

        a = roll_with_advantage()

        if a == 20:
            nat20s["advantage"] += 1

        b = _1d20()

        if b == 20:
            nat20s["1d20"] += 1

        c = _1d20() + 1

        if c == 21:
            nat20s["1d20+1"] += 1

        d = _1d20() + 3

        if d == 23:
            nat20s["1d20+3"] += 1

        e = _1d20() + 5

        if e == 25:
            nat20s["1d20+5"] += 1

        if max([a, b, c, d, e]) == a:
            score["advantage"] += 1

        if max([a, b, c, d, e]) == b:
            score["1d20"] += 1

        if max([a, b, c, d, e]) == c:
            score["1d20+1"] += 1

        if max([a, b, c, d, e]) == d:
            score["1d20+3"] += 1

        if max([a, b, c, d, e]) == e:
            score["1d20+5"] += 1

    pprint.pprint(nat20s)
    pprint.pprint(score)

