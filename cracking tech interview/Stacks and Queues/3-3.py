
"""Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
in real life, we would likely start a new stack when the previous stack exceeds
some threshold. Implement a data structure SetOfStacks that mimics this."""

from pythonds.basic.stack import Stack

class Stack:
     def __init__(self, height):
         self.stacks= []
         if height<1:
            raise NameError("Can't have that height")
         else:
             self.height=height
             
     def isEmpty(self):
         return self.stacks == []

     def push(self, item):
         if self.stacks==[]:
             self.stacks.append([item])
         else:
             if len(self.stacks[-1])>=self.height:
                 self.stacks.append([item])
             else:
                 self.stacks[-1].append(item)
        
     def pop(self):
         if self.stacks==[]:
             raise NameError("Can't pop this stack")
         else:
             popped = self.stacks[-1][-1]
             if len(self.stacks[-1])==1:
                 del self.stacks[-1]
             else:
                 del self.stacks[-1][-1]   
             return popped
        
    def popAt(self, index):
          if self.stacks==[]:
             raise NameError("Can't pop this stack")
         else:
             popped = self.stacks[index-1][-1]
             if len(self.stacks[index-1])==1:
                 del self.stacks[-1]
             elif len(self.stacks)==index:
                 del self.stacks[-1][-1]
             else:
                 self.stacks[index-1][-1]= self.stacks[index][0]

                 for i in range(index, len(self.stacks)):
                     for j in range(0, len(self.stacks[i]):
                         self.stacks[i][j]=self.stacks[i][j+1]
                     if i< len(self.stacks)-1:
                         self.stacks[i][-1]=self.stacks[i+1][0]
                 del self.stacks[-1][-1]
                 if len(self.stacks[-1])==0:
                     del self.stacks[-1]
             return popped   
     

     def size(self):
         return len(self.stacks)
