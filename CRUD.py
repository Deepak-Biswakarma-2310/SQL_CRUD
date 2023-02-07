import mysql.connector as connection

mydb = connection.Connect(host = "localhost", user = "root", passwd = "23101999", database = "sqldbtutorial")
# print(mydb)
# query = "show databases"
cursor = mydb.cursor()
# cursor.execute(query)
# print(cursor.fetchall())

def insert():
    print("\n")
    stdid = int(input("Enter your Student ID: "))
    stdname = input("Enter your name: ")
    age = int(input("Enter your age: "))
    phoneno = input("Enter your Phone Number: ")
    stmt = "insert into StudentBio (stdid,stdname,age,phoneno) values (%s,%s,%s,%s)"
    val = (stdid,stdname,age,phoneno)
    try:
        cursor.execute(stmt,val)
        mydb.commit()
        print("Insert Successfully")
        menu()
    except Exception as e:
        print(e)
        print("Error occurred")
        menu()

def read():
    stmt = "select * from StudentBio"
    try:
        cursor.execute(stmt)
        data = cursor.fetchall()
        if len(data)==0:
            print("Database is empty")
            menu()
        else:
            for record in data:
                print(record)
            print("successfully read")
        menu()
    except Exception as e:
        print(e)
        print("\n")
        print("Database is empty")
        menu()

def update():
    choice = input("\nDo you have any row id ? (Y/N): ").lower()
    if choice == "y":
        stdid = int(input("Enter the row id: "))
        stmt = "select * from StudentBio where stdid=%s"
        val = (stdid,)
        try:
            cursor.execute(stmt,val)
            data = cursor.fetchall()
            for record in data:
                stdname = record[1]
                age = record[2]
                phoneno = record[3]
            print("\nChoose one option to update your record: ")
            print("1. Update Name\n2. Update Age\n3. Update Phone Number")
            choice = int(input("Enter your choice: "))
            if choice==1:
                stdname = input("Enter your Name: ")
            elif choice==2:
                age = int(input("Enter your Age: "))
            elif choice==3:
                phoneno = input("Enter your Phone Number: ")
            else:
                print("Sorry wrong input")
                menu()
            stmt = "update StudentBio set stdname=%s,age=%s,phoneno=%s where stdid=%s"
            val = (stdname,age,phoneno,stdid)
            try:
                cursor.execute(stmt,val)
                mydb.commit()
                print("Updated Successfully")
                menu()
            except Exception as e:
                print("Error occurred")
                print(e)
                menu()
        except Exception as e:
            print(e)
            menu()

def delete():
    choice = input("\nDo you have any row id ? (Y/N): ").lower()
    if choice=="y":
        stdid = int(input("Enter the row id: "))
        stmt = "delete from StudentBio where stdid=%s"
        val = (stdid,)
        try:
            cursor.execute(stmt,val)
            mydb.commit()
            print("Successfully deleted")
            menu()
        except Exception as e:
            print(e)
    else:
        print("Create a new record if not exist else go to the read section and get your id")
        menu()

def menu():
    print("\nSelect any option:-\n1. INSERT\n2. READ\n3. UPDATE\n4. DELETE")
    choice = int(input("Enter your choice: "))
    print("\n")
    if choice==1:
        insert()
    if choice==2:
        read()
    if choice==3:
        update()
    if choice==4:
        delete()
    else:
        print("Sorry wrong input chosen")
        menu()

menu()