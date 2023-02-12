# question 1a
def clamp(a, b, v):
    # determine lower and upper bounds
    low, high = min(a, b), max(a, b)
    # want it to compare max of low and v to make sure v is not lower than low and compare max to high to ensure v is not higher than high.
    return min(high, max(low, v))

# question 1b
def interpolate(a, b, c):
    return c * (b - a) + a 

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

# question 1e
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

# question 2b
def cap(m, lst):
    for i, num in enumerate(lst):
        if num >= m:
            lst[i] = m
    return lst

# question 2c
def prefix(s, lst):
    # base case
    if lst == []:
        return []
    if s == "":
        return []
    else: 
        return [s + x for x in prefix(s, lst[1:])]
        
# question 2c
def suffix (s, lst):
    if s == "":
        return []
    elif lst == []:
        return []
    else: 
        return [x + s for x in suffix(s, lst[1:])]

# question 2d
def short(lst):
    seq = []
    seq_long = []
    for strings in lst:
        if len(strings) > 5:
            seq_long.append(strings)
        else:
            seq.append(strings)
    return seq

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
