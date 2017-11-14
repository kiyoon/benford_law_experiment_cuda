#!/usr/bin/env python2
from random import randrange
from math import log
import sys


t = int(sys.argv[1])
n = int(sys.argv[2])
k = int(sys.argv[3])

sum_max = 0
for tr in range(t):

    max_count = 0
    count = 0

    for num in range(n):
        if randrange(k) == 0:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0

    max_count = max(max_count, count)
    sum_max += max_count

avg_max = sum_max / float(t)


print "t: " + str(t)
print "n: " + str(n)
print "k: " + str(k)
print "average continuity: " + str(avg_max)
print "log%d / log%d: " % (n, k) + str(log(n)/log(k))


