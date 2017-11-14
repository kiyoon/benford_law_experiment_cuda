# Description

It's a experiment code for following proposition:

** When you randomly arrange {0,1,2,...,k-1} with length of n, the maximum length of continuous zeroes is about log_2(n) **  

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

# Result
Result for 100 tries for parameters below  

*t = 100000*  
*n = 10000*  
*k = 2*  

is as follows:  

log10000 / log2: 13.2877123795  

average continuity: 12.62404  
average continuity: 12.61597  
average continuity: 12.62766  
average continuity: 12.62097  
average continuity: 12.6301  
average continuity: 12.61969  
average continuity: 12.61715  
average continuity: 12.62689  
average continuity: 12.60999  
average continuity: 12.62044  
average continuity: 12.62571  
average continuity: 12.61981  
average continuity: 12.61959  
average continuity: 12.61904  
average continuity: 12.62708  
average continuity: 12.61871  
average continuity: 12.6178  
average continuity: 12.62807  
average continuity: 12.62783  
average continuity: 12.6287  
average continuity: 12.62642  
average continuity: 12.60704  
average continuity: 12.62083  
average continuity: 12.61618  
average continuity: 12.62748  
average continuity: 12.62325  
average continuity: 12.63154  
average continuity: 12.61629  
average continuity: 12.6184  
average continuity: 12.62181  
average continuity: 12.61828  
average continuity: 12.62263  
average continuity: 12.60938  
average continuity: 12.61898  
average continuity: 12.61969  
average continuity: 12.62741  
average continuity: 12.62398  
average continuity: 12.61102  
average continuity: 12.61511  
average continuity: 12.62263  
average continuity: 12.62141  
average continuity: 12.62686  
average continuity: 12.62369  
average continuity: 12.62258  
average continuity: 12.62759  
average continuity: 12.62465  
average continuity: 12.62705  
average continuity: 12.61134  
average continuity: 12.62642  
average continuity: 12.61759  
average continuity: 12.63409  
average continuity: 12.61368  
average continuity: 12.62064  
average continuity: 12.61705  
average continuity: 12.61958  
average continuity: 12.6219  
average continuity: 12.61609  
average continuity: 12.62678  
average continuity: 12.62579  
average continuity: 12.62875  
average continuity: 12.62121  
average continuity: 12.6154  
average continuity: 12.61443  
average continuity: 12.6195  
average continuity: 12.62602  
average continuity: 12.62553  
average continuity: 12.61696  
average continuity: 12.61755  
average continuity: 12.6252  
average continuity: 12.62219  
average continuity: 12.62704  
average continuity: 12.62193  
average continuity: 12.62751  
average continuity: 12.62196  
average continuity: 12.61265  
average continuity: 12.61951  
average continuity: 12.61789  
average continuity: 12.62237  
average continuity: 12.62439  
average continuity: 12.62539  
average continuity: 12.60915  
average continuity: 12.62414  
average continuity: 12.61183  
average continuity: 12.60472  
average continuity: 12.61334  
average continuity: 12.62081  
average continuity: 12.61482  
average continuity: 12.6182  
average continuity: 12.6238  
average continuity: 12.62964  
average continuity: 12.6292  
average continuity: 12.6191  
average continuity: 12.62591  
average continuity: 12.63139  
average continuity: 12.61752  
average continuity: 12.62208  
average continuity: 12.62097  
average continuity: 12.62563  
average continuity: 12.60666  
average continuity: 12.61815  
