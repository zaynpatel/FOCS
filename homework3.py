# practice 
def squares(lst):
  if lst == []:
    return []
  else:
    return [x * x for x in lst]
    #return [lst[0] * lst[0]] + [squares(lst[1:])]

#trying = squares([1, 2, 3])

# Question 1
# A (cleaned up code)
def increment_non_zero(lst):
  int_list = []
  #zero_el = []
  for val in lst:
    #if val == 0:
      #zero_el.append(val)
    if val != 0:
      int_list.append(val + 1)
  return int_list

#trying = increment_non_zero([-1, 0, 2, 0, -3])

# practice for B (one without a function, one with a function)
def cap_name(lst):
  return [x.capitalize() for x in lst]

#trying = cap_name(['alice', 'bob', 'charlie', 'david'])
#names = ['alice', 'bob', 'charlie', 'david']
#capitalized_names = list(map(lambda x: x.upper(), names))
#print(capitalized_names)
  
# B* (modified operation(x). b/f correction it was operation * x)
def map_functions(fs, x):
  return [operation(x) for operation in fs]

  #trying = map_functions([(lambda x: x + 1), (lambda x: x + 99)], 10)

# C* (define inner function)
# use the args syntax because we're accepting a variable number of arguments
# use x = f(x) because I'm composing functions for the final output
# fundamentally, I'm defining a sequence of steps inside another sequence of steps. hence, nested functions. not higher order because I'm not passing one function into another. 
def compose_all(*output):
  def inner(x):
    for f in output:
      x = f(x)
    return x 
  return inner

#f = compose_all(lambda x: x + 1)
#trying = f(10)

# D* (first implementation was very off, too complicated)
def pairs1(x, ys):
  return [(x, y) for y in ys]

#trying = pairs1(9, ['a', 'b', 'c'])

# E* (knew this logic but did something more complicated)
def pairs(xs, ys):
  result = []
  for x in xs:
    for y in ys:
      result.append((x, y))
  return result 

trying = pairs([1, 2], ['a', 'b', 'c'])

# Question 2
# A* (wrapped a in a list so the type was accepted, wasn't going to concatenate the lists otherwise. I can feed a in as an int but because of the function running, it's converted to a list) 
def prepend_to_all(a, xss):
  return list(map(lambda x: [a] + x, xss))

#trying = prepend_to_all(1, [[66]])

#B* (remember that order of el in 83 should abide by the order of el in 73 -> pass same param-like objects in to the HOF)
def prefixes(xs):
  # empty list is a prefix of any list, hence why empty list is initialized with result
  result = [[]]
  for item in xs:
    result.append(prepend_to_all(item, result))
  return result
#trying = prefixes([1])

#C 
# helper function define
def helper_reverse(lst):
  return lst[::-1]

def suffixes(xs):
  result = [[]]
  for item in xs:
    result.append(prepend_to_all(item, result))
  return helper_reverse(result)

#D 
from itertools import combinations
def partitions(lst):
  result = [[]]
  n = len(lst)
  for i in range(n+1):
    # from combinations formula: n, k. n is the number of lists in the function parameter, k is the number of 'choosing' objects. k is represented by i in this function. 
    for combo in combinations(lst, i):
      xs1 = list(combo) 
      xs2 = [x for x in lst if x not in xs1]
      result.append((xs1, xs2))
  return result 

#E*
def insert(x, xs):
  result = []
  # loop through to find all possible partions of the inserted list
  for p in partitions(xs):
    # loops through the partitions and inserts [x] into the current partition
    for i in range(len(p)+1):
      result.append(p[:i] + [x] + p[i:])
  return result 

# practice
# 1* (always use temporary variables when appending the loop)
# if .append((a, b)) -> this would append the lists, not the indexes as the problem stated
def prob_one(a, b):
  new_list_c = []
  for temp in a:
    for temps in b:
      prob_one.append((temp, temps))
  return new_list_c

# 2
def triangles(n):
  for i in range(1, n+1):
    print("*" * i)

#trying = triangles(17)

# 3
"""
Prompt: Given two input lists a and b, write a function common_digits(a, b) that returns a list of all pairs of numbers (x, y) where x and y have at least one digit in common. 
"""
# wrong implementation - would return numbers not digits. I knew this so I built commoner digits.
def common_digits(a, b):
  result = []
  for num in a:
    for nums in b:
      if num in nums:
        result.append((num, nums))
  return result 

# not looping over digits. I'm looping over the digits of the number. In other words, the output won't be correct because the loop isn't doing the correct thing.
"""def commoner_digits(a, b):
  results = []
  for num in a:
    for nums in num:
      for numbers in b:
        for numeros in numbers:
          results.append((nums, numeros))"""

# can also implement this with sets instead. still ugly but built-in set types of no duplicates means we don't need to check (if digit == digit 2)
def commoner_digits(a, b):
  results = []
  for num in a:
    # added str(num) because this allows us to loop through individual digits. can't do it with numbers. 
    for digit in str(num):
      for nums in b:
    # same idea here with type change. 
        for digit2 in str(nums):
          if digit == digit2:
            results.append((num, nums))
            # break because we only need one digit to   confirm
            break
  return results

# more practice - except with map, filter, reduce
#1 (recall sum, len for line 137 - which method should be here?)
def count_vowels(string):
  vowels = ['a', 'e', 'i', 'o', 'u']
  final = []
  for vowel in string:
    if vowel in vowels:
      final.append(vowel)
  return len(vowel)

"""
from functools import reduce

def count_vowels(string):
  vowels = ['a', 'e', 'i', 'o', 'u']
  filtered = filter(lambda x: x in vowels, string) -> filter for x (a func parameter) that is in vowels. ,string sharing that you're going to filter on the string input parameter

  return reduce(lambda x, y: x + 1, filtered, 0) -> reduce combines the elements of an input iterable into a single result. so here it's incrementing by 1 for the items in filtered and will return a value at the end.
"""

#2 
def double_odd(nums):
  filtered = filter(lambda x: x % 2 != 0, nums)
  mapping = list(map(lambda x: x * 2, filtered))
  print(mapping)

#3* (add x + y because of sum. obvious.)
from functools import reduce
def sum_squares(nums):
  mapping = list(map(lambda x: x*x, nums))
  return reduce(lambda x, y: x + y, mapping, 0)

#4
def capitalize_words(words):
  mapping = list(map(lambda cap: cap.capitalize(), words))
  return mapping 

#5*
def reverse(string):
  words = string.split()
  reversed_words = map(lambda x: x[::-1], words)
  return ' '.join(reversed_words)

#6
def string_list(lst):
  mapping = list(map(lambda x: len(x), lst))
  return mapping
