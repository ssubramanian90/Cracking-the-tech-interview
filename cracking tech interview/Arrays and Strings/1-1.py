'''Hash Tables'''

'''ArrayList'''
'''resizes itself as needed. When a vector is full,
the array doubles in size. O(1)'''

'''StringBuffer'''
'''Running time=O(n^2)'''



"""Implement an algorithm to determine if a string has all unique characters. What if you
can not use additional data structures?"""

def unique(astring):
    return (len(set(astring))==len(astring))# since strings are iterable, set(string) will give us all the unique characters in a string.
