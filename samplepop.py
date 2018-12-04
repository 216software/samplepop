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
        pop_xx_count/float(args.pop_size)))

    sample = random.sample(pop, args.sample_size)

    sample_xx_count = sum(1 for x in sample if x["x"] == "xx")

    print("xx count for an {0}-element sample is {1}, so {2:0.2f}%".format(
        args.sample_size,
        sample_xx_count,
        sample_xx_count/float(args.sample_size)))


"""

How big does the sample need to be before it resembles the population?
is it based on the percentage of the population?  The number of elements
in the sample?

"""
