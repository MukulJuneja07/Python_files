import pymysql

con=pymysql.connect(host="localhost",user="root",password="password@123",database="db1")
mycursor=con.cursor()
# qry="Select * from Customer"
# mycursor.execute(qry)
# data=mycursor.fetchall()
# for e in data:
#     for m in e:
#         print(m, end="\t")
#     print()

qry="insert into Customer values(03,25,'ABCD')"
mycursor.execute(qry)
con.commit()