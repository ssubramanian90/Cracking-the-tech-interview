'''Hash Tables'''

'''ArrayList'''
'''resizes itself as needed. When a vector is full,
the array doubles in size. O(1)'''

'''StringBuffer'''
'''Running time=O(n^2)'''



"""Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer. """

def removeduplicates(astring):
    removeddupstring=[]
    for c in astring:
        if c not in removeddupstring
        removeddupstring.append(c)

    return ''.join(removeddupstring)


from collections import OrderedDict
def removeduplicates(astring):
    return "".join(OrderedDict.fromkeys(astring))
