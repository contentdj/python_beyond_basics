from pprint import pprint as pp

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

l = [l1, l2, l3]

pp(l)

transpose = list(zip(*l))
pp(transpose)
