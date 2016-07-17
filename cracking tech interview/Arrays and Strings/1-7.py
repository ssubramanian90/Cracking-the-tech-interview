'''Hash Tables'''

'''ArrayList'''
'''resizes itself as needed. When a vector is full,
the array doubles in size. O(1)'''

'''StringBuffer'''
'''Running time=O(n^2)'''



"""Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column is set to 0."""

import numpy as np
def replaceelements(amatrix):
    newmatrix=amatrix
    for row in amatrix:
        for i in row:
            if i==0
                newmatrix[[row][i] for row in newmatrix]=0
    return newmatrix


