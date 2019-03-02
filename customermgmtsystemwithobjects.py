class customer:
    cusList=[]
    def __init__(self):
        self.id=0
        self.age=0
        self.name=""
    def addcustomer(self):
        customer.cusList.append(self)
    def searchcustomer(self):
        for e in customer.cusList:
            if(e.id==self.id):
                self.age=e.age
                self.name=e.name
    def deletecustomer(self,id):
        for i in range(len(customer.cusList)):
            if(customer.cusList[i].id==id):
                cus=customer.cusList.pop(i)

while(1):
    choice=input("Press 1 for Adding customer \n"
                 "Press 2 for Searching customer \n"
                 "Press 3 for Deleting customer \n"
                 "Press 4 for Modifying customer \n"
                 "Press 5 for  Display all values \n"
                 "Press 6  for exit..")
    if(choice=="1"):
        cus=customer()
        cus.id=input("Enter Customer Id..")
        cus.age=input("Enter Customer Age..")
        cus.name=input("Enter Customer Name..")
        cus.addcustomer()
    elif(choice=="2"):
        cus=customer()
        cus.id=input("Enter Customer Id..")
        cus.searchcustomer()
        print("CusId:", cus.id, "CusAge:", cus.age, "CusName:", cus.name)
    elif(choice=="3"):
        cus=customer()
        cus.id=int(input("Enter customer id.."))
        cus.deletecustomer(id)
        # id=input("Enter Id to delete..")
        # customer.deletecustomer(id)
        # flag=customer.deletecustomer(id)
        # # print(flag)