



"""Describe how you could use a single array to implement three stacks."""


from pythonds.basic.stack import Stack

'''class Stack:
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
         return len(self.items)'''


#Approach 1

def threestacks(aarray):
    s1=s2=s3=Stack()
    for i in range(len(aarray)/3):
        s1.push(aarray[i])
    for i in range(2*len(aarray)/3) :
        s2.push(aarray[i])
    for i in range(2*len(aarray)/3) :
        s3.push(aarray[i])
