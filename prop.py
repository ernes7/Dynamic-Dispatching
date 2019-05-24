import pic

class Prop:
  def equality(self):
    return False
  def not_equality(other, self):
    return False

class TRUE(Prop):
  def __str__(self):
    return 'TRUE'
  def apic(self):
    return pic.apic('TRUE')
# *******************************
  def vars(self):
    return []
  def eval(self):
    return True

  def equality(self):
    return True
# *******************************

class FALSE(Prop):
  def __str__(self):
    return 'FALSE'
  def apic(self):
    return pic.apic('FALSE')
# *******************************
  def vars(self):
    return []
  def eval(self):
    return False
# *******************************

class VAR(Prop):
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return self.name
  def apic(self):
    return pic.apic(self.name)
# *******************************
  def vars(self):
    return [self.name]
  def eval(self,other):
    return other[self.name]

  def not_equality(self,other):
    return self.name == other.name
  def __eq__(self,other):
    return other.not_equality(self)
# *******************************

class AND(Prop):
  def __init__(self, p, q):
    self.p = p
    self.q = q
  def __str__(self):
    return 'AND ' + str(self.p) + ' ' + str(self.q)
  def apic(self):
    return self.p.apic().binaryNode('AND', self.q.apic())
# *******************************
  def vars(self):
    return self.p.vars() + self.q.vars()
# *******************************
  def eval(self,other):
    return self.evalHelper(other)
  def evalHelper(self,other):
    return self.p.eval(other) and self.q.eval(other)
# *********************************

class OR(Prop):
  def __init__(self, p, q):
    self.p = p
    self.q = q
  def __str__(self):
    return 'OR ' + str(self.p) + ' ' + str(self.q)
  def apic(self):
    return self.p.apic().binaryNode('OR', self.q.apic())
  # *******************************
  def vars(self):
    return self.p.vars() + self.q.vars()
# *******************************
  def eval(self,other):
    return self.evalHelper(other)
  def evalHelper(self,other):
    return self.p.eval(other) or self.q.eval(other)
# *************************************

class NOT(Prop):
  def __init__(self, p):
    self.p  = p
  def __str__(self):
    return 'NOT ' + str(self.p)
  def apic(self):
    return self.p.apic().unaryNode('NOT')
  # *******************************
  def vars(self):
    return self.p.vars()
#***********************************
  def eval(self,other):
    return self.evalHelper(other)
  def evalHelper(self,other):
    return not self.p.eval(other) 
#*********************************

# *******************************
#self.p.eval(other) and self.q.evals(other)

# The following should print True ... but you'll need to
# make some changes to the code before it works properly.
print(VAR("A") == VAR("A"))

# The next section of code constructs some Prop abstract
# syntax trees ...
a       = VAR("A")
b       = VAR("B")
c       = AND(a,b)
t       = TRUE()
n       = NOT(a)
left    = AND(a, NOT(b))
right   = AND(NOT(a), b)
example = OR(left, right)

# Print out the example expression in text and tree forms:
#print(example.eval({'A': True, 'B': False}))
#print(left.eval({'A': True, 'B': False}))
#print(right.eval({'A': False, 'B': True}))
#print(n.vars())
#print(a.vars())
#print(b.vars())
#print(c.vars())
#print(right.vars())
#print(left.vars())
#print(example.vars())
#print(example)
#print(example.apic())


# ... and then puts some of them together in a list:
list = [TRUE(), TRUE(), left, right, OR(left, right), example]

# Here is a function that you can use for testing.  It takes a list
# of Prop values as inputs, and then displays (a) some diagrams
# showing the structure of each of the expressions; and (b) a table
# that shows the results of comparing each of the Prop values in
# the list against all of the other items.
def eqTests(list):
  # Construct and print a picture of all the trees in list:  (You are
  # not expected to understand exactly how this part of the code works)
  pics = pic.hstrut(0)
  for p in list:
    pics = pics.top(pic.hstrut(3).top(p.apic().pic))
  print(pics)
  # Compare the examples in the given list with one another and display
  # the results in a simple table:
  for l in list:
    for r in list:
      print('Y' if l==r else '-', end='\t')
    print(l)

# Run some tests:
#eqTests(list)

