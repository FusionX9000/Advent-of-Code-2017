import math

input = 277678

square = 0
x = math.sqrt(input)
if x%1==0:
    square=int(x)
else:
    square = int(x)+1

mid = int(square/2)

#Part 1
new_coords=(0,0)
distance = (square*square)-input

if square%2==0:
    coords = (mid,-(mid-1))
    new_coords = (coords[0],coords[1]+distance) if coords[1]+distance<=mid else (int(2*mid - distance),mid)
else:
    coords = (-mid,mid)
    new_coords = (coords[0],coords[1]-distance) if coords[1]-distance>=(-mid) else ((2*mid+distance),coords[1])


print(new_coords)

shortest_distance = sum(math.fabs(x) for x in new_coords)

print(shortest_distance)

#Part 2