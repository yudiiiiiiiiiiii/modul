import math

class circle:
    def __init__(sl, x, y, r):
        sl.X = x
        sl.y = y
        sl.r = r


    def Area(sl):
        return math.pi*sl.r*sl.r