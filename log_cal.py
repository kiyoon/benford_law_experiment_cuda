#!/usr/bin/env python2
from math import log
import sys

n = int(sys.argv[1])
k = int(sys.argv[2])
print "log%d / log%d: " % (n, k) + str(log(n)/log(k))
