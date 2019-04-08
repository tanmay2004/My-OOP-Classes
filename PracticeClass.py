# My First Python Program with Classes

# This class inherits the functions of the 'object' class
class MyFirstClass(object):

  # This is the contructor of this class
  def __init__(self, var1):
    self.var1 = var1
    
  # The below decides how an object or instance of this class will be 'represented'
  def __repr__(self):
    return "Success!"
    
  # This is a method of this class which may be called on the object
  def getParam(self):
    print (self.var1)

test = MyFirstClass("Testing....")
test.getParam()
print (test) # Runs the __repr__ function