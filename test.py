import random
comp_pick = (random.randint(1,30))%4
if comp_pick == 0:
    print(comp_pick)
    comp_pick = 1
print(comp_pick)