import math

class Triangle(object):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        """Constructor"""
        self.A = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.B = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        self.C = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    def perimeter(self):
        per = self.A + self.B + self.C
        return round(per,2)
    def area(self):
        p = (self.perimeter())/2
        area = math.sqrt(p*(p-self.A)*(p-self.B)*(p-self.C))
        return round(area,2)

    def exist(self):
        if( (self.A +self.B > self.C) & (self.A +self.C > self.B) & (self.B +self.C > self.A)  ):
            return 1
        else:
            return 0
trig = Triangle(0,0,3,0,3,3)

print(trig.perimeter())
print(trig.area())
print(trig.exist())