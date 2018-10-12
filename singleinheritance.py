class Apple:
    
    model ="iphone X"
    price = 100000

    def rate(self):
        print("Aravind's mobile rate is:", self.price)
        
class discount(Apple):
    
    def __init__(self):
        self.release = 2018

    def total(self):
        print("The person's mobile model:{} total cost {}".format(self.model,self.release))

mc = discount()
mc.total()
mc.rate()
