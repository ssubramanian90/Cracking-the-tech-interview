
"""Given a sorted (increasing order) array, write an algorithm to create a binary tree with
minimal height."""


class BinaryTree:
     def __init__(self, root, left=None, right=None):
        self.key = root
        self.left_child = left
        self.right_child = right
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

def createbtreewitharray(aarray):
     if aarray== []:
          return None
     elif len(aarray)==1:
          return BinaryTree(aarray[0])
     else:
          return BinaryTree(array[len(array)/2], createbtreewitharray[0:len(array)/2], createbtreewitharray[len(array)/2:])
      

