#using Chart parser
import nltk
from nltk import CFG
grammar = CFG.fromstring("""
S -> NP VP 
NP -> Det N 
VP -> V NP | V 
Det -> 'The' | 'a' |'an'
N -> 'bear'|'squirrel'|'dog'
NP -> N
V -> 'eat' | 'eats' """)
cp = nltk.ChartParser(grammar)
sentence = [s.split() for s in ['The bear eat an squirrel','The dog eats']]
for s in sentence:
    for node in cp.parse(s):
        print(''.join(s))
        print(node)
        print(node.draw())
        print('\n------------\n')
from nltk.parse import ShiftReduceParser
grammar = CFG.fromstring("""
S -> NP VP 
NP -> Det N 
VP -> V NP | V 
Det -> 'The' | 'a' |'an'
N -> 'bear'|'squirrel'|'dog'
NP -> N
V -> 'eat' | 'eats' """)
#using Shift Reduce Parser
sr = ShiftReduceParser(grammar)
sentence = [s.split() for s in ['The bear eat an squirrel','The dog eats']]
for s in sentence:
    for node in sr.parse(s):
        print(''.join(s))
        print(node)
        print(node.draw())
        print('\n------------\n')