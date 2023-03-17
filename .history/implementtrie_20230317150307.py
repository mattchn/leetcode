class Trie(object):
   def __init__(self):
      self.children = [None] * 26
      self.isEndOfWord = False
   
   def insert(self, word):
      node = self.root
      for c in word:
         index =