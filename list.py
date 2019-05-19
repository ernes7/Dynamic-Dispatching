class Nil:
    """ Represents an empty list. """
    def __str__(self): #STEP 2#
    	return 'Nil()'
    def len(self): #STEP 4#
        return 0
    def append(self,other):  #STEP 4#
      return other

class Cons:
    """ Represents a non-empty list. """
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    def __str__(self): #STEP 2#
        return 'Cons(' + str(self.head) + ', ' + str(self.tail) + ')'
    def len(self): #STEP 4#
        return 1 + self.tail.length()
    def append(self, other):  #STEP 4#
        return Cons(self.head, self.tail.append(other))

alist = Cons(1, Cons(2, Cons(3, Nil())))
blist = Cons(4, Cons(5, Cons(6, Cons(7, Nil()))))

def nums(lo, hi):  #STEP 3#
    return Cons(lo, nums(lo+1, hi)) if lo < hi else Nil()

""" Mark Version """
def powers2(n):
    def loop(a ,i):
        return Cons(a, loop(2*a, i-1)) if i>0 else Nil()
    return loop(1,n)

print(str(alist))
