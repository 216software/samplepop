# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import argparse
import random

def set_up_args():

    ap = argparse.ArgumentParser()
    ap.add_argument("pop_size", type=int)
    ap.add_argument("sample_size", type=int)
    return ap.parse_args()

def build_pop(pop_size):

    for i in range(pop_size):

        if random.random() < 0.55:
            yield {"x":'xx', "i": i}

        else:
            yield {"x":'xy', "i": i}


if __name__ == "__main__":

    args = set_up_args()

    pop = [x for x in build_pop(args.pop_size)]

    pop_xx_count = sum(1 for x in pop if x["x"] == "xx")

    print("xx count for an {0}-element population is {1}, so {2:0.2f}%".format(
        args.pop_size,
        pop_xx_count,
        100.0*pop_xx_count/float(args.pop_size)))

    sample = random.sample(pop, args.sample_size)

    sample_xx_count = sum(1 for x in sample if x["x"] == "xx")

    print("Sampled {0:0.2f}% of the population and xx count for an {1}-element sample is {2}, so {3:0.2f}%".format(
        100.0*args.sample_size / args.pop_size,
        args.sample_size,
        sample_xx_count,
        100.0*sample_xx_count/float(args.sample_size)))


"""

How big does the sample need to be before it resembles the population?
is it based on the ratio of the sample size vs the population size?

Is it just the number of elements in the sample?

It seems to be that the number of elements in the sample is important,
even if ratio of the sample to the population stays the same!

In other words, say the population is 10000 and then sample is 100, so,
1%.

That's a crappy sample.

But if the population is 1000*1000, and then sample is 1000, that's only
0.1%, but the sample is much more accurate!

Try it::

    $ python3 samplepop.py 10000 100
    xx count for an 10000-element population is 5515, so 55.15%
    xx count for an 100-element sample is 48, so 48.00%

    $ python3 samplepop.py 1000000 1000
    xx count for an 1000000-element population is 550516, so 55.05%
    xx count for an 1000-element sample is 542, so 54.20%

This article explains part of the issue:
https://www.sciencebuddies.org/science-fair-projects/references/sample-size-surveys

git notes
=========

::

    $ git bundle create samplepop.bundle master
    $ scp samplepop.bundle example.com:/tmp/
    $ ssh example.com
    $ git clone -b master /tmp/samplepop.bundle samplepop2
    $ cd samplepop2

Pretty fresh, right?

"""
