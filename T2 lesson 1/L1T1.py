class Point():
    def __init__(self, x: int, y: int, color = "black"):
        self.x = x
        self.y = y
        self.color = color
points = []
for i in range(1000):
    points.append(Point(i, i).__dict__)
points[1] = Point(1, 1, 'yellow').__dict__
print(points)