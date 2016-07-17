



"""Implement a function to check if a tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
from the root by more than one."""


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

def treebalancing(atree):
        if abs(maxdistance(atree)-mindistance(atree))<2:
            return True
        else:
            return False

def maxdistance(atree):
    if atree= None or atree.get_left_child= None or atree.get_right_child==None:
        return 0
    elif atree.get_left_child!=None and atree.get_right_child==None:
        return 1+maxdistance(atree.get_left_child)
    elif atree.get_right_child!=None and atree.get_left_child==None:
        return 1+maxdistance(atree.get_right_child)
    else:
        return 1+max(maxdistance(atree.get_left_child), maxdistance(atree.get_right_child))

def mindistance(atree):
    if atree= None or atree.get_left_child= None or atree.get_right_child==None:
        return 0
    elif atree.get_left_child!=None and atree.get_right_child==None:
        return 1+mindistance(atree.get_left_child)
    elif atree.get_right_child!=None and atree.get_left_child==None:
        return 1+mindistance(atree.get_right_child)
    else:
        return 1+min(mindistance(atree.get_left_child), mindistance(atree.get_right_child))
