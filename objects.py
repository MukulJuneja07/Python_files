class calculator:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
    def add(self):
        self.z=self.x + self.y
    def sub(self):
        self.z=self.x - self.y
    def mul(self):
        self.z=self.x * self.y
    def divi(self):
        self.z=self.x / self.y
class calc:
    def __init__(self):
        self.m=0
        self.n=0
        self.o=0
    def modulus(self):
        self.o=self.m % self.n
while(1):
    ob=calculator()
    ob.x=int(input("Enter first number"))
    ob.y=int(input("Enter second number"))
    choice=input("Enter choice +,-,*,/")
    if(choice=="+"):
        ob.add()
        print(ob.z)
        print(type(ob.z))
    elif(choice=="-"):
        ob.sub()
        print(ob.z)
        print(type(ob.z))
    elif(choice=="*"):
        ob.mul()
        print(ob.z)
        print(type(ob.z))
    else:
        ob.divi()
        print(ob.z)
        print(type(ob.z))
    obj=calc()