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


# B* (logic partially correct, added new temp vars)
def followSymbol(m, q, sym):
  # specify the key we want to loop through
  for source, label, dest in m['delta']:
    #print(source, label, dest)
    if source == q and label == sym:  
      return dest
  return []
#trying = followSymbol(faMod3x, 3, 'x')

# C
def followString(m, q, syms):
    # new var equal to state param
    state = q
    # update the value of state as it loops through the list of symbols
    for sym in syms:
        state = followSymbol(m, state, sym)
        if not state:
            return []
  # return as a 1 item list  
  return [state]

#trying = followString(faMod3x, 1, ['x'])

# D
def accept(m, s):
    # Start from the initial state of m
    state = m['start']
    # Follow the transitions of m labeled by the symbols in s
    final_state = followString(m, state, list(s))
    # Check if the final state is in the set of accept states of m
    return final_state in m['accept']

# Question 2 - Finite state machine pictures on github
"""
* Only including self.alphabet and self.start because they are needed to initialize the FSM. Accepting state, transition are two separate functions we can initialize later.

__init__ is typically used to prepare a class for 'use'


"""
"""class FA_A: 
  # used to set up the initial parts of FSM (alphabet and start)
  def __init__(self):
    self.alphabet = ['a', 'b', 'c']
    self.start = 0
  # two final states accepted in this machine
  def is_accepting(self, state):
    return state == 0 or state == 1
  def transition(self, state, symbol):
    length = state + (1 if symbol in self.alphabet else 0)
    return length % 3

import random
def recognize(fa_a, n):
  for i in range(n):
    # random.choice() returns randomly selected element from sequence
    length = random.choice([])"""

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
