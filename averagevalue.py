#to print only int values from list:-
# x=[1,2,5,"abc",3.5,9]
# for e in x:
#     u=int(e)
#     print(u)



#
# x=[0,1,4,9,0,0,0,0]
# for e in x:
#     if(e==0):
#         x.remove(0)
# print(x)


# #to print cetpa in one line:-
# x="cetpa infotech"
# for e in x:
#     print(e,end="")
# print(end="\n")
#
#
# #methods append and extend are used here :-
# x=[1,2,7.5,"abc"]
# y=[5,6]
# x.append(3.5)
# print(x)
# x.extend(y)
# print(x)
# x.append(y)
# print(x)
#
# #method format is used here :-
# x=21
# y="mukul"
# z="juneja"
# print("My name is %s %s and my age is %d"%(y,z,x))
# print("My name is {} {} and my age is {}".format(y,z,x))
# print("My name is {name1} {name2} and my age is {age}".format(age=x,name1=y,name2=z))
#
# #method index is used here:-
# x=[1,2,3.5,"abc"]
# #u=x.index(3.5)
# print(id(x))
#
# #normal printing is done in this:-
# x="cetpa"
# y="infotech"
# print(x,y)
#
# #split method is used here:-
# x="Cetpa Infotech"
# u=x.split()
# print(u)
#
# #split method used:-
# x=input("Enter any number")
# u=x.split()
# print(u)
#
# #split method:-
# x=input("Enter both numbers").split()
# for i in range(len(x)):
#     x[i]=int(x[i])
#     print(i)
#
# x=input("Enter the values")
# for e in range(len(x)):
#     e=x.split()
#     print(e)
#
# #rjust method is used:-
# x="CETpa infotech"
# u=x.rjust(40,"*")
# print(u)
#
# #xpandtabs method:-
# x="CE\t Tpa i\tnfotech"
# u=x.expandtabs(20)
# print(u)
#
# #casefold method:-
# x="CETpa infotech"
# u=x.casefold()
# print(u)
#
# #format method;-
# x=35
# y="vikas"
# print("My name is ",y, "and my age is ",x)
# print("My name is %s and age is %d"%(y,x))
#
# x=input("Enter both numbers").split()
# x[0]=int(x[0])
# print(x)

