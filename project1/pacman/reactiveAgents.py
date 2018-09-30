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

from game import Directions
from game import Agent
from game import Actions
import util
import time
import search

class NaiveAgent(Agent):
    "An agent that goes West until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        sense = state.getPacmanSensor()
        if sense[7]:
            return Directions.STOP
        else:
            return Directions.WEST

class PSAgent(Agent):
    "An agent that follows the boundary using production system."

    def getAction(self, state):
        ''' Your code goes here! '''
        return Directions.NORTH

class ECAgent(Agent):
    "An agent that follows the boundary using error-correction."

    def getAction(self, state):
        ''' Your code goes here! '''
        return Directions.NORTH
