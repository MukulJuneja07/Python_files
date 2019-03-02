def getid():
    while(1):
        id=input("Enter Customer id")
        if(id.isdecimal()):
            return id
        else:
            print("Enter correct id")
def getage():
    while(1):
        age=input("Enter customer age")
        if(age.isdigit()):
            return age
        else:
            print("Enter correct age")
def getname():
    while(1):
        name=input("Enter customer name")
        if(name.islower()):
            return name
        else:
            print("Enter correct name")
def searchcust(id):
    if(idlist.count(id)==0):
        index=idlist.index(id)
        return index
def deletecust(id):
    index=idlist.index(id)
    idlist.pop(index)
    agelist.pop(index)
    namelist.pop(index)
idlist=[]
agelist=[]
namelist=[]
while(1):
    choice=input("1 for adding customers, 2 for searching customers, 3 for deleting customer, 4 for modifying customers, 5 for display all values , 6 for exit")
    if(choice=='1'):
        id=getid()
        age=getage()
        name=getname()
        idlist.append(id)
        agelist.append(age)
        namelist.append(name)
        print(idlist)
        print(agelist)
        print(namelist)
    elif(choice=='2'):
        id=input("Enter customer id")
        index=searchcust(id)
        print("Customer id: ", id)
        print(idlist)
        print(agelist)
        print(namelist)
    elif(choice=='3'):
        id=input("Enter customer id")
        deletecust(id)





# idlist=[]
# agelist=[]
# namelist=[]
# while(1):
    # choice=input("1 for add customers, 2 for search customers, 3 for delete customers, 4 for modify customers, 5 for display all, 6 for exit")
    # if(choice=='1'):
    #     id = input("Enter customer id")
    #     age = input("Enter customer age")
    #     name = input("Enter customer name")
    #     idlist.append(id)
    #     agelist.append(age)
    #     namelist.append(name)
    # elif(choice=='2'):
    #     name = input("Enter customer name")