'''
Problem 4, Assignment 3
COMP 3211, 2018 Fall, HKUST

Author: Gerald Liu

Definitions (Foo, Bar are in { Lisa, Bob, Jim, Mary }):
FooBar = Foo is ranked immediately ahead of Bar
BioFoo = Foo is a biology major

The program will output the variables that are true and analyze the result.
Expected output (with Python 3):

>>> python ranking.py
MaryBob = True
JimLisa = True
BioLisa = True
BobJim = True

Therefore, the ranking is: Mary, Bob, Jim, Lisa.

'''

from __future__ import print_function
from z3 import Bool, And, Or, Not, Implies, Sum, If, Solver

lb = Bool('LisaBob')
bl = Bool('BobLisa')
lj = Bool('LisaJim')
jl = Bool('JimLisa')
lm = Bool('LisaMary')
ml = Bool('MaryLisa')
bj = Bool('BobJim')
jb = Bool('JimBob')
bm = Bool('BobMary')
mb = Bool('MaryBob')
jm = Bool('JimMary')
mj = Bool('MaryJim')
bio_l = Bool('BioLisa')
bio_b = Bool('BioBob')
bio_j = Bool('BioJim')
bio_m = Bool('BioMary')

solver = Solver()
solver.add(
    # Lisa is not next to Bob
    And(Not(lb), Not(bl)),
    # Jim is ranked immediately ahead of a biology major
    Or(
        And(jl, bio_l),
        And(jb, bio_b),
        And(jm, bio_m)
    ),
    # Bob is ranked immediately ahead of Jim
    bj,
    # One of the women (Lisa and Mary) is a biology major
    Or(bio_l, bio_m),
    # One of the women is ranked first
    Or(
        And(Not(bl), Not(ml), Not(jl)),
        And(Not(bm), Not(lm), Not(jm))
    ),
    # A student must have a rank
    Or(lb, bl, lj, jl, lm, ml),
    Or(lb, bl, bj, jb, bm, mb),
    Or(lj, jl, bj, jb, jm, mj),
    Or(lm, ml, bm, mb, jm, mj),
    # A student can be immediately ahead of at most one other student
    Sum([If(b,1,0) for b in [lb, lj, lm]]) <= 1,
    Sum([If(b,1,0) for b in [bl, bj, bm]]) <= 1,
    Sum([If(b,1,0) for b in [jl, jb, jm]]) <= 1,
    Sum([If(b,1,0) for b in [ml, mb, mj]]) <= 1,
    # A student can immediately follow at most one other student
    Sum([If(b,1,0) for b in [bl, jl, ml]]) <= 1,
    Sum([If(b,1,0) for b in [lb, jb, mb]]) <= 1,
    Sum([If(b,1,0) for b in [lj, bj, mj]]) <= 1,
    Sum([If(b,1,0) for b in [lm, bm, jm]]) <= 1,
    # Two students cannot be ahead of each other
    Implies(lb, Not(bl)),
    Implies(lj, Not(jl)),
    Implies(lm, Not(ml)),
    Implies(bj, Not(jb)),
    Implies(bm, Not(mb)),
    Implies(jm, Not(mj))
)

solver.check()
model = solver.model()
[print(var, '= True') for var in model.decls() if model[var] == True]
print('\nTherefore, the ranking is: Mary, Bob, Jim, Lisa.')
