from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
      return "({}, {})".format(self.x, self.y)

    def dist_to(self, p):
        ysqr = (p.y - self.y)**2
        xsqr = (p.x - self.x)**2
        return sqrt(ysqr + xsqr)

    def abs(self):
        return self.dist_to(Point(0,0))


class Rectangle:
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2

  def getsidelengths(self):
    yperim = max(self.p1.y, self.p2.y) - min(self.p1.y, self.p2.y)
    xperim = max(self.p1.x, self.p2.x) - min(self.p1.x, self.p2.x)
    return yperim, xperim

  def area(self):
    yper, xper = self.getsidelengths()
    return xper * yper

  def perim(self):
    yper, xper = self.getsidelengths()
    return (xper*2)+(yper*2)

  def center(self):
    x = (self.p1.x + self.p2.x)/2
    y = (self.p1.y + self.p2.y)/2
    return Point(x, y)
  


def main():
    p1 = Point(0, 0)
    print(f"The point ({p1.x}, {p1.y}) is at a distance of {p1.abs()} from the origin.")

    p2 = Point(2, 2)
    print(f"It is a distance {p1.dist_to(p2):.5} away from the point ({p2.x}, {p2.y}).")

    myrect = Rectangle(p1, p2)
    print(myrect.area())
    print(myrect.perim())
    print(myrect.center())
    
  
if __name__ == "__main__":
    main()