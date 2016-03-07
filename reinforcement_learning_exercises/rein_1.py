import numpy as np
import random

l1 = [1.0,1.0,2.0,1.0,1.0,1.0]
l2 = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,200.0]
l3 = [1.0,1.0,1.0,3.0]
l4 = [2.0,2.0,2.0,2.0,2.0,2.0,2.0,-100.0]

l1e = 0
l2e = 0
l3e = 0
l4e = 0

ll = ['l1','l2','l3','l4']

llv = [l1,l2,l3,l4]

l1e = l1[random.choice(range(len(l1)))]
l2e = l2[random.choice(range(len(l2)))]
l3e = l3[random.choice(range(len(l3)))]
l4e = l4[random.choice(range(len(l4)))]



lle_t = [('l1e',l1e,'l1'), ('l2e',l2e,'l2'), ('l3e',l3e,'l3'), ('l4e',l4e,'l4')]

lle = [l1e,l2e,l3e,l4e]

for le in lle:
  print le
  
l1c = 1
l2c = 1
l3c = 1
l4c = 1

booty = 0
choice = ''

for i in range(1000):
  if i%9==0:
    ln = random.choice(ll)
  else:
    for i in range(4):
      if lle_t[i][1] == max(lle):
        ln = lle_t[i][2]  
    
    
       
  if ln == 'l1':
    l1c += 1
    val_this_round = random.choice(l1)
    l1e = ((l1e*(l1c - 1)) + val_this_round)/l1c
    choice = "l1"
  elif ln ==  'l2':
    l2c += 1
    val_this_round = random.choice(l2)
    l2e = ((l2e*(l2c - 1)) + val_this_round)/l2c
    choice = "l2"
  elif ln ==  'l3':
    l3c += 1
    val_this_round = random.choice(l3)
    l3e = ((l3e*(l3c - 1)) + val_this_round)/l3c
    choice = "l3"
  elif ln == 'l4': 
    l4c += 1
    val_this_round = random.choice(l4)
    l4e = ((l4e*(l4c - 1)) + val_this_round)/l4c
    choice = "l4"
  
    
  lle_t = [('l1e',l1e,'l1'), ('l2e',l2e,'l2'), ('l3e',l3e,'l3'), ('l4e',l4e,'l4')]
  lle = [l1e,l2e,l3e,l4e]
  booty += val_this_round
  print i 
  print choice
  print "Val this round: " + str(val_this_round) 
  print "Loot so far: " + str(booty)
  print "Estimates: "
  iter_s = 0
  for lep in lle: 
    iter_s +=1
    print "l" + str(iter_s) + ": " + str(lep)
    
lst_cnt = 0     
for l in llv:
  lst_cnt += 1
  print "Avg of l" + str(lst_cnt) + ": "
  print sum(l)/len(l)  

print sum(l1)/len(l1)
print sum(l2)/len(l2)
print sum(l3)/len(l3)
print sum(l4)/len(l4)

l1e2 = 0
l2e2 = 0
l3e2 = 0
l4e2 = 0

l1e2 = l1[random.choice(range(len(l1)))]
l2e2 = l2[random.choice(range(len(l2)))]
l3e2 = l3[random.choice(range(len(l3)))]
l4e2 = l4[random.choice(range(len(l4)))]

l1e2p = 0
l2e2p = 0
l3e2p = 0
l4e2p = 0

lle_t2 = [('l1e2',l1e2,'l1'), ('l2e2',l2e2,'l2'), ('l3e2',l3e2,'l3'), ('l4e2',l4e2,'l4')]

lle2 = [l1e2,l2e2,l3e2,l4e2]

alpha = 0.003

for le in lle2:
  print le
  
l1c2 = 1
l2c2 = 1
l3c2 = 1
l4c2 = 1

booty2 = 0
choice = ''

for i in range(1000):
  if i%9==0:
    ln = random.choice(ll)
  else:
    for i in range(len(ll)):
      if lle_t2[i][1] == max(lle2):
        ln = lle_t2[i][2]  
    
    
       
  if ln == 'l1':
    l1c2 += 1
    val_this_round = random.choice(l1)
    l1e2 = l1e2p + alpha*(val_this_round - l1e2p)
    l1e2p = l1e2
    choice = "l1"
  elif ln ==  'l2':
    l2c2 += 1
    val_this_round = random.choice(l2)
    l2e2 = l2e2p + alpha*(val_this_round - l2e2p)
    l2e2p = l2e2
    choice = "l2"
  elif ln ==  'l3':
    l3c2 += 1
    val_this_round = random.choice(l3)
    l3e2 = l3e2p + alpha*(val_this_round - l3e2p)
    l3e2p = l3e2
    choice = "l3"
  elif ln == 'l4': 
    l4c2 += 1
    val_this_round = random.choice(l4)
    l4e2 = l4e2p + alpha*(val_this_round - l4e2p)
    l4e2p = l4e2
    choice = "l4"
  
    
  lle_t2 = [('l1e2',l1e2,'l1'), ('l2e2',l2e2,'l2'), ('l3e2',l3e2,'l3'), ('l4e2',l4e2,'l4')]
  lle2 = [l1e2,l2e2,l3e2,l4e2]
  booty2 += val_this_round
  print i 
  print choice
  print "Val this round: " + str(val_this_round) 
  print "Loot so far: " + str(booty2)
  print "Loot from averaging method: " + str(booty)
  print "Estimates: "
  iter_s = 0
  for lep in lle2: 
    iter_s +=1
    print "l" + str(iter_s) + ": " + str(lep)
    
