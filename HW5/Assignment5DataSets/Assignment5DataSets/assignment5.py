#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  assignment5.py
#  Phu Dang
#  
#  Copyright 2014 user <user@cu-cs-vm>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import getopt, sys
from math import log

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    #print start_p
    #print emit_p
 
    # Initialize base cases (t == 0)
    for y in states:
        if (start_p[y] == 0 or emit_p[y][obs[0]] == 0):
            V[0][y] = 0
        else:
            V[0][y] = (start_p[y])*(emit_p[y][obs[0]])
        path[y] = [y]
 
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            (prob, state) = max(((V[t-1][y0])*(trans_p[y0][y])*(emit_p[y][obs[t]]), y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        # Don't need to remember the old paths
        path = newpath
    n = 0           # if only one element is observed max is sought in the initialization values
    if len(obs) != 1:
        n = t
    (prob, state) = max((V[n][y], y) for y in states)
    return (prob, path[state])

def main(argv):
  pnumber = ''
  hmmorder = ''
	#Import arguments and parse into options.
  try:
    optlist, remainder = getopt.getopt(argv, 'hp:o:', ["problem=","hmmorder="])
    #If no arguments profided
    if len(optlist) == 0:
      print "***Options required***"
  #if inappropriate argument provided
  except getopt.GetoptError as err:
    print str(err)

  for o, a in optlist:
    if o == "-h":
         print 'assignment5.py -p <problem number> -o <hmm order>'
         sys.exit()
    elif o in ("-p", "--problem"):
         pnumber = a
    elif o in ("-o", "--hmmorder"):
         hmmorder = a
  if (hmmorder == "2"):
      print "Functionality not implemented"
      
  #Problem 1
  if (pnumber == "1" and hmmorder == "1"):
    data = {}
    numline = 0
    pass_file = "robot_no_momemtum.data"
    with open (pass_file) as f:
        for line in f:
            if (numline == 40000):
                break
            if ("." not in line):
                a,b = line.split(" ")
                numline = numline+1
                if data.has_key((a,b[0])):
                    data[(a,b[0])] = data.get((a,b[0]))+1
                else:
                    dict2 = {(a,b[0]):1}
                    data.update(dict2)
    dataone = [[0 for x in range(4)] for x in range(4)]
    datatwo = [[{"r":0,"g":0,"b":0,"y":0} for x in range(4)] for x in range(4)]
    for (s,o) in data:
        first,second = s.split(":")
        first = int(first)
        second = int(second)
        dataone[first-1][second-1] = dataone[first-1][second-1] + data.get((s,o))
        datatwo[first-1][second-1][o] = datatwo[first-1][second-1].get(o) + data.get((s,o))
    for i in range (0,4):
        for j in range (0,4):
            if (dataone[i][j] != 0):
                datatwo[i][j]["r"] = float(datatwo[i][j].get("r")+1)/(dataone[i][j]+2)
                datatwo[i][j]["g"] = float(datatwo[i][j].get("g")+1)/(dataone[i][j]+2)
                datatwo[i][j]["b"] = float(datatwo[i][j].get("b")+1)/(dataone[i][j]+2)
                datatwo[i][j]["y"] = float(datatwo[i][j].get("y")+1)/(dataone[i][j]+2)
    #Output P(E(t)=o | X[t]=s)
    print "The probability of observing (P(E[t]=o | X[t]=s)) are:"
    for i in range (0,4):
        for j in range (0,4):
            print str(i+1)+":"+str(j+1)+" "+str(datatwo[i][j])
    emit = {}
    for i in range (0,4):
        for j in range (0,4):
            dict2 = {str(i+1)+":"+str(j+1):datatwo[i][j]}
            emit.update(dict2)
    
    #Working with training data
    count = 0
    data = []
    datastate = [[0 for x in range (16)] for x in range (16)]
    with open (pass_file) as f:
        for line in f:
            if ("." not in line):
                count = count + 1
                a,b = line.split(" ")
                data.append(a)
            if (count == numline):
                break;
    dataone = []
    for i in data:
        a,b = i.split(":")
        a = int(a)
        b = int(b)
        dataone.append((a,b))
    for i in range (0,len(dataone)):
        if (i%200 != 199):
            (x1,y1) = dataone[i]
            (x2,y2) = dataone[i+1]
            datastate[4*(x1-1)+(y1-1)][4*(x2-1)+(y2-1)] = datastate[4*(x1-1)+(y1-1)][4*(x2-1)+(y2-1)] + 1
    s = 0
    for i in range (0,len(datastate)):
        for j in range (0,len(datastate)):
            s = s + datastate[i][j]
        if (s != 0):
            for j in range (0,len(datastate)):
                datastate[i][j] = float(datastate[i][j] + 1)/(s+2)
            s = 0
    #Output P(X(t+1)=s' | X[t]=s)
    print
    print "The probability of traversing (P(X[t+1])=s' | X[t]=s)) are:"
    for i in range (0,16):
        print "From state "+str(i/4+1)+":"+str(i%4+1)
        for j in range (0,16):
            print "  To state "+str(j/4+1)+":"+str(j%4+1)+"  "+str(datastate[i][j])
    trans = {}
    for i in range (0,len(datastate)):
        start = str(i/4+1)+":"+str(i%4+1)
        dict2 = {start:{}}
        trans.update(dict2)
        for j in range (0,len(datastate)):
            end = str(j/4+1)+":"+str(j%4+1)
            trans[start].update({end:datastate[i][j]})
            
            
    # Distribution over the start state
    datastartstate = [[0 for x in range(4)] for x in range(4)]
    for (i,j) in dataone:
        datastartstate[i-1][j-1] = datastartstate[i-1][j-1] + 1
    s = 0
    for i in range (0,len(datastartstate)):
        for j in range (0,len(datastartstate)):
            s= s + datastartstate[i][j]
    for i in range (0,len(datastartstate)):
        for j in range (0,len(datastartstate)):
            if (datastartstate[i][j] != 0):
                datastartstate[i][j] = float(datastartstate[i][j]+1)/(s+2)
    #Output P(X[0])
    print
    print "The distribution over the start state (P(X[0])) are:"
    for i in range (0,4):
        for j in range (0,4):
            print str(i+1)+":"+str(j+1)+" "+str(datastartstate[i][j])
    start_p = {}
    state = []
    for i in range (0,4):
        for j in range (0,4):
            state.append(str(i+1)+":"+str(j+1))
            start_p.update({str(i+1)+":"+str(j+1):datastartstate[i][j]})
    count = 0
    oser = []
    comp = []
    oserone =[]
    compone =[]
    with open (pass_file) as f:
        for line in f:
            if ("." not in line):
                count = count + 1
                if (count > numline):
                    a,b = line.split(" ")
                    oser.append(b[0])
                    comp.append(a)
    count = 0
    b = []
    for i in range (0,len(oser)):
        if (i % 200 == 0):
            start = i
        if (i % 200 == 199):
            end = i
            (a,b) = viterbi(oser[start:end],state,start_p,trans,emit)
            for j in range (0,len(b)):
                if (comp[j+start] == b[j]):
                    count = count + 1
    print
    print "The last 200 states producing by viterbi is (suggestion from Prof Rhonda):"
    print b
    print
    print "Percentage of correctness:"
    print (float(count)/float(len(comp)))*100.00
  
  #Problem 2
  if (pnumber == "2" and hmmorder == "1"):
    data = []
    numline = 0
    pass_file = "typos10.data"
    with open (pass_file) as f:
        for line in f:
            if ("." not in line):
                a,b = line.split(" ")
                data.append((a,b[0]))
    state = []
    training =[]
    for n in range (20000,len(data)):
        i,j = data[n]
        if i not in state:
            state.append(i)
        training.append((i,j))
    emit = {}
    for i in state:
        if i not in emit:
            emit.update({i:{}})
        for j in state:
            if j not in emit[i]:
                emit[i].update({j:0})
    for (i,j) in training:
        emit[i][j] = emit[i][j] + 1
    emit2 = {}
    for i in state:
        if i not in emit2:
            emit2.update({i:0})
    for (i,j) in training:
        emit2[i] = emit2[i] + 1
    for i in emit:
        for j in emit[i]:
            if (emit[i][j] != 0):
                emit[i][j] = float(emit[i][j]+1) / (emit2[i]+2)
    #Output P(E(t)=o | X[t]=s)
    print "The probability of observing (P(E[t]=o | X[t]=s)) are:"
    for i in emit:
        print "In state "+i+":"
        print str(emit[i])
    
    #Working with training data
    sta = {}
    for i in state:
        if i not in sta:
            sta.update({i:{}})
        for j in state:
            if j not in sta[i]:
                sta[i].update({j:0})
    for i in range (0,len(training)-1):
        a,b = training[i]
        c,d = training[i+1]
        sta[a][c] = sta[a][c] + 1
    sta2 = {}
    for i in state:
        if i not in sta2:
            sta2.update({i:0})
    for (i,j) in training:
        sta2[i] = sta2[i] + 1
    for i in sta:
        for j in sta[i]:
            if (sta[i][j] != 0):
                sta[i][j] = float(sta[i][j]+1) / (sta2[i]+2)
    #Output P(X(t+1)=s' | X[t]=s)
    print
    print "The probability of traversing (P(X[t+1])=s' | X[t]=s)) are:"
    for i in sta:
        print "From "+i+" to:"
        print sta[i]
    
    # Distribution over the start state
    startstate = sta2
    for i in state:
        startstate[i] = float(startstate[i]+1)/(len(training)+2)
    #Output P(X[0])
    print
    print "The distribution over the start state (P(X[0])) are:"
    print startstate
    oser = []
    comp = []
    count = 0
    b = []
    for n in range (0,20000):
        i,j = data[n]
        oser.append(j)
        comp.append(i)    
    for i in range (0,len(oser)):
        if (i % 250 == 0):
            start = i
        if (i % 250 == 249):
            end = i
            (a,b) = viterbi(oser[start:end],state,startstate,sta,emit)
            for j in range (0,len(b)):
                if (comp[j+start] == b[j]):
                    count = count + 1
    print
    print "The last 250 states producing by viterbi is (suggestion from Prof Rhonda):"
    print b
    print
    print "Percentage of correctness:"
    print (float(count)/float(len(comp)))*100.00
    
  #Problem 3
  if (pnumber == "3" and hmmorder == "1"):
    data = []
    numline = 0
    pass_file = "topics.data"
    with open (pass_file) as f:
        for line in f:
            if ("." not in line):
                (w,rest) = line.split(" ",1)
                rest = rest.split()
                for i in rest:
                    data.append((w,i))
    state = []
    training =[]
    oserone = []
    for n in range (1500,len(data)):
        i,j = data[n]
        if i not in state:
            state.append(i)
        if j not in oserone:
            oserone.append(j)
        training.append((i,j))
    emit = {}
    for i in state:
        if i not in emit:
            emit.update({i:{}})
        for j in oserone:
            if j not in emit[i]:
                emit[i].update({j:0})
    for (i,j) in training:
        emit[i][j] = emit[i][j] + 1
    emit2 = {}
    for i in state:
        if i not in emit2:
            emit2.update({i:0})
    for (i,j) in training:
        emit2[i] = emit2[i] + 1
    for i in emit:
        for j in emit[i]:
            if (emit[i][j] != 0):
                emit[i][j] = float(emit[i][j]+1) / (emit2[i]+2)
    #Output P(E(t)=o | X[t]=s)
    print "The probability of observing (P(E[t]=o | X[t]=s)) are:"
    for i in emit:
        print "In state "+i+":"
        print str(emit[i].values())
    #Working with training data
    sta = {}
    for i in state:
        if i not in sta:
            sta.update({i:{}})
        for j in state:
            if j not in sta[i]:
                sta[i].update({j:0})
    for i in range (0,len(training)-1):
        a,b = training[i]
        c,d = training[i+1]
        sta[a][c] = sta[a][c] + 1
    sta2 = {}
    for i in state:
        if i not in sta2:
            sta2.update({i:0})
    for (i,j) in training:
        sta2[i] = sta2[i] + 1
    for i in sta:
        for j in sta[i]:
            if (sta[i][j] != 0):
                sta[i][j] = float(sta[i][j]+1) / (sta2[i]+2)
    #Output P(X(t+1)=s' | X[t]=s)
    print
    print "The probability of traversing (P(X[t+1])=s' | X[t]=s)) are:"
    for i in sta:
        print "From "+i+" to:"
        print sta[i]
    # Distribution over the start state
    startstate = sta2
    for i in state:
        startstate[i] = float(startstate[i]+1)/(len(training)+2)
    #Output P(X[0])
    print
    print "The distribution over the start state (P(X[0])) are:"
    print startstate
    oser = []
    comp = []
    count = 0
    b = []
    for n in range (0,1500):
        i,j = data[n]
        oser.append(j)
        comp.append(i)    
    for i in range (0,len(oser)):
        if (i % 300 == 0):
            start = i
        if (i % 300 == 299):
            end = i
            (a,b) = viterbi(oser[start:end],state,startstate,sta,emit)
            for j in range (0,len(b)):
                if (comp[j+start] == b[j]):
                    count = count + 1
    print
    print "The last 300 states producing by viterbi is (suggestion from Prof Rhonda):"
    print b
    print
    print "Percentage of correctness:"
    print (float(count)/float(len(comp)))*100.00
  return 0

if __name__ == '__main__':
	main(sys.argv[1:])

