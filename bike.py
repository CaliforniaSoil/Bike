class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0 
    def displayInfo(self):
        print self.price 
        print self.max_speed 
        print self.miles
    def ride(self):
        self.miles += 10
        return self
    def reverse(self):
        if self.miles >= 5:
            self.miles -= 5
        return self
bike1 = bike('$100','30mph')
bike2 = bike('$100','30mph')
bike3 = bike('$100','30mph')
bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
