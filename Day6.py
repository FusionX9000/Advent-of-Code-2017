input = "11 11 13 7 0 15 5 5 4 4 1 1 7 1 15 11"
d = [int(x) for x in input.split()]
combinations = {}
steps=0
#Part 1 and Part 2
while(True):
    max_ = max(d)
    pointer = d.index(max_)
    combinations.setdefault(str(d),[0,steps]) #Dictionary values modified for part 2 to include steps
    combinations[str(d)][0]+=1
    if 2 in [x[0] for x in combinations.values()]: #if expression modified for part 2
        print("[Part 2] Number of steps between loop:",steps-combinations[str(d)][1])
        break
    d[pointer]=0
    while(max_>0):
        pointer+=1
        if(pointer==len(d)): pointer = 0
        max_-=1
        d[pointer]+=1
    steps += 1
print("[Part 1]Total number of redistribrutions before repetition:",steps)
