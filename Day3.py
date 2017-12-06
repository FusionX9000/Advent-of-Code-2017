import math
import numpy
numpy.set_printoptions(linewidth=200)

input = 277678

#Part 1 (can be simplified further if odd squares are used)
square = int(math.ceil(math.sqrt(input)))
mid = int(square/2)
new_coords=(0,0)
distance = (square*square)-input

if square%2==0:
    coords = (mid,-(mid-1))
    new_coords = (coords[0],coords[1]+distance) if coords[1]+distance<=mid else (int(2*mid - distance),mid)
else:
    coords = (-mid,mid)
    new_coords = (coords[0],coords[1]-distance) if coords[1]-distance>=(-mid) else ((2*mid+distance),coords[1])

shortest_distance = sum(math.fabs(x) for x in new_coords)
print(new_coords)
print("Shortest Distance",shortest_distance)

#Part 2 (No external package used to traverse array or array-based functions except to pretty-print the arrsay)
square=13 #Sufficiently large 2D array for given input (Variable square reused)
mid = int(square/2) #centre of array
arr = [[0 for i in range(square)] for f in range(square)] #Initialise 2D array of size 'square' with values 0
arr[mid][mid]=1 #Initialise the centre-most element with value 1
coords = [mid,mid] #Initial starting point
move = [(-1,0),(0,-1),(1,0),(0,1)] #list for clockwise movement

#Add all the neighbouring elements of the array at given index
def sum_all(arr,index):
    suma = 0
    neighbours =  [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    for i in neighbours:
        try:
            index2=[sum(x) for x in zip(i,index)]
            suma+=arr[index2[0]][index2[1]]
        except:
            continue
    return suma

#Navigates the boundary of given length and initialises the elements with sum of neighbouring elements
def navigate_boundary(arr,coords,length):
    b=1
    pointer = 0 #Start with anti-clockwise traversal from rightmost edge
    #Loop through boundary of square
    for a in range(length*4):
        arr[coords[0]][coords[1]] = sum_all(arr, coords) - arr[coords[0]][coords[1]]  # element at coord = sum of neigbouring elements
        #If vertice of square reached, reset b to 0
        if b==length:
            b=0
            pointer+=1
            if pointer==4:
                return arr
        #If element at coord > input then print the element and break
        if arr[coords[0]][coords[1]] > input:
            print(arr[coords[0]][coords[1]])
            return
        coords = [sum(x) for x in list(zip(coords, move[pointer]))] #Next coordinate
        b+=1
    return arr

#Loop through all the possible squares which have their centres at the middle of 2D array (ignoring square of length 0)
for a in range(1,mid):
    coords[1]+=1
    t=navigate_boundary(arr, coords, 2 * a)
    if not t: break
    arr=t
    coords[0]+=1

print(numpy.matrix(arr))
