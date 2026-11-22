class Circle:
    def __init__(self,radius):
        self.radius=radius
    def __str__(self):
        return(f'Radius:{self.radius}')
        
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,value):
        if value<=0:
            raise ValueError('radius shoud be positive!')
        self._radius=value
    @property
    def area(self):
        return self._radius*self._radius*3
c=Circle(1)
c.radius=3
print(c.area)
print(c)

        