import sqlite3
import datetime
import time
import datetime
conn = sqlite3.connect('test9.db')
c = conn.cursor()
def tableCreate():
    c.execute("CREATE TABLE davor_table(ID INT, datestamp TEXT, name TEXT, age INT, city TEXT, state TEXT, grade INT)")
def dataEntry():
    print (" FIRST WE NEED TO ENTER US A NUMBER OF ROWS !!!")
    while 1:
        x = input("Please enter how many persons do we need to store into database?? ")
        try:
            val = int(x)
            print ('integer entered', val)
            break
        except ValueError:
            print (x, ' is not an integer, You must give me a number')
    x = int(x)

    for i in range (x):
        idfordb = i
        name = str(input("Whats the name ??? "))
        while 2:
            age = input("Whats Your age ??? ")
            try:
                val = int(age)
                print ('integer entered', val)
                break
            except ValueError:
                print (age, ' is not an integer, You must give me a number')
        age = int(age)
        city = str(input(" In which city doYou live ???"))
        state = str(input(" In which state doYou live ???"))

        while 3:
            grade = input("Whats Your grade ??? ")
            try:
                val = int(grade)
                print ('integer entered', val)
                break
            except ValueError:
                print (grade, ' is not an integer, You must give me a number')
        grade = int(grade)
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO davor_table (ID, datestamp, name, age, city, state, grade) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (idfordb, date, name, age, city, state, grade))
    conn.commit()
tableCreate()
dataEntry()


