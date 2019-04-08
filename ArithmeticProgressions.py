import sys
import time

class ArithmeticProgression (object):  
  # Constructor
  def __init__(self, a, d):
    self.a = a
    self.d = d
    self.terms_list = [self.a]

  # Representation of object as a printable string
  def __repr__(self):
    return "This is an AP with first term as " + str(self.a) + " and the common difference as " + str(self.d)
    
  def addToSequence(self, num_terms):
    for x in range(num_terms):
      self.terms_list.append(self.terms_list[-1] + self.d)
  
  def getTermAtPos(self, pos_n):
    return self.a + self.d * (pos_n - 1)
    
  def getPosOfTerm(self, term):
    return int((term - self.a + self.d) / self.d)
    
  def contains(self, term):
    possible_pos = (term - self.a + self.d) / self.d
    if float(possible_pos) - int(float(possible_pos)) == 0:
      return True
    else:
      return False
  
  def getNextTerms(self, no_of_terms):
    answer = [self.terms_list[-1]]
    
    for x in range(no_of_terms):
      answer.append(answer[-1] + self.d)
      
    answer.pop(0)
    return answer
    
  def getSumNthTerm(self, n):
    return (n/2) * (2 * self.a + (n - 1) * self.d)
  
  def getTermSumSeq(self):
    return sum(self.terms_list)

AP_new = ArithmeticProgression (1, 5) # First term given as first param is automatically added to the series list
print ("\n" + str(AP_new))
AP_new.addToSequence(90)
print ("90 terms have been added to my sequence!\n")
print ("Sum of terms till now is " + str(AP_new.getTermSumSeq()))
print ("The term at position 1000 in my AP is " + str(AP_new.getTermAtPos(1000)))
print ("The next five terms are " + str(AP_new.getNextTerms(5))) # Prints terms 92 to 96
print ("Sum of terms till position 250 is " + str(AP_new.getSumNthTerm(250)))

if AP_new.contains(4000):
  print ("4000 is at position " + str(AP_new.getPosOfTerm(4000)) + " in my AP!")
else:
  print ("4000 was not found in my AP!")

# time.sleep(3)