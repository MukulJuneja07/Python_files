# x=int(input("Enter First No."))
# y=int(input("Enter Second No."))
# z=int(input("Enter Third No."))
# if(x>y and x>z):
#     print("x is greatest:",x)
# elif(y>x and y>z):
#     print("y is greatest:",y)
# else:
#     print("z is greatest:",z)

x=int(input("Enter first number."))
y=int(input("Enter second number."))
z=int(input("Enter third number."))
m=int(input("Enter fourth number."))
n=int(input("Enter fifth number."))
if(x>y):
    if(x>z):
        if(x>m):
            if(x>n):
                print("x is the greatest number: ", x)
elif(y>z):
    if(y>m):
        if(y>n):
            if(y>x):
                print("y is the greatest number: ", y)
elif(z>m):
    if(z>n):
        if(z>x):
            if(z>y):
                print("z is the greatest number: ", z)
elif(m>n):
    if(m>x):
        if(m>y):
            if(m>z):
                print("m is the greatest number: ", m)
else:
    print("n is the greatest number: ", n)

# if(x>y and x>z and x>m and x>n):
#     print("x is the greatest number: ", x)
# elif(y>z and y>m and y>n and y>x):
#     print("y is the greatest number: ", y)
# elif(z>m and z>n and z>x and z>y):
#     print("z is the greatest number: ", z)
# elif(m>n and m>x and m>y and m>z):
#     print("m is the greatest number: ", m)
# else:
#     print("n is the greatest number: ", n)

