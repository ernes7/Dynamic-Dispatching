class Nil:
    """ Represents an empty list. """
    def __str__(self): #STEP 2#
    	return 'Nil()'
    def length(self): #STEP 4#
        return 0
    def append(self,other):  #STEP 4#
      return other
    def __add__(self,other):  #STEP 5#
      return other
    def map(self,f):  #STEP 6#
        return self
    def filter(self, pred): #STEP 6#
        return self
    def lengthAcc(self, a):      #STEP 7#
        return a
    def sumAcc(self, acc): #STEP 7#
        return acc
    def rev0nto(self, list): #STEP 7#
        return list

    def commaCons(self, s):     #STEP 9#
        return s

    def eqNil(self):         # STEP 10 #
        return False
    def eqNil(self):         # STEP 10 #
        return True
    def __eq__(self, other):  # STEP 10 #
        return other.eqNil() 

# -----------------------------------------------------
############ HW 5 Problem 1 #############
    #def zip(self,other):
     #   return self.zipHelp(other)
    def zip(self,other):
        return self.zipHelp(other)
    def zip2(self,other):
        return ']'
    def zipHelp(other, self):
        return ']'
#--------------------------------------------------- 

class Cons:
# -----------------------------------------------------
############ HW 5 Problem 1 #############
    def zip(self,other):
        return '[' + other.zipHelp(self)
    def zip2(self,other):
        return ' , ' + other.zipHelp(self)
    #def zipHelp(other, self):
        #return Cons((self.head, other.head),self.tail.zip(other.tail))
    def zipHelp(other, self):
        return '(' + str(self.head) + ', ' + str(other.head) + ')' + str(self.tail.zip2(other.tail))
#---------------------------------------------------     
    """ Represents a non-empty list. """
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    def __str__(self): #STEP 2#
        return 'Cons(' + str(self.head) + ', ' + str(self.tail) + ')'
    def length(self): #STEP 4#
        return 1 + self.tail.length()
    def append(self, other):  #STEP 4#
        return Cons(self.head, self.tail.append(other))
    def __add__(self, other):  #STEP 5#
        return Cons(self.head, self.tail + other)
    def map(self,f):  #STEP 6#
        return Cons(f(self.head), self.tail.map(f))
    def filter(self, pred): #STEP 6#
        rest = self.tail.filter(pred)
        return Cons(self.head, rest) if pred(self.head) else rest
    def lengthAcc(self, a):      #STEP 7#
        return self.tail.lengthAcc(1+a)
    def sumAcc(self, acc): #STEP 7#
        return self.tail.sumAcc(acc + self.head)
    def rev0nto(self, list): #STEP 7#
        return self.tail.rev0nto(Cons(self.head, list))
# ---------------------------------------------------
    def commaElements(self):   #STEP 9#
        return self.tail.commaCons(str(self.head))
    def commaCons(self, s):     #STEP 9#
        return s + ', ' + self.commaElements()
# ---------------------------------------------------
    def eqCons(other, self): #STEP 10#
        return False
    def eqCons(other, self): #STEP 10#
        return self.head==other.head and self.tail==other.tail
    def __eq__(self, other):  # STEP 10 #
        return other.eqCons(self)


alist = Cons(1, Cons(2, Cons(3, Nil())))
blist = Cons(4, Cons(5, Cons(6, Cons(7, Nil()))))

def nums(lo, hi):  #STEP 3#
    return Cons(lo, nums(lo+1, hi)) if lo < hi else Nil()

""" Mark Version """ #STEP 3#
def powers2(n):
    def loop(a ,i):
        return Cons(a, loop(2*a, i-1)) if i>0 else Nil()
    return loop(1,n)

""" Testing """
# HW 5.1 #
print(nums(0,6).zip(nums(1,7)))
print(nums(0,6).zip(nums(0,3)))
print(nums(0,3).zip(nums(0,6)))

# 9 #
#print(alist.commaElements())

# 7 #
#print(alist.sumAcc(0))

# 5 #
#print(alist + blist)
#print(blist + alist)
#print((alist + blist).length())
#print(alist + blist.length())

# 1 & 2 #
#print(alist)
#print(blist)

# 3 #
#print(nums(10,15))

# 4 #
#print(alist.length())
#print(blist.length())
#print(alist.append(blist))
#print(blist.append(alist))

