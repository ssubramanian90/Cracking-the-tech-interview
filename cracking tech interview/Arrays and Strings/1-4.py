'''Hash Tables'''

'''ArrayList'''
'''resizes itself as needed. When a vector is full,
the array doubles in size. O(1)'''

'''StringBuffer'''
'''Running time=O(n^2)'''



"""Write a method to decide if two strings are anagrams or not"""

def checkanagrams(astring1, astring2):
    return (set(astring1)==set(astring2))
