



"""Write code to remove duplicates from an unsorted linked list."""


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

    def removeduplicateswithbuffer(self):
        current=self.head
        previous=None
        duplicates={}
        while current !=None and not found:
            if duplicates.has_key(current.getData()):
                current=current.getNext()
                previous.setNext(current)
            else: 
                duplicates[current.getData()]=True
                previous=current
                current=current.getNext()
                
     def removeduplicateswithoutbuffer(self):
        current=self.head
        previous=None
        nextone=current.getNext()
        while current !=None and not found:
            while nextone!=None:
                if nextone.getData()== current.getData():
                    nextone=nextone.getNext()
                    previous.setNext(nextone)
                else:
                    previous=nextone
                    nextone=nextone.getNext()
            previous=current
            current=current.getNext()
            nextone=current.getNext()    
            
