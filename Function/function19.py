from functools import reduce
n=int(input("Enter upto how many terms you want fibonacci series "))
def fib_series(n):
    return reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0,1])
print(fib_series(n))
