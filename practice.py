import math

def max_num(a,b,c):
    nums = [a,b,c]
    return max(nums)

print(max_num(3, 1, 7))

def mult_list(*args):
    return math.prod(list(args))

print(mult_list(1, 2, 3))

def rev_string(string):
    return string[:: -1]

print(rev_string("Hello World!"))

def num_within(num,min,max):
    if num >= min and num <= max:
        return True
    else:
        return False
    
print(num_within(10, 3, 10))

def pascal(n):
    for i in range(n):
        print(' '*(n - 1), end='')
        print(' '.join(map(str, str(11**i))))

pascal(5)