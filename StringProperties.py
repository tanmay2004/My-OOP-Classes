class StringProperties(object):
  
  def __init__(self, str):
    self.str = str
  
  def __repr__(self):
    return self.str
    
  def getVowelsNum(self):
    vowel_list = ["a", "e", "i", "o", "u"]
    ans = 0
    
    for char in self.str:
      if char.lower() in vowel_list:
        ans += 1
    
    return ans
    
  def getWords(self):
    return len((self.str).split())
    
  def getChars(self):
    numOfLetters = 0
    
    for char in self.str:
      if char.isalpha():
        numOfLetters += 1
    
    return numOfLetters

new_prop = StringProperties("The quick brown fox jumps over the lazy dog.") # This is known as a panagram!
print ()
print (new_prop)
print (str(new_prop.getVowelsNum()) + " vowels were found!")
print (str(new_prop.getChars()) + " characters are there in your sentence!") 
print (str(new_prop.getWords()) + " words are there in your sentence!")