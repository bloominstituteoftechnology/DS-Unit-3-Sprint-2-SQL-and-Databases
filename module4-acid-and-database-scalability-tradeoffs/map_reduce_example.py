from functools import reduce  # map is built-in

my_list = [1, 2, 3, 4]

"""
We want the sum of squared values (A fairly real statisitcal task!)
Traditional(non-mapreduce approach
"""
ssv_trad = sum([i ** 2 for i in my_list])
"""
That works fine - but what if we had 40 billion numbers?
We could use a mapreduce approach 
To be clear - this ccode still runs on one computer
But mapreduce paradigm *could* be distributed more directly
"""

squared_values = map(lambda i: i ** 2, my_list)


def add_numbers(x1, x2):
    return x1 + x2


ssv_mapreduce = reduce(add_numbers, squared_values)

print('Sum of squared values (trad): ' + str(ssv_trad))
print('Sum of squared values (map-reduce): ' + str(ssv_mapreduce))
