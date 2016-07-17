

"""
#Write a program to sort a stack in ascending order.
You should not make any assumptions about how the stack is implemented. 
#The following a"""

from pythonds.basic.stack import Stack

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def sortstacks(astack):
     temp=Stack()
     while not astack.isEmpty():
          tmp=astack.pop()
          while temp.peek()<tmp:
               temp.pop()
          temp.push(tmp)
     return temp

