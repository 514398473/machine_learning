# coding=utf-8
import numpy



def replace_mean(t):
    for i in range(t.shape[1]):
        n = t[:, i]
        non = numpy.count_nonzero(n != n)
        if non != 0:
            not_nan = n[n == n]
            n[numpy.isnan(n)] = not_nan.mean()
    return t

arr = numpy.arange(24)
arr = arr.reshape(4, 6)
arr = arr.astype('float')
arr[2, 4] = numpy.nan
print(arr)
replace_mean(arr)
print(arr)
