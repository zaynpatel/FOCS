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
print(trying)

# Question 2
# A 
