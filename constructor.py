class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(10, 20)
point.x = 12
print(point.x)
print(point.y)