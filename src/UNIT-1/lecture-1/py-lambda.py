f1 = lambda x: x
print(f1(1))
print(f1('potato'))
print()

f2 = lambda x, y : x + y
print(f2(3, 2))
print(f2('pot', 'ato'))
print()

f3 = lambda x, y : 'factor' if (x % y == 0) else 'not factor'
print(f3(6, 2))
print(f3(997, 40))
