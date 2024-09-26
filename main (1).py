#Project Name: Donated Books Inventory and Sales Management system
#Made by: Arsheya Mathur
#Session: 2022-23
#Class: 12A

import mysql.connector
from prettytable import PrettyTable

conn=mysql.connector.connect(host='localhost', user='root', password='arsheya42', database='STOCK')



def donate_book():
    conn=mysql.connector.connect(
        host='localhost', database='STOCK', user='root', password='arsheya42')
    cursor=conn.cursor()

    TYPE="Donated"
    BOOK_NAME=input("Enter name of the book: ")
    cursor.execute("select * from BOOKS where trim(BOOK_NAME)='{}'".format(BOOK_NAME))
    cursor.fetchone()
    count=cursor.rowcount
    
    if count!=0:
        QTY=int(input("Enter the quanity: "))
        cursor.execute("UPDATE BOOKS SET QTY=QTY+{} WHERE trim(BOOK_NAME)='{}';".format(QTY,BOOK_NAME))
        cursor.execute("SELECT ID FROM BOOKS WHERE BOOK_NAME='{}';".format(BOOK_NAME))
        ID=str(cursor.fetchone())
        ID=ID.strip("(").strip(")").strip(",")
        print(ID)
        cursor.execute("INSERT INTO TRANSACTIONS(DOT,QTY,TYPE,ID)VALUES(curdate(),'{}','{}',{});".format(QTY,TYPE,ID))
        conn.close()
        
    else:
        AUTHOR_NAME=input("Enter name of the Author: ")
        SERIES_NAME=input("Enter name of the Series: ")
        GENRE=input("Enter the genre: ")
        BOOK_TYPE=input("Enter Book type: ")
        PRICE=float(input("Enter the price: "))
        QTY=int(input("Enter the quanity: "))
        
        sql1="INSERT INTO BOOKS(BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY)VALUES('{}','{}','{}','{}','{}',{},{});".format(BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY)
        cursor.execute("select max(ID) FROM BOOKS;")
        ID=str(cursor.fetchone())
        ID=ID.strip("(").strip(")").strip(",")
        sql2="INSERT INTO TRANSACTIONS(DOT,QTY,TYPE,ID)VALUES(curdate(),{},'{}',{});".format(QTY,TYPE,ID)
        cursor.execute(sql1)
        cursor.execute(sql2)
        conn.close()
        
    print("Book donated successfully")
    
def purchase_book():
    conn=mysql.connector.connect(host='localhost', user='root', password='arsheya42', database='STOCK')
    cursor=conn.cursor()
    
    TYPE="Purchased"
    
    BOOK_NAME=input("Enter the book which you want to purchase: ")
    count=cursor.execute("select count(*) from BOOKS where trim(BOOK_NAME)='{}'".format(BOOK_NAME))
    x=str(cursor.fetchone())
    x=x.strip("(").strip(")").strip(",")
    x=int(x)
    #print(x)
    #count=cursor.rowcount
    #print(count)

    if x==1:
        QTY=int(input("Enter the quantity: "))
        cursor.execute("SELECT QTY FROM BOOKS WHERE BOOK_NAME='{}';".format(BOOK_NAME))
        Q=str(cursor.fetchone())
        Q=Q.strip("(").strip(")").strip(",")
        Q=int(Q)
        #print(Q)
        #print(type(Q))

        if QTY<Q:
            cursor.execute("UPDATE BOOKS SET QTY=QTY-{} WHERE trim(BOOK_NAME)='{}';".format(QTY,BOOK_NAME))
            cursor.execute("SELECT ID FROM BOOKS WHERE BOOK_NAME='{}';".format(BOOK_NAME))
            ID=str(cursor.fetchone())
            ID=ID.strip("(").strip(")").strip(",")
            #print(ID)
            cursor.execute("INSERT INTO TRANSACTIONS(DOT,QTY,TYPE,ID)VALUES(curdate(),'{}','{}',{});".format(QTY,TYPE,ID))
            conn.close()
            print("Book successfully purchased")
            
        else:
            print("Sorry we don't have that much quantity in our inventory")
        
        conn.close()

    else:
        print("There is no book", BOOK_NAME, "in the inventory")


def search_menu():
    conn=mysql.connector.connect(host='localhost', database='STOCK', user='root', password='arsheya42')
    cursor=conn.cursor()

    while True:
        print("What would you like to search?")
        print("Press 1 to search Book")
        print("Press 2 to search Author")
        print("Press 3 to search Series")
        print("Press 4 to search Genre")
        print("Press 5 to search Book Type")
        print("Press 6 to exit search")

        n=int(input("Enter you choice: "))

        if n==1:
            BOOK_NAME=input("Enter the name of the book you want to search: ")
            cursor.execute("select * from BOOKS where BOOK_NAME='{}';".format(BOOK_NAME))
            result=cursor.fetchall()
            table=PrettyTable(['ID','BOOK NAME','AUTHOR NAME','SERIES NAME','GENRE','BOOK TYPE','PRICE','QTY'])
            for ID,BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY in result:
                table.add_row([ID,BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY])    
            print(table)
        
        if n==2:
            AUTHOR_NAME=input("Enter the name of the author you want to search: ")
            cursor.execute("select * from BOOKS where trim(AUTHOR_NAME)='{}';".format(AUTHOR_NAME))
            result=cursor.fetchall()
            table=PrettyTable(['ID','BOOK NAME','AUTHOR NAME','SERIES NAME','GENRE','BOOK TYPE','PRICE','QTY'])
            for ID,BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY in result:
                table.add_row([ID,BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY])    
            print(table)
        
        if n==3:
            SERIES_NAME=input("Enter the name of the series you want to search: ")
            cursor.execute("select * from BOOKS where SERIES_NAME='{}';".format(SERIES_NAME))
            result=cursor.fetchall()
            table=PrettyTable(['ID','BOOK NAME','AUTHOR NAME','SERIES NAME','GENRE','BOOK TYPE','PRICE','QTY'])
            for ID,BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY in result:
                table.add_row([ID,BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY])    
            print(table)
            

        if n==4:
            GENRE=input("Enter the genre you want to search: ")
            cursor.execute("select * from BOOKS where GENRE='{}';".format(GENRE))
            result=cursor.fetchall()
            table=PrettyTable(['ID','BOOK NAME','AUTHOR NAME','SERIES NAME','GENRE','BOOK TYPE','PRICE','QTY'])
            for ID,BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY in result:
                table.add_row([ID,BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY])    
            print(table)

        if n==5:
            BOOK_TYPE=input("Enter the book type you want to search: ")
            cursor.execute("select * from BOOKS where BOOK_TYPE='{}';".format(BOOK_TYPE))
            result=cursor.fetchall()
            table=PrettyTable(['ID','BOOK NAME','AUTHOR NAME','SERIES NAME','GENRE','BOOK TYPE','PRICE','QTY'])
            for ID,BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY in result:
                table.add_row([ID,BOOK_NAME,AUTHOR_NAME,SERIES_NAME,GENRE,BOOK_TYPE,PRICE,QTY])    
            print(table)

        if n==6:
            break


    
    
def main():
    while True:
        print("--------------------------------MAIN MENU-----------------------------------")
        print("1. Donate Book")
        print("2. Purchase Book")
        print("3. Search Menu")
        print("4. Exit Main Menu")

        n=int(input("Enter your choice: "))

        if n==1:
            donate_book()
        if n==2:
            purchase_book()
        if n==3:
            search_menu()
        if n==4:
            break

main()



    
