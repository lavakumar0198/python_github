class Bikes():
    def __init__(self,Bikename,milage,price,year):
        self.a=Bikename
        self.b=milage
        self.c=price
        self.d=year
    def bikedetails(self):
        print("BikeName:",self.a)
        print("Milage:",self.b)
        print("price:",self.c)
        print("year:",self.d)

aa=input("enter bike name:")
bb=int(input("enter milage:"))
cc=float(input("enter price:"))
dd=int(input("enter year:"))
lava_ = Bikes(aa,bb,cc,dd)
lava_.bikedetails()
   