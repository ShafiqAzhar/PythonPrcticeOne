class Point:
    def move(self):
        print('Move')
    def draw(self):
        print('Draw')


point1 = Point()
point1.draw()
point1.x = 10
print(point1.x)
point2 = Point()
point2.move()