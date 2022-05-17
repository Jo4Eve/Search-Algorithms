#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

class Node:#creates the node
    def __init__(self, parent, state, action):
        self.parent = parent
        self.state = state
        self.action = action
        
class  StackFrontier():#object to store frontier variables
    def __init__(self):
        self.frontier = []# create a frontier represented by a list, empty to begin with
        
    def Add(self,node):
        self.frontier.append(node)# appends node at the end of the frontier list
        
    def contains_state(self,state):# checks if the fronties contains a particular state
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == )#returns 0 is the frontier is empty
    
    def remove_frontier(self):
        if self.empty():
            raise Exception('Frontier is empty!')
        else:
            node = self.frontier[-1]# removes the node at the end
            self.frontier = self.frontier[:-1]#updating the frontier
            return node
        
class QueueFrontier(StackFrontier):# inherists all stackfrontier functions except node removal
    def remove_frontier(self):
        if self.empty():
            raise Exception('Frontier is empty')
        else:
            node =  self.frontier[0]
            self.frontier =  self.frontier[1:]
            return node
            

    
   
    
        
    

