class AlternateIterable:
    def __init__(self):
        self.data = [1, 2, 3]

    def __getitem__(self, idx):
        return self.data[idx]

for i in AlternateIterable():
    print(i)