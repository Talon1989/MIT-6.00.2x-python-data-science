class Obj:
    def __init__(self, x, y):
        self.x = x
        self.y = y


li = [Obj(0, 0), Obj(0, 1), Obj(2, 2)]

print(li[1].x)

listOfNums = [n for n in range(10)]
evenNumbers = list( filter(lambda x: x % 2 == 0, listOfNums) )
print(evenNumbers)