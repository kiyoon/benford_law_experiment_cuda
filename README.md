# Description

It's a experiment code for following proposition:

** When you randomly arrange {0,1,2,...,k-1} with length of n, the maximum continuous zero is about log_2(n) **  

Refer to: Benford's law.

For example, when n=3000 and k=2, log_2(3000) = 11.55.  
In other words, 1/2^11.55 = 1/3000

# Dependency

Pycuda 2017.1.1

# Usage

If you want to run t=100000, n=10000, k=2 ({0,1}), then run  
`CUDA_DEVICE=0 python rand_cuda.py 100000 10000 2`

If you want more experiments,  
`python log_cal.py 10000 2; for i in {1..50}; do CUDA_DEVICE=0 python rand_cuda.py 100000 10000 2; done`

