# legend: star (*) next to letter means I had to debug. 
# Question 1
"""
finite_automata = {
states: int list, 
alphabet: character list, 
delta: (int * char * int) list,
start: int,
final: int list
}
"""

"""
Accepts set of strings over ['x', 'y'] that contains a number of xs that is a multiple of 3
"""

faMod3x = {
  'state': [1, 2, 3],
  'alphabet': ['x', 'y'],
  'delta': [(1, 'x', 2), 
            (2, 'x', 3), 
            (3, 'x', 1), 
            (1, 'y', 1), 
            (2, 'y', 2), 
            (3, 'y', 3)],
  'start': 1,
  'final': [1]
}

faStartXEndZ = {
  'states': [0, 1, 2],
  'alphabet': ['x', 'y', 'z'],
  'delta': [(0, 'x', 1), 
            (1, 'x', 1), 
            (1, 'y', 1), 
            (1, 'z', 2), 
            (2, 'x', 1), 
            (2, 'y', 1), 
            (2, 'z', 2)],
  'start': 0,
  'final': [2]
}

# A* (logic correct, had to debug scope)
def isFinal(m, q):
  for temp, temps in m.items():
    if temp == 'final':
      if temps == q:
        return True
  return False
#trying = isFinal(faMod3x, [2])

# B


# Question 3
# A 
def sets(xs):
    return set(xs)

# B* (added found)
def set_sub(s, t):
  for sub in s:
    found = False
    for subs in t:
      if sub == subs:
        found = True
        break 
    if not found:
      return False
  return True

# C* (added elif with subsets)
def set_equal(s, t):
  # check for length of sets otherwise default False
  if len(s) != len(t):
    return False
  # base case to check for empty lists
  elif not s and not t:
    return True
  elif set(s).issubset(set(t)) and set(t).issubset(set(s)):
    return set_equal(s[1:], t[1:])
  else:
    return False

# D 
def set_union(s, t):
  union = []
  not_included = []
  for temp in s:
    if temp in union:
      not_included.append(temp)
    elif temp not in union:
      union.append(temp)
  for temps in t:
    if temps in union:
      not_included.append(temps)
    elif temps not in union:
      union.append(temps)
  return union

# D (with recursion)
def set_unions(s, t):
  if not s and not t:
    return []
  if not s:
    return t
  if not t:
    return s
  # [] around s and t in lines 58, 60 because we want to return a concatenated list w/element
  # and recursive steps instead of two separate lists (this would be case if no brackets)
  elif s[0] == t[0]:
    return [s[0]] + set_unions(s[1:], t[1:])
  else:
    return [s[0], t[0]] + set_unions(s[1:], t[1:])
  
# E
def set_intersection(s, t):
  intersection = []
  for val in s:
    for vals in t:
      if val == vals:
        intersection.append(val)
  return intersection

#recursion practice

#4* (not operator negates boolean value of operand. if lst is empty or not)
def sum_of_list(lst):
  if not lst:
    return 0
  else:
    return lst[0] + sum_of_list(lst[1:])
