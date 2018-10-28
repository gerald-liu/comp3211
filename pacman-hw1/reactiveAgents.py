# reactiveAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# Edited by Gerald Liu

from game import Directions
from game import Agent
from game import Actions
import util
import time
import search
from ECAgentLearning import train_all, decide

# The agent receives a GameState (defined in pacman.py)

# An agent that goes West until it can't.
class NaiveAgent(Agent):
    def getAction(self, state):
        sense = state.getPacmanSensor()
        if sense[7]:
            return Directions.STOP
        else:
            return Directions.WEST

# An agent that follows the boundary using production system.
class PSAgent(Agent):
    def getAction(self, state):
        s = state.getPacmanSensor()
        x = [ s[1] or s[2], s[3] or s[4], s[5] or s[6], s[7] or s[0] ]
        
        if x[3] and not x[0]:
            return Directions.NORTH
        elif x[2] and not x[3]:
            return Directions.WEST
        elif x[1] and not x[2]:
            return Directions.SOUTH
        elif x[0] and not x[1]:
            return Directions.EAST
        else:
            return Directions.NORTH

# An agent that follows the boundary using error-correction.
class ECAgent(Agent):
    def getAction(self, state):
        sense = state.getPacmanSensor()
        labels = ['north', 'east', 'south', 'west']
        filenames = ['ECAgentTrainingData/' + l + '.csv' for l in labels]
        weight_sets = train_all(filenames)
        decisions = []
        for i in range(len(labels)):
            decisions.append(decide(weight_sets[i], sense))

        if decisions[0]:
            return Directions.NORTH
        elif decisions[1]:
            return Directions.EAST
        elif decisions[2]:
            return Directions.SOUTH
        elif decisions[3]:
            return Directions.WEST
        else:
            return Directions.NORTH
