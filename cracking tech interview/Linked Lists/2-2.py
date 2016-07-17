'''Hash Tables'''

'''ArrayList'''
'''resizes itself as needed. When a vector is full,
the array doubles in size. O(1)'''

'''StringBuffer'''
'''Running time=O(n^2)'''



"""Implement an algorithm to find the nth to last element of a singly linked list."""

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
       def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def findnthtolast(self, n):#Don't have the length
        current=self.head
        marker=self.head
        i=1
        while i<=n:
                marker=marker.getNext()

        while marker.getNext()!=None:
            current=current.getNext()
            marker=marker.getNext()

        return current

    def findnthtolast(self, n):#Recursion
        current=self.head
        marker=self.head
        for i in range(n)
              if marker is None:
                    return None
              marker=marker.getNext()
              if marker is None:
                  return current
              else:
                  return findnthtolast(current.next,n)
 
    
            

