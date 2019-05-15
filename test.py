#!/usr/bin/python3

from math import sqrt
import sys


def usage(progname):
    print('USAGE')
    print('\t%s pSize sSize p' % progname)
    print()
    print('DESCRIPTION')
    print('\tpSize\tsize of the population')
    print('\tsSize\tsize of the sample (supposed to be representative)')
    print('\tp\tpercentage of voting intentions for a specific candidate')


def main(args):
    if '-h' in args[1:]:
        usage(args[0])
        return 0

    if len(args) != 4:
        print('%s: missing or excess arguments' % args[0], file=sys.stderr)
        usage(args[0])
        return 84

    try:
        psize, ssize, p = int(args[1]), int(args[2]), float(args[3]) / 100
        if not (psize > 1 and 0 <= ssize <= psize and 0 <= p <= 1):
            raise ValueError()
    except ValueError:
        print('%s: invalid argument' % args[0], file=sys.stderr)
        return 84

    def clamp(x):
        return min(max(x, 0), 1)

    def interval(x, i):
        return (100 * clamp(x - i), 100 * clamp(x + i))

    v = ((p * (1 - p)) / ssize) * ((psize - ssize) / (psize - 1))
    i95 = interval(p, 1.96 * sqrt(v))
    i99 = interval(p, 2.58 * sqrt(v))

    print('population size:\t\t%d' % psize)
    print('sample size:\t\t\t%d' % ssize)
    print('voting intentions:\t\t%g%%' % (p * 100))
    print('variance:\t\t\t%f' % v)
    print('95%% confidence interval:\t[%.2f%% ; %.2f%%]' % i95)
    print('99%% confidence interval:\t[%.2f%% ; %.2f%%]' % i99)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
