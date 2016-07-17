



"""Given a binary search tree, design an algorithm which creates a linked list of all the
nodes at each depth (eg, if you have a tree with depth D, you’ll have D linked lists)."""


class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None
    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
            return self.right_child

    def get_left_child(self):
            return self.left_child

    def set_root_val(self, obj):
            self.key = obj
    def get_root_val(self):
            return self.key

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

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

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

def BSTdepth(atree):
    maxdepth=0
    current=0
    if atree.get_root_val() is None:
        return -1
    else:
        if atree.get_left_child() is not None or atree.get_right_child() is not None:
            current+=1
            if current>maxdepth:
                maxdepth=current
            BSTdepth(atree.get_left_child())
            BSTdepth(atree.get_right_child())
            return maxdepth



def createlistwithbtree(atree):
     if atree is None:
         return []

      r=[[atree.get_root_val()]]
      queue=[atree]
      while len(queue)>0:
          newq=[]
          for node in queue:
              if node.left_child is not None:
                  newq.append(node.left_child)
              if node.right_complete is not None:
                  newq.append(node.right_child)
          queue=newq
          if len(queue)==0:
              break
       r.append([i for i in q])
       return r


def createlinkedlistwithbtree(atree, depth=1, alist) :
    
    llist=UnorderedList()
    llist.add(atree.get_root_val)
    if len(alist)>=depth:
        llist.setNext(alist[depth-1])
        alist[depth-1]=llist
    else:
        alist.append(llist))       
    if atree.get_left_child() is not None:
         alist=createlinkedlistwithbtree(atree.get_left_child(), depth+1, alist)
    if atree.get_right_child() is not None:
         alist=createlinkedlistwithbtree(atree.get_right_child(), depth+1, alist)
    return alist
