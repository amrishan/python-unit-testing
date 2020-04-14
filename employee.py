class Employee:
    
    raise_amount = 1.05
    
    def __init__(self, first, last, pay): 
        self.first = first #instance variables
        self.last = last
        self.pay = pay
        
    @property   #helps to treat method like an attribute
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)
    
    @property
    def full_name(self): 
        return "{} {}".format(self.first, self.last)
    
    def pay_raise(self):
        self.pay = self.pay * self.raise_amount