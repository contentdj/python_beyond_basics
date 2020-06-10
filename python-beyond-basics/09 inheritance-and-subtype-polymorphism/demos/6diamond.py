class A:
    def func(self):
        return 'A.func'

class B(A):
    def func(self):
        return 'B.func'

class C(A):
    def func(self):
        return 'C.func'

class D(C, B):
    pass

print(D.mro())

d = D()
print(d.func())



# B's methods take precedence over C
class E(B, C):
    pass

e = E()
print(e.func())