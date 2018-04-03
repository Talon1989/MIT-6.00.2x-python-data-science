class Food:
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'