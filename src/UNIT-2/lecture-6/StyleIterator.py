

class StyleIterator:
    def __init__(self, styles):
        """
        :param styles: tuple of strings to be used with pylab for plotting
        """
        self.index = 0
        self.styles = styles


    def nextStyle(self):
        # result = self.styles[self.index]
        # if self.index == len(self.styles) - 1:
        #     self.index = 0
        # else:
        #     self.index += 1
        # return result
        stile = self.styles[self.index % len(self.styles)]
        self.index += 1
        return stile