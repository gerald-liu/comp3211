# search.py
# ---------
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

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def genericGraphSearch(problem, openStruct):
    closed = []
    startState = problem.getStartState()
    openStruct.push( (startState, []) )

    # when OPEN is not empty
    while not openStruct.isEmpty():
        # get the first node on OPEN
        state, actions = openStruct.pop()

        # return if the goal is about to be expanded
        if problem.isGoalState(state):
            return actions

        # if the node has been visited, ignore the node
        if state in closed:
            continue
        
        # add the node to CLOSE
        closed.append(state)

        # for each child of the node
        for childState, actionToChild, stepCost in problem.getSuccessors(state):
            # if the child has not been visited, push it to OPEN
            if childState not in closed:
                openStruct.push((
                    childState,
                    actions + [actionToChild],
                ))

    # return False if the goal cannot be reached
    return False


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    openStack = util.Stack()
    return genericGraphSearch(problem, openStack)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    openQueue = util.Queue()
    return genericGraphSearch(problem, openQueue)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # f = cost
    openPQ = util.PriorityQueueWithFunction(lambda node: problem.getCostOfActions(node[1]))
    return genericGraphSearch(problem, openPQ)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # f = cost + heuristic
    openPQ = util.PriorityQueueWithFunction(lambda node: problem.getCostOfActions(node[1]) + heuristic(node[0], problem))
    return genericGraphSearch(problem, openPQ)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
