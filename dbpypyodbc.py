import pypyodbc
try:
    myConnection=pypyodbc.connect('DRIVER={SQL Server};''SERVER=localhost;''DATABASE=quizdb;''UID=root;PWD=kurbla25')

except:
    print("Could not connect")


