#!/usr/bin/env python3

import sys, os, math, csv
from sys import stdin
from math import factorial, sqrt, exp, pi

def error_handling():
    arg = []
    i = 1
    if (len(sys.argv) != 4):
        exit(84)
    try:
        while (i < len(sys.argv)):
            arg.append(float(sys.argv[i]))
            i += 1
    except:
        exit(84)
    return arg

def first_print(tab):
    print("Population size: ", int(tab[0]), sep="")
    print("Sample size: ", int(tab[1]), sep="")
    print("Voting intentions: ", tab[2], "%", sep="")

def main():
    arg = error_handling()
    first_print(arg)

main()
