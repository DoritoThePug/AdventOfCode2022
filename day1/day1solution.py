from itertools import groupby

result = sorted([sum(list(map(int,map(str.strip,x[1])))) for x in groupby([line for line in open("./day1/input.txt",'r').readlines()], lambda x: x=='\n') if not x[0]],reverse=True)

print("Part 1: ", result[:1][0])
print("Part 2: ", sum(result[:3]))
