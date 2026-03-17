import psycopg2
def table():
    connect = psycopg2.connect(
        dbname="postgres",
        user="postgres", 
        password = "nishant", 
        host = "localhost", 
        port="5432"
    )
    cursor = connect.cursor()

    cursor.execute('''create table employees(Name text, ID int, Age int)''')

    print("Table Created Successfully")

    connect.commit()
    connect.close()

def data1():
    connect = psycopg2.connect(
        dbname="postgres",
        user="postgres", 
        password = "nishant", 
        host = "localhost", 
        port="5432"
    )
    cursor = connect.cursor()

    cursor.execute('''insert into employees(Name, ID, Age) values('Sam', 01, 21)''')

    print("Data added Successfully")

    connect.commit()
    connect.close()

def extract():
    connect = psycopg2.connect(
        dbname="postgres",
        user="postgres", 
        password = "nishant", 
        host = "localhost", 
        port="5432"
    )
    cursor = connect.cursor()

    cursor.execute('''select * from employees''')

    show = cursor.fetchone()
    print(show[0])
    print(show[1])
    print(show[2])

    connect.commit()
    connect.close()


# table()
# data()
# extract()

def data2():
    connect = psycopg2.connect(
        dbname="postgres",
        user="postgres", 
        password = "nishant", 
        host = "localhost", 
        port="5432"
    )
    cursor = connect.cursor()

    name = input("Enter name")
    id  =  input("Enter id")
    age = input("Enter age")

    query = ('''insert into employees(Name, ID, Age) values(%s, %s, %s);''')

    cursor.execute(query, (name, id, age))

    print("Data added Successfully")

    connect.commit()
    connect.close()

data2()