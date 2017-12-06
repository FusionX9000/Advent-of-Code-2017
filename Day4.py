with open('day4_input.txt','r') as target:
    input = target.read().strip()

#Part 1
correct_pass = sum([1 for x in input.split('\n') if len(x.split())==len(set(x.split()))])
print(correct_pass)

#Part 2
correct_pass = sum([1 for b in input.split('\n') if len(set([''.join(sorted(a)) for a in b.split()]))==len(b.split())])
print(correct_pass)

