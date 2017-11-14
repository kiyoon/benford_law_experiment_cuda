#!/usr/bin/env python2
from random import randrange
from math import log
import sys
import numpy as np
import pycuda.driver as drv
import pycuda.autoinit
from pycuda.compiler import SourceModule

mod = SourceModule('''
#include <stdio.h>
#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))  
__global__ void print_3d(int* maxs,unsigned char* in,int N)
{
    int init = blockIdx.x*blockDim.x*N + N*threadIdx.x;

    int i;
    int count = 0;
    int max_count = 0;
    for (i = init; i < init+N; i++)
    {
        if(in[i] == 0)
        {
            count++;
        }
        else
        {
            max_count = MAX(max_count, count);
            count = 0;
        }
    }

    max_count = MAX(max_count, count);
    maxs[blockDim.x*blockIdx.x + threadIdx.x] = max_count;

    //printf("%d ", (int)in[i]);
}
''')

t = int(sys.argv[1])
n = int(sys.argv[2])
k = int(sys.argv[3])

#print "t: " + str(t)
#print "n: " + str(n)
#print "k: " + str(k)

if t % 1000 != 0:
    raise ValueError('t must be proportional to 1000')

print_3d = mod.get_function("print_3d")
inp = np.random.randint(k, size=(t,n), dtype=np.uint8)
dest = np.zeros(t, dtype=np.int32)

blockDim = 1000
print_3d(drv.Out(dest), drv.In(inp), np.int32(n), grid=(t/blockDim,1), block=(blockDim,1,1))

print "average continuity: " + str(dest.mean())
#print "log%d / log%d: " % (n, k) + str(log(n)/log(k))

