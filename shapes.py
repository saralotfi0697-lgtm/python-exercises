from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r*self.r*3.14
    def __lt__(self, other):
        return self.r<other.r
    def __add__(self, other):
        return Circle(self.r+other.r)


c=Circle(2)
print(c.area())
print('----')
print(Circle(2)<Circle(5))
print(Circle(9)<Circle(8))
print('----')
ob1=Circle(2)
ob2=Circle(3)
ob3=Circle(1)
ob4=Circle(8)
ob5=Circle(5)
Circles=[ob1,ob2,ob3,ob4,ob5]
ob6=ob1+ob4
print(ob6.r)

print(sorted(Circles))

for i in sorted(Circles):
    print(i.r)