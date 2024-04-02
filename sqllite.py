import sqlite3

## Connectt to SQlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor = connection.cursor()

## create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute("""Insert Into STUDENT values('Sri','Data Science','A',90)""")
cursor.execute("""Insert Into STUDENT values('Jeevan','Machine Learning','B',100)""")
cursor.execute("""Insert Into STUDENT values('Arun','Data Science','A',35)""")
cursor.execute("""Insert Into STUDENT values('Hari','DEVOPS','A',80)""")
cursor.execute("""Insert Into STUDENT values('Haran','DEVOPS','A',66)""")

## Disspaly ALl the records

print("The isnerted records are")
data = cursor.execute("""Select * from STUDENT""")
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
