# Iterative policy evaluation
import numpy as np

policy_list = [pi_1,pi_2,pi_3]

state_space = []
value_list = []

for s in state_space:
  value_list.append(np.array(s.shape).zeros)
  
def update(value_list, sigma = 0):
  delta = 0
  
  while delta < sigma:
    #do stuff
  v = value_list[state]
  
  #value_list[state] = Bellman_equation   
  
  delta = max(delta, abs(v - value_list[state])
  
  #return all arrays