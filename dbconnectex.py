import MySQLdb

connection = MySQLdb.connect("localhost","root","kurbla25","quizdb")
c = connection.cursor()
c.execute("SELECT * FROM questions")
rows = c.fetchall()
for eachRow in rows:
    print (eachRow)





# c.execute("SELECT * FROM student")
# rows = c.fetchall()
# for eachRow in rows:
#     print (eachRow)
#
# title1 =('PROBA')
# question1 = 'CORBA'
# answer1 = 'GURABIJE'
# category1 = 5
#
# naredba = str("INSERT INTO student VALUES ("+"'"+(title1)+"',"+"'"+(question1)+"',"+"'"+(answer1)+"',"+str(category1)+")")
# c.execute(naredba)
# print ("")
#
# c.execute("SELECT * FROM student")
# rows = c.fetchall()
# for eachRow in rows:
#     print (eachRow)






