# COMP 3211

COMP 3211 &ndash; Fundamentals of Artificial Intelligence  
2018 Fall, HKUST

Programs by Gerald Liu

Grade: 100%

**For reference only, please DO NOT COPY.**

##  Assignment 1

### Problem 3: Genetic Programming

Files added: `gp/gp.py`, `gp/gp-example-output.txt`

Files moved: `gp/gp-training-set.csv`



Run `python gp/gp.py` with Python 3.

An example output can be found with `cat ./gp-example-output.txt` .

### Problem 4 & 5

Files added: `pacman-hw1/ECAgentLearning.py`, `pacman-hw1/ECAgentTrainingData/*`

Files edited: `pacman-hw1/reactiveAgents.py`



Run everything with Python 2.

For Problem 4, run `python pacman-hw1/pacman.py --layout smallMap --pacman PSAgent`

For Problem 5, run `python pacman-hw1/pacman.py --layout smallMap --pacman ECAgent` 

## Assignment 2

Files edited: `pacman-hw2/search.py`, `pacman-hw2/searchAgents.py`



Run everything with Python 2.

For Task 1, run

`python pacman-hw2/pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic`

For Task 2, run

`python pacman-hw2/pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`

`python pacman-hw2/pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem`

For Task 3, run

`python pacman-hw2/pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5`

## Assignment 3

### Problem 1 & 2

Files edited: `pacman-hw3/valueIterationAgents.py`, `pacman-hw3/qlearningAgents.py`



Run everything with Python 2.

For Problem 1, run `python pacman-hw3/gridworld.py -a value -i 100 -k 10`

For Problem 2, run `python pacman-hw3/gridworld.py -a q -k 5 -m`

### Problem 3 & 4

Files added: `kr/lady.py`, `kr/ranking.py`



Run everything with Python 3.

For Problem 3, run `python kr/lady.py`

For Problem 4, run `python kr/ranking.py`
