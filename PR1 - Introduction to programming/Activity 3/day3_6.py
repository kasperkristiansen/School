#Additional
#3

import sys
my_var = 'A'
print('\nSize of ', my_var, ':\t', sys.getsizeof(my_var))
my_var = '42'
print('Size of', my_var, ':\t', sys.getsizeof(my_var))
my_var = 42
print('Size of', my_var, ':\t', sys.getsizeof(my_var))
my_var = 2 ** 100
print('Size of', my_var, ':\t', sys.getsizeof(my_var))
my_var = "Monty Python's Flying Circus!"
print('Size of', my_var, ':\t', sys.getsizeof(my_var))