class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.t = (self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.t


a = [Point(-34, 72), Point(-23, -45), Point(4, 5), Point(34, -43), Point(-32, -26), Point(44, 66), Point(34, 43), Point(34, 53), Point(32, 23)]
max = a[0].get_coords()
for p in a:
    if p.get_x() < max[0]:
        max = p.get_coords()
    if p.get_y() < max[1]:
        max = p.get_coords()
print(max)


