



"""Given a directed graph, design an algorithm to find out whether there is a route between
two nodes."""

from pythonds.graphs import Graph
from pythonds.queue import Queue

class Vertex:
     def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
     

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices+ = 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

# Recursion
def graphconnection(agraph, anode1, anode2):
     if anode1!=None and anode1 is anode2:
          return True
     elif anode1=None and anode1 is anode2:
               return False
     nodefound= False
     for neighbour in anode1.getConnections:
          pathfound=graphconnection(agraph, neighbour, anode2)
          if pathfound:
               break
     return pathfound
          
#bfs
def graphconnection(agraph, anode1, anode2):
     if anode1!=None and anode1 is anode2:
          return True
     elif anode1=None and anode1 is anode2:
               return False
     allvisited=set([anode1, anode2])
     aqueue=deque([anode1])
     while len(aqueue)>0:
          node=aqueue.pop()
          for neighbour in node.getConnections:
               if neighbour is anode2:
                    return True
               elif neighbour not in allvisited:
                    allvisited.add(neighbour)
                    aqueue.append(neighbour)
     return False
     
