import math
import itertools

x = 5
char_list = []
print(math.factorial(x))
for i in range(x):
    char_list.append(i + 1)

perm_list = list(itertools.permutations(char_list))
for x in range(len(perm_list)):
    print(*perm_list[x])
