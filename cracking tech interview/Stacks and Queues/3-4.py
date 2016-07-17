
"""Tower of Hanoit problem"""

from pythonds.basic.stack import Stack

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        print ("moving disk",fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

