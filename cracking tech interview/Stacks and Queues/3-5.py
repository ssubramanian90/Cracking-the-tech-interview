

"""Implement a MyQueue class which implements a queue using two stacks."""

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


class Queue:
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def enqueue(self,item):
        self.stack1.push(item)

    def dequeue(self):
        for i in range(0,len(self.stack1) -1):
            self.stack2.push(self.stack1.pop())
        popped=self.stack2.pop()

         for i in range(0,len(self.stack2) -1):
            self.stack1.push(self.stack2.pop())

        
        return popped
            
