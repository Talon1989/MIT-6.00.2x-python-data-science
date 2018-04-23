class Location:
    def __init__(self, x, y):
        """
        :param x: float
        :param y: float
        """
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """
        :param deltaX: float
        :param deltaY: float
        :return: new Location shifted by delta values
        """
        return Location(self.x + deltaX,
                        self.y + deltaY)

    def distFrom(self, other):
        """
        :param other: Location
        :return: hypotenuse with lines of self values - other values
        """
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'