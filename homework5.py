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


# Question 2
"""
The goal of question 2 is to write a CPU simulator to understand how it runs a program. This simulator is a software implementaiton of a CPU based on a program I give the function (a set of instructions).

CPUs are the primary component on computer hardware today and perform most processing tasks. They fetch instructions form memory and execute them. 
"""
# A*
""" 
Registers hold *any* type of data that the processor needs to manipulate or access quickly (ex: logical operations), while a cache is memory of a specific data type that holds frequently accessed data in a central location (below main memory but above registers) for fast access. 

Registers, because of their ability to manipulate or quickly access data, are located on the processor. 
"""
# the program returns true if the sum of the value in the first two registers is equal to the value in the 3rd register
p_plus = [
  {
    "REGISTER": ("X", 3)
  },
  {
    "REGISTER": ("Y", 4)
  },
  {
    "REGISTER": ("Z", 7)
  },
  # add values in the 2 registers
  {
    "ADD": ("X", "Y")
  },
  # compare the results of addition with value in the Z register
  {
    "CMP": ("Z", "ADD")
  },
  # if the value of 3 + 4 = 0, this is the conditional jump that gives control to the instruction at the label where the value is zero, the control would be transfered to the fail label, which results in FALSE and the program is exited.
  {
    "JZ": "done"
  },
  {
    "FALSE": None
  },
  {
    "LABEL": "done"
  },
  # if the program is not 0, in which case the execution was successful and the correct value is given, the value jumps to TRUE and the program is exited.
  {
    "TRUE": None
  }
]


# program is a parameter that takes in a list of dictionary values as instructions, similar to p_plus
def run_cpu(program):
  # the variables before the while loop, registers and pc, are initializations that change in the code below.
  registers = {"X": 0, "Y": 0, "Z": 0, "ADD": 0}

  # pc is program counter. this value represents the index of the current instruction in the program list. hence, why the while loop makes sense; as the value of pc is incrementing by 1, it will get bigger than the program (total num of vals in dictionary) and there will be nothing for run_cpu to execute so the execution will stop
  pc = 0

  while pc < len(program):
    # the instruction at the moment of the loop is the index of program input (similar to p_plus)

    instruction = program[pc]

    # initialize two temporary variables for the key : value pair in the instruction variable
    # using the next, iter syntax because it lets programmers begin with the first item in the program param input instead of trying to index a value, knowing the indexing is random
    op, args = next(iter(instruction.items()))

    if op == "REGISTER":
      # tuple unpacking means we assign the variables reg, val to args, because we have multiple data types in the p_plus variable, we need to use this method to unpack
      reg, val = args
      # value in register dictionary is updated based on its key
      registers[reg] = val
    # if the operation is add, sum their values
    elif op == "ADD":
      reg1, reg2 = args
      registers["ADD"] = registers[reg1] + registers[reg2]
    # adding a "SUB" statement to this function
    elif op == "SUB":
      reg1, reg2 = args
      registers["SUB"] = registers[reg1] - registers[reg2]
    # adding a "MAX" statement to address question 3
    elif op == "MAX":
      reg1, reg2 = args
      registers["MAX"] = max(registers[reg1], registers[reg2])
    # if the operation is compare, check if the two register keys are the same and if they are, then set the register equal to 1
    elif op == "CMP":
      reg1, reg2 = args
      if registers[reg1] == registers[reg2]:
        registers["Z"] = 1
        # if the registers are not the same, set the value to 0. btw - before programming this I did not know elif statements could hold their own if/else logic as nested parts
      else:
        registers["Z"] = 0
    elif op == "JZ":
      label = args
      # jump instruction that redirects the instructions if the output ("Z") is 1
      if registers["Z"] == 1:
        pc = label_to_pc(program, label)
    # question 4
    elif op == "DIFF":
      # set DIFF to the absolute difference of the two specified registers
      reg1, reg2 = args
      registers["DIFF"] = abs(registers[reg1] - registers[reg2])
      # compute the first two abs value, store it, and compare it to register Z
      if registers["DIFF"] == registers["Z"]:
                registers["Z"] = 1
      else:
        registers["Z"] = 0
    elif op == "FALSE":
      return False
    elif op == "TRUE":
      return True
    pc += 1
  # question 1: Return None
  # Return True or False based on the value of register "Z"
  # question 2: return True if registers["Z"] == 1 else False
  #return True if registers["Z"] == 1 and registers["MAX"] == registers["Z"] else False
  return True if registers["Z"] == 1 and registers["DIFF"] == registers["Z"] else False

def label_to_pc(program, label):
  # iterates through program (same p_plus that's labelled above but assigns an index for each item in the list)
  for i, instr in enumerate(program):
    # returns index if "LABEL" is in instr and the "LABEL" is a key in instr iterator
    if "LABEL" in instr and instr["LABEL"] == label:
      return i
  raise ValueError(f"Label '{label}' not found in program")


# B
p_sub = [{
  "REGISTER": ("X", 5)
}, {
  "REGISTER": ("Y", 2)
}, {
  "REGISTER": ("Z", 3)
}, {
  "SUB": ("X", "Y")
}, {
  "CMP": ("Z", "SUB")
}, {
  "JZ": "done"
}, {
  "FALSE": None
}, {
  "LABEL": "done"
}, {
  "TRUE": None
}]

result = run_cpu(p_sub)
#print(result)

p_max = [
    {"REGISTER": ("X", 5)},
    {"REGISTER": ("Y", 3)},
    {"REGISTER": ("Z", 4)},
    {"MAX": ("X", "Y")},
    {"CMP": ("Z", "MAX")},
    {"JZ": "done"},
    {"FALSE": None},
    {"LABEL": "done"},
    {"TRUE": None}
]
result = run_cpu(p_max)
#print(result)

p_diff = [
    {"REGISTER": ("X", 7)},
    {"REGISTER": ("Y", 3)},
    {"REGISTER": ("Z", 4)},
    {"SUB": ("X", "Y")},
    {"DIFF": ("Z", "SUB")},
    {"CMP": ("Z", "DIFF")},
    {"JZ": "done"},
    {"FALSE": None},
    {"LABEL": "done"},
    {"TRUE": None}
]

result = run_cpu(p_diff)
#print(result)
