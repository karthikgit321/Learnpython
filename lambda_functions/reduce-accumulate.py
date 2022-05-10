'''
Both reduce() and accumulate() can be used to calculate the summation of a sequence elements.
 But there are differences in the implementation aspects in both of these.

reduce() is defined in “functools” module, accumulate() in “itertools” module.
reduce() stores the intermediate result and only returns the final summation value.
Whereas, accumulate() returns a iterator containing the intermediate results.
The last number of the iterator returned is summation value of the list.
reduce(fun,seq) takes function as 1st and sequence as 2nd argument.
In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.
'''

import itertools
import functools

lis=[1,2,3,4,5]

print(functools.reduce(lambda x,y :x+y,lis))

print(list(itertools.accumulate(lis,lambda x,y :x+y)))