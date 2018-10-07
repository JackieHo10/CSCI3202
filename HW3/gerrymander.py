# Partner List: Phu Dang

from sys import argv
from sys import maxsize
import itertools

script,pass_file = argv

class Node(object):
    def __init__(self, i_depth, i_player, i_remaining, data):
             self.i_depth = i_depth
             self.i_player = i_player
             self.i_remaining = i_remaining
             self.data = data
             self.children = []

    def addchildren(self,obj):
             self.children.append(obj)

    def deletechildren(self,obj):
             self.children.remove(obj)

    def getchildren(self,i):
             return self.children[i]

def utility(matrix,l):
    abstract

def minimax(node, i_depth, player):
    if (i_depth == 0) or (abs(node.data[0]) != maxsize):
        return node.data[0]
    i_bestValue = maxsize * (-player)
    for i in range(len(node.children)):
        child = node.children[i]
        val = minimax(child, i_depth - 1, -player)
        if (player < 0):
            if (val) < (i_bestValue): #Checking which one's closer to the goal of ith player
                i_bestValue = val
        else:
            if (val) > (i_bestValue):
                i_bestValue = val	   
    return i_bestValue

def main():
    if (pass_file == 'smallNeighborhood'):
        data = []
        with open (pass_file) as f:
            for line in f:
                a,b,c,d = line.split(" ")
                data.append(a)
                data.append(b)
                data.append(c)
                data.append(d[0])
        Matrix = [[0 for x in xrange(4)] for x in xrange(4)] 
        i = 0
        for j in range (0,4):
            for k in range (0,4):
                Matrix[j][k] = (i,data[i])
                i = i + 1
        for j in range (0,4):
            for k in range (0,4):
                print (Matrix[j][k])
        print ('*************************')
        print ('MAX = R')
        print ('MIN = D')
        print ('*************************')
        result = {}
        temp = []
        remain = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        t = Node(0,1,remain,(maxsize,temp))
        l = list(itertools.combinations(remain,4))
        for child in l:
            (a,b,c,d) = child
            if ((a%4) == 3) and (b != (a+4)):
                temp.append(child)
            elif ((b%4) == 3) and (c != (b+4)):
                temp.append(child)
            elif ((c%4) == 3) and (d != (c+4)):
                temp.append(child)
            elif (b != (a+1)) and (b != (a+4)):
                temp.append(child)
            elif (c != (b+1)) and (c != (b+4)):
                temp.append(child)
            elif (d != (c+1)) and (d != (c+4)):
                temp.append(child)
        for r in temp:
            l.remove(r)
        for child in l:
            for i in child:
                remain.remove(i)
            s = Node(1,-1,remain,(maxsize,(child)))
            t.addchildren(s)
            remain = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        p = 0
        for child in l:
            temp = []
            remain = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            for i in child:
                remain.remove(i)
            dataone = []
            for i in remain:
                dataone.append(i)
            n = list(itertools.combinations(remain,4))
            for chil in n:
                (a,b,c,d) = chil
                if ((a%4) == 3) and (b != (a+4)):
                    temp.append(chil)
                elif ((b%4) == 3) and (c != (b+4)):
                    temp.append(chil)
                elif ((c%4) == 3) and (d != (c+4)):
                    temp.append(chil)
                elif (b != (a+1)) and (b != (a+4)):
                    temp.append(chil)
                elif (c != (b+1)) and (c != (b+4)):
                    temp.append(chil)
                elif (d != (c+1)) and (d != (c+4)):
                    temp.append(chil)
            for r in temp:
                n.remove(r)
            if (n != {}):
                for chil in n:
                    for i in chil:
                        remain.remove(i)
                    s = Node(2,1,remain,(maxsize,(child,chil)))
                    t.getchildren(p).addchildren(s)
                    datatwo =[]
                    tempone = []
                    for i in remain:
                        datatwo.append(i)
                    m = list(itertools.combinations(remain,4))
                    for chi in m:
                        (a,b,c,d) = chi
                        if ((a%4) == 3) and (b != (a+4)):
                            tempone.append(chi)
                        elif ((b%4) == 3) and (c != (b+4)):
                            tempone.append(chi)
                        elif ((c%4) == 3) and (d != (c+4)):
                            tempone.append(chi)
                        elif (b != (a+1)) and (b != (a+4)):
                            tempone.append(chi)
                        elif (c != (b+1)) and (c != (b+4)):
                            tempone.append(chi)
                        elif (d != (c+1)) and (d != (c+4)):
                            tempone.append(chi)
                        for r in tempone:
                            m.remove(r)
                        tempone = []
                        if (m != {}):
                            for chi in m:
                                for i in chi:
                                    remain.remove(i)
                                [a,b,c,d] = remain
                                if ((a%4) == 3) and (b != (a+4)):
                                    remain = []
                                elif ((b%4) == 3) and (c != (b+4)):
                                    remain = []
                                elif ((c%4) == 3) and (d != (c+4)):
                                    remain = []
                                elif (b != (a+1)) and (b != (a+4)):
                                    remain = []
                                elif (c != (b+1)) and (c != (b+4)):
                                    remain = []
                                elif (d != (c+1)) and (d != (c+4)):
                                    remain = []
                                if (remain != []):
                                    u = utility(Matrix,(child,chil,chi,remain))
                                    k = Node(3,-1,[],(u,(child,chil,chi,remain)))
                                    s.addchildren(k)
                                    result.update({u:(child,chil,chi,remain)})
                                remain = []
                                for i in datatwo:
                                    remain.append(i)
                        else:
                            t.getchildren(p).deletechildren(s)
                    remain = []
                    for i in dataone:
                        remain.append(i)
            else:
                t.deletechildren(child)
            p = p + 1
        val = minimax(t,3,t.i_player)
        print (val)
        util = result.get(val)
        print (util)
    if (pass_file == 'largeNeighborhood'):
        data = []
        with open (pass_file) as f:
            for line in f:
                a,b,c,d,e,m,n,s = line.split(" ")
                data.append(a)
                data.append(b)
                data.append(c)
                data.append(d)
                data.append(e)
                data.append(m)
                data.append(n)
                data.append(s)
        Matrix = [[0 for x in xrange(8)] for x in xrange(8)] 
        i = 0
        for j in range (0,8):
            for k in range (0,8):
                Matrix[j][k] = data[i]
                i = i + 1
    return 0	

if __name__ == '__main__':
    main()
