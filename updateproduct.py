import sqlite3
folder = sqlite3.connect("product.db")
getcode = input("Enter the code to be updated ?")

getname = input("Enter the product name :")
getprice = input("Enter the price")
getdistributer = input("Enter the distributer name :")
getmanufacturer = input("Enter the manufacturer name :")
folder.execute("UPDATE PRODUCTDATA SET \
NAME ='"+getname+"',PRICE = "+getprice+",DISTRIBUTERNAME ='"+getdistributer+"',MANUFACTURERNAME = '"+getdistributer+"' \
WHERE PRODUCTCODE ="+getcode)
folder.commit()
print("updated sucessfully")