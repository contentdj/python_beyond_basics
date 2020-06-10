positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])
print(list(positives))

# filter 0, False, or empty
trues = filter(None, [0, 1, False, True, [], [1,2,3], '', 'hello'])
print(list(trues))