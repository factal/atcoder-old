import itertools
import collections

s_1 = input()
s_2 = input()
s_3 = input()

character = list(set(s_1 + s_2 + s_3))
nums = [str(i) for i in range(10)]
table = {e:i for i, e in enumerate(character)}

if len(character) > 10:
    print('UNSOLVABLE')
    exit()
else:
    for number_combinations in itertools.permutations(nums, len(character)):
        if number_combinations[table[s_1[0]]] == '0' or number_combinations[table[s_2[0]]] == '0' or number_combinations[table[s_3[0]]] == '0':
            continue
        n_1, n_2, n_3 = ('', '', '')
        for i in s_1:
            n_1 += number_combinations[table[i]]
        for i in s_2:
            n_2 += number_combinations[table[i]]
        for i in s_3:
            n_3 += number_combinations[table[i]]
        n_1, n_2, n_3 = int(n_1), int(n_2), int(n_3)
        if n_1 + n_2 ==  n_3:
            print(n_1, n_2, n_3, sep='\n')
            exit()
print('UNSOLVABLE')