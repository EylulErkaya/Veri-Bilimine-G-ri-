class circle():
    def __init__(self, radius):
        """initializes self with radius"""
        self.circle_radius= radius
        
        
    def get_radius(self):
        """returns the radius of self"""
        return self.radius
        
    def set_radius(self, radius):
        """radius is a number changes the radius of self to radius"""
        self.radius= radius
        
        
    def get_area(self):
        """ return the area of self using pi= 3.14 """
        return 3.14*self.r*self.r
        
    def equal(self, c):
        "c is a circle object returns true if self and c have the same radius value  "
        return (c.r == self.r)
        
    def bigger(selff, c):
        if c.r >self.r:
            return c
        elif cr < self.r:
            return self

c1= circle(1)
c2= circle(2)