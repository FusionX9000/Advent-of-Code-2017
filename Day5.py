with open('Day5_input.txt','r') as target:
    input=[int(n) for n in target.read().strip().split('\n')]

#Part 1
pointer = steps = 0
input1=input.copy()
while(pointer<len(input1)):
    input1[pointer],pointer,steps=input1[pointer]+1,pointer+input1[pointer],steps+1
print(steps)

#Part 2
input2=input.copy()
pointer = steps = 0
while(pointer<len(input2)):
    input2[pointer], pointer, steps = input2[pointer] + 1 if input2[pointer] < 3 else input2[pointer]-1 , pointer + input2[pointer], steps + 1
print(steps)