import sqlite3
folder = sqlite3.connect("product.db")
getcode = input("enter the id :")

result = folder.execute("SELECT * FROM PRODUCTDATA WHERE PRODUCTCODE= " +getcode )
for i in result:
    print("Product Code :",i[0])
    print("Product Name :",i[1])
    print("PRICE :",i[2])
    print("Distributer Name :", i[3])
    print("Manufacturer Name :",i[4])