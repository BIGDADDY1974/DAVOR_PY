import MySQLdb;
class Client(object):
    def __init__(self):
        self.connection = MySQLdb.connect("localhost","root","kurbla25","quizdb");
        self.cursor = self.connection.cursor();
        return;
    def saveQuestion(self, title, question, answer):
        sql = "INSERT INTO questions VALUES ("+"'"+(title)+"',"+"'"+(question)+"',"+"'"+(answer)+"',"+"1"+")";
        self.cursor.execute(sql);
        self.connection.commit();
        self.connection.close();
        return;
    def getQuestion(self, title):
        sql = "SELECT Description FROM questions WHERE QuestionName = '"+(title)+"'";
        self.cursor.execute(sql);
        results = self.cursor.fetchone();
        question = results;
        self.connection.close()
        for letter in results:
            exit = ""
            if letter != ("'"):
                exit = exit + letter
            else:
                pass
        return exit;
    def getAnswer(self, title):
        try:
            sql = "SELECT CorrectAnswer FROM questions WHERE QuestionName = '"+(title)+"'";
            self.cursor.execute(sql);
            results = self.cursor.fetchone();
            correctAnswer = results;
            self.connection.close();
            for letter in results:
                exit = ""
                if letter != ("'"):
                    exit = exit + letter
            else:
                pass
            return exit;
        except MySQLdb.Error as err:
            return err;




# connection = MySQLdb.connect("localhost","root","kurbla25","quizdb")
# cursor = connection.cursor()
# print ("Conected !!!")
# # print ("")
# title1 = "MACKA999"
# question1 = "KER999"
# answer1 = "MIS999"
# # category1 = "1"
#
# cursor.execute("INSERT INTO questions (QuestionName, Description, CorrectAnswer) VALUES (%s,%s,%s)",(title1, question1, answer1))
# connection.commit()
# # sql = "INSERT INTO questions VALUES ("+"'"+(title1)+"',"+"'"+(question1)+"',"+"'"+(answer1)+"',"+"1"+")"
# # cursor.execute(sql)
# # connection.commit()
# # connection.close()
#
# print ("")
# sql = "SELECT CorrectAnswer FROM questions WHERE QuestionName = '"+(title1)+"'"
# cursor.execute(sql)
# results = cursor.fetchone()
# print (results)
# print ("")
# for letter in results:
#     exit = ""
#     if letter != ("'"):
#         exit = exit + letter
#     else:
#         pass
#
# print (exit)
#
# #
# # # question = results[0]
# #
# # filename= 'data.txt'
# # 1output = '1min' + filename
# #
# #
# # anti_vowel(text):
# #     resultat = ""
# #     for i in text:
# #         if i in "aeiouAEIOU":
# #             resultat = resultat + ""
# #         else:
# #             resultat = resultat + i
# #     print resultat
# #     return resultat


    