import random

def rnd(max):
    return int(random.random()*max)
total = 10000

counts_selected = 0
counts_failed = 0
for i in range(total):
    doors = []*3
    doors[rnd(3)] = 1
    doors[rnd(3)] = 2
    door_removed = i for i in doors if i == 0
    print(door_removed)
    
    
    