import sqlite3
folder = sqlite3.connect("product.db")

result = folder.execute("SELECT * FROM PRODUCTDATA ")
for i in result:
    print("Product Code :",i[0])
    print("Product Name :",i[1])
    print("PRICE :",i[2])
    print("Distributer Name :", i[3])
    print("Manufacturer Name :",i[4])