'''Hash Tables'''

'''ArrayList'''
'''resizes itself as needed. When a vector is full,
the array doubles in size. O(1)'''

'''StringBuffer'''
'''Running time=O(n^2)'''



"""Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?"""
from numpy import matrix
from numpy import linalg
def rotateimage(aimage):
    transposeimage= [[row[i] for row in aimage] for i in range(aimage)]
    #Rotate by 90
    return np.matrix(row.reverse() for row in transposeimage)
    # Rotate by -90
    return np.matrix([row[i] for row in transposeimage]for i in range(transposeimage)])


from iterables import chain
import numpy as np
import sys,math
def rotateimage(aimage):
    alist=list(chain.from_iterable(aimage))
    aline=''.join(alist)
    n=int(math.sqrt(len(aline)))
    output=''
    for i in range(len(aline)):
        index=n*(n-1-i%n)+int(i/n)
        output+=aline[index]+' '

    return np.matrix(ouput.rstrip())

