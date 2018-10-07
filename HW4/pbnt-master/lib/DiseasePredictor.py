#! /usr/bin/env python
# Phu Dang
# Partner: Jie He

import getopt, sys
from numpy import *
from pbnt.Graph import *
from pbnt.Distribution import *
from pbnt.Node import *
from pbnt.Inference import *

try:
    from IPython import embed
except:
    pass

debug = False;

def jointProb(disease,condone):
    cond = copy.copy(condone)
    for node in disease.nodes:
        if node.id == 0:
            pollution = node
        if node.id == 1:
            smoker = node
        if node.id == 2:
            cancer = node
        if node.id == 3:
            xray = node
        if node.id == 4:
           dyspnoea = node
    engine = JunctionTreeEngine(disease)
    if len(cond) == 2:
        w = cond[0]
        if (w == "p"):
              Q = engine.marginal(pollution)[0]
              # embed()
              index = Q.generate_index([True], range(Q.nDims))
              engine.evidence[pollution]=True
              #print "Given pollution = low"
        if (w == "~p"):
              Q = engine.marginal(pollution)[0]
              # embed()
              index = Q.generate_index([False], range(Q.nDims))
              engine.evidence[pollution]=False
              #print "Given pollution = high"
        if (w == "s"):
              Q = engine.marginal(smoker)[0]
              # embed()
              index = Q.generate_index([True], range(Q.nDims))
              engine.evidence[smoker]=True
              #print "Given smoker = true"
        if (w == "~s"):
              Q = engine.marginal(smoker)[0]
              # embed()
              index = Q.generate_index([False], range(Q.nDims))
              engine.evidence[smoker]=False
              #print "Given smoker = false"
        if (w == "c"):
              Q = engine.marginal(cancer)[0]
              # embed()
              index = Q.generate_index([True], range(Q.nDims))
              engine.evidence[cancer]=True
              #print "Given cancer = true"
        if (w == "~c"):
              Q = engine.marginal(cancer)[0]
              # embed()
              index = Q.generate_index([False], range(Q.nDims))
              engine.evidence[cancer]=False
              #print "Given cancer = false"
        if (w == "x"):
              Q = engine.marginal(xray)[0]
              # embed()
              index = Q.generate_index([True], range(Q.nDims))
              engine.evidence[xray]=True 
              #print "Given xray = pos"
        if (w == "~x"):
              Q = engine.marginal(xray)[0]
              # embed()
              index = Q.generate_index([False], range(Q.nDims))
              engine.evidence[xray]=False
              #print "Given xray = neg"
        if (w == "d"):
              Q = engine.marginal(dyspnoea)[0]
              # embed()
              index = Q.generate_index([True], range(Q.nDims))
              engine.evidence[dyspnoea]=True
              #print "Given dyspnoea = true"
        if (w == "~d"):
              Q = engine.marginal(dyspnoea)[0]
              # embed()
              index = Q.generate_index([False], range(Q.nDims))
              engine.evidence[dyspnoea]=False
              #print "Given dyspnoea = false" 
        w = cond[1]
        if (w == "p"):
              #print "Given pollution = low"
              D = engine.marginal(pollution)[0]
              index_1 = D.generate_index([True], range(D.nDims))
              return Q[index]*D[index_1]
        if (w == "~p"):
              #print "Given pollution = high"
              D = engine.marginal(pollution)[0]
              index_1 = D.generate_index([False], range(D.nDims))
              return Q[index]*D[index_1]
        if (w == "s"):
              #print "Given smoker = true"
              D = engine.marginal(smoker)[0]
              index_1 = D.generate_index([True], range(D.nDims))
              return Q[index]*D[index_1]
        if (w == "~s"):
              #print "Given smoker = false"
              D = engine.marginal(smoker)[0]
              index_1 = D.generate_index([False], range(D.nDims))
              return Q[index]*D[index_1]
        if (w == "c"):
              #print "Given cancer = true"
              D = engine.marginal(cancer)[0]
              index_1 = D.generate_index([True], range(D.nDims))
              return Q[index]*D[index_1]
        if (w == "~c"):
              #print "Given cancer = false"
              D = engine.marginal(cancer)[0]
              index_1 = D.generate_index([False], range(D.nDims))
              return Q[index]*D[index_1]
        if (w == "x"):
              #print "Given xray = pos"
              D = engine.marginal(xray)[0]
              index_1 = D.generate_index([True], range(D.nDims))
              return Q[index]*D[index_1]
        if (w == "~x"):
              #print "Given xray = neg"
              D = engine.marginal(xray)[0]
              index_1 = D.generate_index([False], range(D.nDims))
              return Q[index]*D[index_1]
        if (w == "d"):
              #print "Given dyspnoea = true"
              D = engine.marginal(dyspnoea)[0]
              index_1 = D.generate_index([True], range(D.nDims))
              return Q[index]*D[index_1]
        if (w == "~d"):
              #print "Given dyspnoea = false"
              D = engine.marginal(dyspnoea)[0]
              index_1 = D.generate_index([False], range(D.nDims))
              return Q[index]*D[index_1]
    else:
        k = cond.pop(0)
        o = jointProb(disease,cond)
        for w in cond:
          if (w == "p"):
              engine.evidence[pollution]=True
              #print "Given pollution = low"
          if (w == "~p"):
              engine.evidence[pollution]=False
              #print "Given pollution = high"
          if (w == "s"):
              engine.evidence[smoker]=True
              #print "Given smoker = true"
          if (w == "~s"):
              engine.evidence[smoker]=False
              #print "Given smoker = false"
          if (w == "c"):
              engine.evidence[cancer]=True
              #print "Given cancer = true"
          if (w == "~c"):
              engine.evidence[cancer]=False
              #print "Given cancer = false"
          if (w == "x"):
              engine.evidence[xray]=True
              #print "Given xray = pos"
          if (w == "~x"):
              engine.evidence[xray]=False
              #print "Given xray = neg"
          if (w == "d"):
              engine.evidence[dyspnoea]=True
              #print "Given dyspnoea = true"
          if (w == "~d"):
              engine.evidence[dyspnoea]=False
              #print "Given dyspnoea = false"
        if (k == "p"):
          K = engine.marginal(pollution)[0]
          # embed()
          index_2 = K.generate_index([True], range(K.nDims))
          #print "Conditional probability of pollution=low is ",K[index_2]
        if (k == "~p"):
          K = engine.marginal(pollution)[0]
          # embed()
          index_2 = K.generate_index([False], range(K.nDims))
          #print "Conditional probability of pollution=high is ",K[index_2]
        if (k == "s"):
          K = engine.marginal(smoker)[0]
          # embed()
          index_2 = K.generate_index([True], range(K.nDims))
          #print "Conditional probability of smoker=true is ",K[index_2]
        if (k == "~s"):
          K = engine.marginal(smoker)[0]
          # embed()
          index_2 = K.generate_index([False], range(K.nDims))
          #print "Conditional probability of smoker=false is ",K[index_2]
        if (k == "c"):
          K = engine.marginal(cancer)[0]
          # embed()
          index_2 = K.generate_index([True], range(K.nDims))
          #print "Conditional probability of cancer=true is ",[index_2]
        if (k == "~c"):
          K = engine.marginal(cancer)[0]
          # embed()
          index_2 = K.generate_index([False], range(K.nDims))
          #print "Conditional probability of cancer=false is ",K[index_2]
        if (k == "x"):
          K = engine.marginal(xray)[0]
          # embed()
          index_2 = Q.generate_index([True], range(K.nDims))
          #print "Conditional probability of xray=pos is ",K[index_2]
        if (k == "~x"):
          K = engine.marginal(xray)[0]
          # embed()
          index_2 = K.generate_index([False], range(K.nDims))
          #print "Conditional probability of xray=neg is ",K[index_2]
        if (k == "d"):
          K = engine.marginal(dyspnoea)[0]
          # embed()
          index_2 = K.generate_index([True], range(K.nDims))
          #print "Conditional probability of dyspnoea=true is ",K[index_2]
        if (k == "~d"):
          K = engine.marginal(dyspnoea)[0]
          # embed()
          index_2 = K.generate_index([False], range(K.nDims))
          #print "Conditional probability of dyspnoea=false is ",K[index_2]
           
        return o * K[index_2]

