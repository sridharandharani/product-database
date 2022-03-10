import sqlite3
from prettytable import PrettyTable

folder = sqlite3.connect("product.db")

listoftables = folder.execute("SELECT name from sqlite_master where type = 'table' and name = 'PRODUCTDATA' ").fetchall()

if listoftables != []:
    print("Table already exist !")
else:
    folder.execute(''' CREATE TABLE PRODUCTDATA(
                        PRODUCTCODE INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT,
                        PRICE INTEGER,
                        DISTRIBUTERNAME TEXT,
                        MANUFACTURERNAME TEXT ); ''')
    print("table created ")

while True:
    print("Select an option :")
    print("1.Add product ")
    print("2.view all product ")
    print("3.search product using code ")
    print("4.update product using code ")
    print("5.delete product using code ")
    print("6. Exit ")

    choice = int(input("Enter an option :"))
    if choice == 1:

        get_name = input("Enter the Name :")
        get_price = input("Enter the price :")
        get_distributername = input("Enter the Distributer Name :")
        get_manufacturername = input("Enter the Manufacturer Name :")

        folder.execute("INSERT INTO PRODUCTDATA(NAME,PRICE,DISTRIBUTERNAME,MANUFACTURERNAME) \
        VALUES('" + get_name + "'," + get_price + ",'" + get_distributername + "','" + get_manufacturername + "')")
        folder.commit()
        print("Inserted sucessfully")

    elif choice == 2:
        result = folder.execute("SELECT * FROM PRODUCTDATA ")
        table = PrettyTable(["PRODUCT CODE","PRODUCT NAME","PRICE","DISTRIBUTER NAME","MANUFACTURER NAME"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(table)

    elif choice == 3:
        getcode = input("enter the id :")

        result = folder.execute("SELECT * FROM PRODUCTDATA WHERE PRODUCTCODE= " + getcode)
        table = PrettyTable(["PRODUCT CODE", "PRODUCT NAME", "PRICE", "DISTRIBUTER NAME", "MANUFACTURER NAME"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4]])
        print(table)

    elif choice == 4:
        getcode = input("Enter the code to be updated ?")

        getname = input("Enter the product name :")
        getprice = input("Enter the price")
        getdistributer = input("Enter the distributer name :")
        getmanufacturer = input("Enter the manufacturer name :")
        folder.execute("UPDATE PRODUCTDATA SET \
        NAME ='" + getname + "',PRICE = " + getprice + ",DISTRIBUTERNAME ='" + getdistributer + "',MANUFACTURERNAME = '" + getdistributer + "' \
        WHERE PRODUCTCODE =" + getcode)
        folder.commit()
        print("updated sucessfully")

    elif choice == 5:
        getcode = input("enter the id :")
        folder.execute("DELETE FROM PRODUCTDATA WHERE PRODUCTCODE=" + getcode)
        folder.commit()
        print("deleted sucessfully")

    elif choice == 6:
        folder.close()
        break
    else:
        print("Invalid option")


