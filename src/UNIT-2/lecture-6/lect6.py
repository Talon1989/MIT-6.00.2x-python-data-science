from Drunk import Drunk
from Drunk import UsualDrunk
from Field import Field
from Location import Location


def walk(f, d, steps):
    """
    :param f: instance of Field
    :param d: instance of Drunk
    :param steps: int >= 0, times 'd' moves
    :return: distance between starting and final location
    """
    assert isinstance(f, Field); assert isinstance(d, Drunk)
    start = f.getLoc(d)
    for _ in range(steps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


patatino = UsualDrunk('patatino')
f1 = Field()
f1.addDrunk(patatino, Location(0,0))
print(walk(f1, patatino, 15))
print()