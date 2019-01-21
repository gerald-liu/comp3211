'''
Problem 3, Assignment 3
COMP 3211, 2018 Fall, HKUST

Author: Gerald Liu

There are three rooms.
One room contains a lady and each of the other two contain a tiger.
At most one of the following statements on the signs of the rooms is true:
Statement 1 (Room I): A TIGER IS IN THIS ROOM.
Statement 2 (Room II): A LADY IS IN THIS ROOM.
Statement 3 (Room III): A TIGER IS IN ROOM II.

Since Statement 2 and 3 contradict each other, one of them must be true..
Since Statement 2 implies Statement 1 and at most one statement can be true, Statement 2 must be false.
Therefore, Statement 3 is true, which implies that Statement 1 is false, so the lady is in Room I.

Let p, q, r denotes the events that the lady is in Room I, II, III respectively.
Statement 1: Not(p)
Statement 2: q
Statement 3: Not(q)

The program will output the variables that are true and analyze the result.
Expected output (with Python 3):

>>> python lady.py
Lady in Room I = True

That is, the lady is in Room I.

'''

from __future__ import print_function
from z3 import Bool, And, Or, Not, Sum, If, Solver

p = Bool('Lady in Room I')   # Lady in Room I
q = Bool('Lady in Room II')  # Lady in Room II
r = Bool('Lady in Room III') # Lady in Room III

solver = Solver()
solver.add(
    # The lady is in only one of the three rooms
    Sum([If(b,1,0) for b in [p, q, r]]) == 1,
    # At most one statement is true
    Or(
        # Room I is true
        And(
            Not(p),
            Not(q),
            q
        ),
        # Room II is true
        And(
            p,
            q,
            q
        ),
        # Room III is true
        And(
            p,
            Not(q),
            Not(q)
        ),
        # All are false
        And(
            p,
            Not(q),
            q
        )
    )
)

solver.check()
model = solver.model()
[print(var, '= True') for var in model.decls() if model[var] == True]
print('\nThat is, the lady is in Room I.')
