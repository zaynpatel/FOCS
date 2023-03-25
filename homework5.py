# practice problem for partial
# partial functions mean there is not a return value for all of the inputs

import math


def iroot(m):
  n = int(math.sqrt(m))
  if n * n == m:
    return n
  else:
    return None


# Question 1
# A*
# create a function that takes in any number of arguments
def null_pfn():
  # takes in one input and always returns None
  def partial_func(x):
    return None

  # doesn't matter what value of x is, always be None
  return partial_func


# B*
def extend_pfn(a, b, pf):

  def partial_func(x):
    if x == a:
      return b
    else:
      return pf(x)

  return partial_func


# BB
def complement_pfn(f):

  def new_partial_function(x):
    if f(x) is None:
      return None
    else:
      return not f(x)

  return new_partial_function


# C
def join_pfn(pf1, pf2):
  # partial function because it returns a value only if pf1 and pf2 have values that are defined
  def joined_pfn(x):
    # check if input is defined
    if pf1(x) is not None:
      # return pf1 'on that input' if it is defined
      return pf1(x)
    else:
      # otherwise, return what pf2 returns on that input
      return pf2(x)

  # return partial function
  return joined_pfn


# D (part 1) - creating total functions
def default_pfn(d, pf):

  def partial_pfn(x):
    if x is not None:
      return pf(x)
    else:
      return d

  return partial_pfn


# D (part 2)
def fail_pfn(pf):

  def failed_pfn(x):
    if pf(x) is not None:
      return pf(x)
    else:
      raise Exception("undefined")

  return failed_pfn


# E*     
def mk_dict(ps):
  # given a list of pairs (as a list) which it converts to a dictionary 
  # in the prior case of having a list, we wouldn't be able to loop through values as cleanly because they can be multiple types in a list and ints aren't iterable so we'd have to type convert all values to strings, which are iterable and use nested loops to get the value
  d = dict()
  for k, v in ps:
    # assigns value (v) to the dictionary key (k)
    d[k] = v 
  def dict_lookup(key):
    if key in d:
      return d[key]
    else:
      raise Exception("Key not found: {}".format(key))
  return dict_lookup 
