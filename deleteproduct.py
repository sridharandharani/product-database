import sqlite3
folder = sqlite3.connect("product.db")
getcode = input("enter the id :")
folder.execute("DELETE * FROM PRODUCTDATA WHERE PRODUCTCODE="+getcode)
folder.commit()