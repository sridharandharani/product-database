# create a new project called product app database name is product, table name is product data are product code ,name, price,distributer name,manufuter name
import sqlite3
folder = sqlite3.connect("Product.db")

# folder.execute(''' CREATE TABLE PRODUCTDATA(
#                     PRODUCTCODE INTEGER PRIMARY KEY AUTOINCREMENT,
#                     NAME TEXT,
#                     PRICE INTEGER,
#                     DISTRIBUTERNAME TEXT,
#                     MANUFACTURERNAME TEXT
# );''')
print("table created ")

get_name = input("Enter the Name :")
get_price = input( "Enter the price :")
get_distributername = input("Enter the Distributer Name :" )
get_manufacturername = input( "Enter the Manufacturer Name :")

folder.execute("INSERT INTO PRODUCTDATA(NAME,PRICE,DISTRIBUTERNAME,MANUFACTURERNAME) \
VALUES('"+get_name+"',"+get_price+",'"+get_distributername+"','"+get_manufacturername+"')")
folder.commit()
folder.close()
print("Inserted sucessfully")