def output(cond):
    for w in cond:
            if (w == "p"):
              print "Given pollution = low"
            if (w == "~p"):
              print "Given pollution = high"
            if (w == "s"):
              print "Given smoker = true"
            if (w == "~s"):
              print "Given smoker = false"
            if (w == "c"):
              print "Given cancer = true"
            if (w == "~c"):
              print "Given cancer = false"
            if (w == "x"):
              print "Given xray = pos"
            if (w == "~x"):
              print "Given xray = neg"
            if (w == "d"):
              print "Given dyspnoea = true"
            if (w == "~d"):
              print "Given dyspnoea = false"           

def main():

  #Initialize the Cancer Bayes Network
  #network = nGraph()
  #testing basic bayes net class implementation
  numberOfNodes = 4
  #name the nodes
  pollution = 0
  smoker = 1
  cancer = 2
  xray = 3
  dyspnoea = 4

  pNode = BayesNode(0, 2, name="pollution")
  sNode = BayesNode(1, 2, name="smoker")
  cNode = BayesNode(2, 2, name="cancer")
  xNode = BayesNode(3, 2, name="xray")
  dNode = BayesNode(4, 2, name="dyspnoea")

  #pollution
  pNode.add_child(cNode)

  #smoker
  sNode.add_child(cNode)

  #cancer
  cNode.add_parent(pNode)
  cNode.add_parent(sNode)
  cNode.add_child(xNode)
  cNode.add_child(dNode)

  #xray
  xNode.add_parent(cNode)
  
  #dyspnoea
  dNode.add_parent(cNode)

  nodes = [pNode,sNode,cNode,xNode,dNode]

  #create distributions
  #pollution distribution
  pDistribution = DiscreteDistribution(pNode)
  index = pDistribution.generate_index([],[])
  # embed()
  pDistribution[index] = [0.1,0.9]
  pNode.set_dist(pDistribution)

  #smoker distribution
  sDistribution = DiscreteDistribution(sNode)
  index = sDistribution.generate_index([],[])
  # embed()
  sDistribution[index] = [0.7,0.3]
  sNode.set_dist(sDistribution)
  
  #xray
  dist = zeros([cNode.size(),xNode.size()], dtype=float32)
  dist[0,] = [0.8,0.2]
  dist[1,] = [0.1,0.9]
  xDistribution = ConditionalDiscreteDistribution(nodes=[cNode, xNode], table=dist)
  xNode.set_dist(xDistribution)

  #dyspnoea
  dist = zeros([cNode.size(), dNode.size()], dtype=float32)
  dist[0,] = [0.7,0.3]
  dist[1,] = [0.35,0.65]
  dDistribution = ConditionalDiscreteDistribution(nodes=[cNode, dNode], table=dist)
  dNode.set_dist(dDistribution)

  #cancer
  dist = zeros([pNode.size(), sNode.size(), cNode.size()], dtype=float32)
  dist[0,0,] = [0.98,0.02]
  dist[1,0,] = [0.999,0.001]
  dist[0,1,] = [0.95,0.05]
  dist[1,1,] = [0.97,0.03]
  cDistribution = ConditionalDiscreteDistribution(nodes=[pNode, sNode, cNode], table=dist)
  cNode.set_dist(cDistribution)


  #create bayes net
  disease = BayesNet(nodes)
  for node in disease.nodes:
    if node.id == 0:
      pollution = node
    if node.id == 1:
      smoker = node
    if node.id == 2:
      cancer = node
    if node.id == 3:
      xray = node
    if node.id == 4:
      dyspnoea = node
  # embed()
  engine = JunctionTreeEngine(disease)

  # engine.evidence[cloudy] = True
  # #Compute the marginal probability given the evidence cloudy=False, rain=true
  # Q = engine.marginal(sprinkler)[0]
  # index = Q.generate_index([True],range(Q.nDims))
  # print "The marginal probability of wetgrass=false | cloudy=False, rain=True:", Q[index]

  #Run logic on bayes:


  #print result
  
  #Import arguments and parse into options.
  try:
    optlist, remainder = getopt.getopt(sys.argv[1:], 'j:g:m:vh')
    #If no arguments profided
    if len(optlist) == 0:
      print "***Options required***"
      usage()
  #if inappropriate argument provided
  except getopt.GetoptError as err:
    print str(err)
    usage()

  for o, a in optlist:
    if o == "-v":
      debug = True
      if debug:
        #view input
        print "\nProvided Arguments: "
        print str(optlist) + "\n"
    elif o == "-h":
      usage()
    elif o == "-m":
      # Return the Marginal probability
      if(a == "P"):
          Q = engine.marginal(pollution)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "The marginal probability of pollution=low:", Q[index]
          Q = engine.marginal(pollution)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "The marginal probability of pollution=high:", Q[index]
      if(a == "p"):
          Q = engine.marginal(pollution)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "The marginal probability of pollution=low:", Q[index]
      if(a == "~p"):
          Q = engine.marginal(pollution)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "The marginal probability of pollution=high:", Q[index]
      if(a == "S"):
          Q = engine.marginal(smoker)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "The marginal probability of smoker=true:", Q[index]
          Q = engine.marginal(smoker)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "The marginal probability of smoker=false:", Q[index]
      if(a == "s"):
          Q = engine.marginal(smoker)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "The marginal probability of smoker=true:", Q[index]
      if(a == "~s"):
          Q = engine.marginal(smoker)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "The marginal probability of smoker=false:", Q[index]
      if(a == "C"):
          Q = engine.marginal(cancer)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "The marginal probability of cancer=true:", Q[index]
          Q = engine.marginal(cancer)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "The marginal probability of cancer=false:", Q[index]
      if(a == "c"):
          Q = engine.marginal(cancer)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "The marginal probability of cancer=true:", Q[index]
      if(a == "~c"):
          Q = engine.marginal(cancer)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "The marginal probability of cancer=false:", Q[index]
      if(a == "X"):
          Q = engine.marginal(xray)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "The marginal probability of xray=pos:", Q[index]
          Q = engine.marginal(xray)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "The marginal probability of xray=neg:", Q[index]
      if(a == "x"):
          Q = engine.marginal(xray)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "The marginal probability of xray=pos:", Q[index]
      if(a == "~x"):
          Q = engine.marginal(xray)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "The marginal probability of xray=neg:", Q[index]
      if(a == "D"):
          Q = engine.marginal(dyspnoea)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "The marginal probability of dyspnoea=true:", Q[index]
          Q = engine.marginal(dyspnoea)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "The marginal probability of dyspnoea=false:", Q[index]
      if(a == "d"):
          Q = engine.marginal(dyspnoea)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "The marginal probability of dyspnoea=true:", Q[index]
      if(a == "~d"):
          Q = engine.marginal(dyspnoea)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "The marginal probability of dyspnoea=false:", Q[index]
    elif o == "-g":
      # Return the conditional probability
      cond = []
      (k,l) = a.split("|")
      test = False
      for w in l:
          if (test):
              w = "~" + w
              test= False
              cond.append(w)
          else:
              if (w == "~"):
                  test = True
              else:
                  cond.append(w)
      for w in cond:
          if (w == "p"):
              engine.evidence[pollution]=True
              print "Given pollution = low"
          if (w == "~p"):
              engine.evidence[pollution]=False
              print "Given pollution = high"
          if (w == "s"):
              engine.evidence[smoker]=True
              print "Given smoker = true"
          if (w == "~s"):
              engine.evidence[smoker]=False
              print "Given smoker = false"
          if (w == "c"):
              engine.evidence[cancer]=True
              print "Given cancer = true"
          if (w == "~c"):
              engine.evidence[cancer]=False
              print "Given cancer = false"
          if (w == "x"):
              engine.evidence[xray]=True
              print "Given xray = pos"
          if (w == "~x"):
              engine.evidence[xray]=False
              print "Given xray = neg"
          if (w == "d"):
              engine.evidence[dyspnoea]=True
              print "Given dyspnoea = true"
          if (w == "~d"):
              engine.evidence[dyspnoea]=False
              print "Given dyspnoea = false"
      if (k == "p"):
          Q = engine.marginal(pollution)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "Conditional probability of pollution=low is ",Q[index]
      if (k == "~p"):
          Q = engine.marginal(pollution)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "Conditional probability of pollution=high is ",Q[index]
      if (k == "s"):
          Q = engine.marginal(smoker)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "Conditional probability of smoker=true is ",Q[index]
      if (k == "~s"):
          Q = engine.marginal(smoker)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "Conditional probability of smoker=false is ",Q[index]
      if (k == "c"):
          Q = engine.marginal(cancer)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "Conditional probability of cancer=true is ",Q[index]
      if (k == "~c"):
          Q = engine.marginal(cancer)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "Conditional probability of cancer=false is ",Q[index]
      if (k == "x"):
          Q = engine.marginal(xray)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "Conditional probability of xray=pos is ",Q[index]
      if (k == "~x"):
          Q = engine.marginal(xray)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "Conditional probability of xray=neg is ",Q[index]
      if (k == "d"):
          Q = engine.marginal(dyspnoea)[0]
          # embed()
          index = Q.generate_index([True], range(Q.nDims))
          print "Conditional probability of dyspnoea=true is ",Q[index]
      if (k == "~d"):
          Q = engine.marginal(dyspnoea)[0]
          # embed()
          index = Q.generate_index([False], range(Q.nDims))
          print "Conditional probability of dyspnoea=false is ",Q[index]
      pass
    elif o == "-j":
      # Return the joint probability
      cond = []
      test = False
      for w in a:
          if (test):
              w = "~" + w
              test= False
              cond.append(w)
          else:
              if (w == "~"):
                  test = True
              else:
                  cond.append(w)
      if ("P" not in cond) and ("S" not in cond) and ("C" not in cond) and ("X" not in cond) and ("D" not in cond):
          output(cond)
          y = jointProb(disease,cond)
          print "The joint probability of is ",y
      if (a == "PSC"):
          output(["p","s","c"])
          y = jointProb(disease,["p","s","c"])
          print "The joint probability of is ",y
          output(["p","s","~c"])
          y = jointProb(disease,["p","s","~c"])
          print "The joint probability of is ",y
          output(["p","~s","c"])
          y = jointProb(disease,["p","~s","c"])
          print "The joint probability of is ",y
          output(["p","~s","~c"])
          y = jointProb(disease,["p","~s","~c"])
          print "The joint probability of is ",y
          output(["~p","s","c"])
          y = jointProb(disease,["~p","s","c"])
          print "The joint probability of is ",y
          output(["~p","s","~c"])
          y = jointProb(disease,["~p","s","~c"])
          print "The joint probability of is ",y
          output(["~p","~s","c"])
          y = jointProb(disease,["~p","~s","c"])
          print "The joint probability of is ",y
          output(["~p","~s","~c"])
          y = jointProb(disease,["~p","~s","~c"])
          print "The joint probability of is ",y
      if (a == "PCX"):
          output(["p","c","x"])
          y = jointProb(disease,["p","c","x"])
          print "The joint probability of is ",y
          output(["p","c","~x"])
          y = jointProb(disease,["p","c","~x"])
          print "The joint probability of is ",y
          output(["p","~c","x"])
          y = jointProb(disease,["p","~c","x"])
          print "The joint probability of is ",y
          output(["p","~c","~x"])
          y = jointProb(disease,["p","~c","~x"])
          print "The joint probability of is ",y
          output(["~p","c","x"])
          y = jointProb(disease,["~p","c","x"])
          print "The joint probability of is ",y
          output(["~p","c","~x"])
          y = jointProb(disease,["~p","c","~x"])
          print "The joint probability of is ",y
          output(["~p","~c","x"])
          y = jointProb(disease,["~p","~c","x"])
          print "The joint probability of is ",y
          output(["~p","~c","~x"])
          y = jointProb(disease,["~p","~c","~x"])
          print "The joint probability of is ",y
      if (a == "PCD"):
          output(["p","c","d"])
          y = jointProb(disease,["p","c","d"])
          print "The joint probability of is ",y
          output(["p","c","~d"])
          y = jointProb(disease,["p","c","~d"])
          print "The joint probability of is ",y
          output(["p","~c","d"])
          y = jointProb(disease,["p","~c","d"])
          print "The joint probability of is ",y
          output(["p","~c","~d"])
          y = jointProb(disease,["p","~c","~d"])
          print "The joint probability of is ",y
          output(["~p","c","d"])
          y = jointProb(disease,["~p","c","d"])
          print "The joint probability of is ",y
          output(["~p","c","~d"])
          y = jointProb(disease,["~p","c","~d"])
          print "The joint probability of is ",y
          output(["~p","~c","d"])
          y = jointProb(disease,["~p","~c","d"])
          print "The joint probability of is ",y
          output(["~p","~c","~d"])
          y = jointProb(disease,["~p","~c","~d"])
          print "The joint probability of is ",y
      if (a == "CDX"):
          output(["c","d","x"])
          y = jointProb(disease,["p","c","d"])
          print "The joint probability of is ",y
          output(["c","~d","x"])
          y = jointProb(disease,["p","c","~d"])
          print "The joint probability of is ",y
          output(["~c","d","x"])
          y = jointProb(disease,["p","~c","d"])
          print "The joint probability of is ",y
          output(["~c","~d","x"])
          y = jointProb(disease,["p","~c","~d"])
          print "The joint probability of is ",y
          output(["c","d","~x"])
          y = jointProb(disease,["~p","c","d"])
          print "The joint probability of is ",y
          output(["c","~d","~x"])
          y = jointProb(disease,["~p","c","~d"])
          print "The joint probability of is ",y
          output(["~c","d","~x"])
          y = jointProb(disease,["~p","~c","d"])
          print "The joint probability of is ",y
          output(["~c","~d","~x"])
          y = jointProb(disease,["~p","~c","~d"])
          print "The joint probability of is ",y
      if ("P" in cond) and ("S" not in cond) and ("C" not in cond) and ("X" not in cond) and ("D" not in cond):
          cond.remove("P")
          cond.append("p")
          output(cond)
          y = jointProb(disease,cond)
          print "The joint probability of is ",y
          cond.remove("p")
          cond.append("~p")
          output(cond)
          y = jointProb(disease,cond)
          print "The joint probability of is ",y
      if ("P" not in cond) and ("S" in cond) and ("C" not in cond) and ("X" not in cond) and ("D" not in cond):
          cond.remove("S")
          cond.append("s")
          output(cond)
          y = jointProb(disease,cond)
          print "The joint probability of is ",y
          cond.remove("s")
          cond.append("~s")
          output(cond)
          y = jointProb(disease,cond)
          print "The joint probability of is ",y
      if ("P" not in cond) and ("S" not in cond) and ("C" in cond) and ("X" not in cond) and ("D" not in cond):
          cond.remove("C")
          cond.append("c")
          output(cond)
          y = jointProb(disease,cond)
          print "The joint probability of is ",y
          cond.remove("c")
          cond.append("~c")
          output(cond)
          y = jointProb(disease,cond)
          print "The joint probability of is ",y
      if ("P" not in cond) and ("S" not in cond) and ("C" not in cond) and ("X" in cond) and ("D" not in cond):
          cond.remove("X")
          cond.append("x")
          output(cond)
          y = jointProb(disease,cond)
          print "The joint probability of is ",y
          cond.remove("x")
          cond.append("~x")
          output(cond)
          y = jointProb(disease,cond)
          print "The joint probability of is ",y
      if ("P" not in cond) and ("S" not in cond) and ("C" not in cond) and ("X" not in cond) and ("D" in cond):
          cond.remove("D")
          cond.append("d")
          output(cond)
          y = jointProb(disease,cond)
          print "The joint probability of is ",y
          cond.remove("d")
          cond.append("~d")
          output(cond)
          y = jointProb(disease,cond)
          print "The joint probability of is ",y
    pass


def usage():
  print """
  Usage:
  ---
    Flags
    -g  conditional probablity
    -j  joint probability
    -m  marginal probability
    -v  verbose
    -h  help
  ---
    Input
    P  Polution   (p = low,  ~p = high)
    S  Smoker     (s = true, ~s = false)
    C  Cancer     (c = true, ~c = false)
    D  Dyspnoea   (d = true, ~d = false)
    X  X-Ray      (x = true, ~x = false)
  ---
    Example
    python bayesnet.py -jPSC
    (joint probabilities for Pollution, Smoker, and Cancer)

    python bayesnet.py -j~p~s~c
    (joint probability for pollution = h, smoker = f, cancer = f)

    python bayesnet.py -gc|s
    (conditional probability for cancer given that someone is a smoker)
  """
  sys.exit(2)

if __name__ == "__main__":
    main()
