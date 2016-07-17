"""How would you design a stack which, in addition to push and pop, also has a function
min which returns the minimum element? Push, pop and min should all operate in
O(1) time"""

from pythonds.basic.stack import Stack

class Stack:
     def __init__(self):
         self.items = []
         slef.minimum=[]

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)
         if item<=self.minimum[-1] or not self.minimum:
                self.minimum.append(item)

     def pop(self):
        if self.items.pop()==self.minimum[-1]:
            self.minimum.pop()
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def min(self):
         return self.minimum[-1]


 
    
            

