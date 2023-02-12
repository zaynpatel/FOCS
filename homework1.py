"""
Code a function clamp of type int -> int -> int -> int where clamp a b v returns v if v is between a and b (inclusively), 
and otherwise returns the smallest of a and b if v is smaller, or the largest of a and b if v is larger. 
In most uses, a would be the smaller value and b would be the larger value.
"""

# question 1a
"""def clamp(a, b, v):
    # 20 is more than 15 and 10
    if v <= b and v <= a:
        return v 
    # saying same thing as above
    elif v <= a and v <= b:
        return min(a, b)
    elif v >= a and v >= b:
        return max(a, b)
clamp(10, 15, 20)"""

"""def clamp(a, b, v):
    # determine lower and upper bounds
    low, high = min(a, b), max(a, b)
    # want it to compare max of low and v to make sure v is not lower than low and compare max to high to ensure v is not higher than high.
    return min(high, max(low, v))"""

# working and done mostly by self, chatgpt helped with debug 
"""def repeat(s, n):
    if n <= 0:
        return ""
    else: 
        return s + repeat(s, n-1)

trying = repeat("hello", 6)
print(trying)"""

# question 1b
def interpolate(a, b, c):
    return c * (b - a) + a 

# had correct implementation where I returned 1. Didn't have correct logic for how to print a list. 
# adding seq is similar to having a list where I append items to it, hence seq.append(n)
# for each recursive call, I add the seq values with numbers to the list. 
# my logic before was to write list(collatz_sequence) but I realized after that all functions are not iterable objects so this wouldn't make sense. 
# I can call list(collatz_sequence(n))

# question 1c
def repeat(s, n):
    if n <= 0:
        return ""
    else:
        return s + repeat(s, n-1)

# question 1d
def collatz_sequence(n, seq=None):
    if seq is None:
        seq = []
    seq.append(n)
    if n == 1:
        return seq 
    elif n % 2 == 0:
        return collatz_sequence(n / 2, seq)
    else: 
        return collatz_sequence(3*n + 1, seq)

trying = collatz_sequence(19)
#print(trying)

# question 1e
"""def sequence(i, j, step):
    if seq is None: 
        seq = []
    seq.append(zip (i, j))
    elif i < j and step > 0:
        return i + sequence(step, seq)
    elif i > j and step > 0:
        return i + sequence(step, seq)"""
def sequence(i, j, step):
   seq = []
   while i != j:
       seq.append(i)
       i += step
    seq.append(j)
    return seq
trying = sequence(10, 20, 4)
#print(trying)

# question 2a

def pairneg(lst):
    # base case
    if lst == []:
        return lst 
    # pairneg recursion removes the first element of the list
    else: 
        return [[lst[0], -lst[0]]] + pairneg(lst[1:])

testing = pairneg([1])
#print(testing)

# question 2b
"""def cap(m, lst):
    for num in lst:
        if num >= m:
            
            # replace every element in lst that's greater than m with m
        else: 
            pass """

def cap(m, lst):
    for i, num in enumerate(lst):
        if num >= m:
            lst[i] = m
    return lst

testing_two = cap(5, [1, 2, 3])
#print(testing_two)

# question 2c
"""def prefix(s, l):
    if not l:
        return []
        """

# question 2d
def short(lst):
    for strings in lst:
        if len(strings) > 5:
            return "too long"
        else:
            return strings

testing_three = short(["hello", "world"])
#print(testing_three)

# question 2e
def within(a, b, lst):
    lt = []
    for temp in lst:
        if temp > a and temp < b:
            lt.append(temp)
        elif temp < a and temp > b:
            lt.append(temp)
# question 2f
def split(m, lst):
    lt = []
    lt1 = []
    for temp in lst:
        if temp <= m:
            lst.append(lt)
        elif temp > m:
            lst.append(lt1)
    return lt, lt1 

# question 3a
def vscale(a, v):
    if not a:
        return []
    else:
        return [v * x for x in vscale(a - 1, v)]
testing_four = vscale(1.0, [1.0, 2.0, 3.0])
#print(testing_four)

# question 3b (non-recursive version)
"""def vadd(v, w, seq=None):
    if seq is None:
        return []  
    seq.append()  
    #else:
        #return vadd(v, w, seq)

tests = vadd(10, 20)
#print(tests)"""

# works but implemented with for loop
def vadd(v, w):
    return sum([vi + wi for vi, wi in zip(v, w)])

tests = vadd([10, 20, 30], [20, 40, 60])
#print(tests)
"""
def vadd(v, w, seq=None):
    if seq is None:
        return []
    seq.append(zip(v, w))"""

# question 3c
import math 
def vlength(v):
    for temp in v:
        temp2 = v[temp] ** 2
    sums = sum(temp2)
    math.sqrt(sums)

# question 3d
def vproduct(v, w):
    res_list = []
    for i in range(0, len(v)):
        if i == []:
            return 0
        else:
            res_list.append(v[i] * w[i])
