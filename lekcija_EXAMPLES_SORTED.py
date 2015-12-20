
### SIMPLE BASIC 1
cars = input("How many cars we have ??? ")
space_in_a_car = input("How many spaces in one cars we have per car??? ")
drivers = input("How many available drivers we have ??? ")
passengers = input("How many available passangers we have ??? ")
cars_not_driven = int(cars) - int(drivers)
cars_driven = drivers
carpool_capacity = int(cars_driven) * int(space_in_a_car)
average_passengers_per_car = int(passengers) / int(cars_driven)
print (("There are ") + str(cars) +  (" cars available "))
print (("There are only ") + str(drivers) + (" drivers available."))
print (("There will be ") + str(cars_not_driven) +  (" empty cars today."))
print (("We can transport ") + str(carpool_capacity) + (" people today."))
print (("We have ") + str(passengers) +  (" to carpool today."))
print (("We need to put about ") +  str(average_passengers_per_car) + (" in each car."))

### SIMPLE BASIC 2
my_name = input("What is Your name ??? ")
my_age = input("What is age ??? ")
my_height = input("What is height ??? ")
my_weight = input("What is weight ??? ")
my_eyes = input("What colour are Your eyes ??? ")
my_teeth = input("What colour are Your teeth ??? ")
my_hair = input("What colour is Your hair ??? ")
print (("Let's talk about %s.") % str(my_name))
print (("He's %d inches tall.") % int(my_height))
print (("He's %d pounds heavy.") % int(my_weight))
print ("Actually that's not too heavy :-) ")
zbir = int(int(my_age) + int(my_height) + int(my_weight))
print (("He's got %s eyes and %s hair.") % (my_eyes, my_hair))
print (("His teeth are usually %s depending on the coffee.") % str(my_teeth))
print (("If I add %d, %d, and %d I get %d.") %
      (int(my_age), int(my_height), int(my_weight), (zbir)))


### SIMPLE BASIC 3
x = ("There are %d types of people.") % (10)
binary = ("binary")
do_not = ("don't")
y = (("Those who know %s and those who %s.") % (binary, do_not))
print (x)
print (y)
print (("I said: %r.") % (x))
print (("I also said: '%s'.") % (y))
hilarious = False
joke_evaluation = ("Isn't that joke so funny?! %r")
print (joke_evaluation % hilarious)
w = ("This is the left side of...")
e = ("a string with a right side.")
print (w + e)


### LEARN THE PYTHON THE HARD WAY
print ("Mary had a little lamb.")
print (("Its fleece was white as %s.") % ("snow"))
print ("And everywhere that Mary went.")
for i in range(1,10):
   print (".....")
end1 = ("C")
end2 = ("h")
end3 = ("e")
end4 = ("e")
end5 = ("s")
end6 = ("e")
end7 = ("B")
end8 = ("u")
end9 = ("r")
end10 = ("g")
end11 = ("e")
end12 = ("r")
print ((end1 + end2 + end3 + end4 + end5 + end6 ) + (" ") +
      (end7 + end8 + end9 + end10 + end11 + end12))

### FORMATTER STRINGS
formatter = ("%r %r %r %r")
print ((formatter) % (1, 2, 3, 4))
print ((formatter) % ("one", "two", "three", "four"))
print ((formatter) % (True, False, False, True))
print ((formatter) % (formatter, formatter, formatter, formatter))
#print formatter % (("I had this thing."),("That you could type up right."),
                  ("But it didn't sing."),("So I said goodnight."))

### FORMATING DAYS
days = ("Mon Tue Wed Thu Fri Sat Sun")
months = ("Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug")
print (("Here are the days: ") + (days))
print (("Here are the months: ") + (months))
print (""" There's something going on here.
With the three double-quotes.
Even 4 lines if we want,
or 5, or 6.""")

### FORMATING STRINGS
tabby_cat = ("\tI'm tabbed in.")
persian_cat = ("I'm split\non a line.")
backslash_cat = ("I'm \\ a \\ cat.")
fat_cat = ("""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""")
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)


### FOR IN LOOP
for i in ["/","-","|","\\","|"]:
       print (("%s\r") % i,)


### BASIC PROGRAM
print ("How old are you? Years?")
age = input()
print ("How tall are you? In cm ")
height = input()
print ("How much do you weight? In kg")
weight = input()
print (("So, you're %r years old, %r cm tall and %r kg heavy.") % (age, height, weight))


### BASIC STRINGS
print ("Rec poruka treba da se odstampa vise puta u istom redu")
stampa = input("koliko puta da se ostampa poruka ")
stampa = int(stampa)
print("Poruka, " * (stampa))

### BASIC INPUT
name = input("Whats Your name ")
country = input("Whats the name of your country ")
name = name.capitalize()
country = country.capitalize()
print ("Hello " + name + " You are living in a " + country)
name = name.upper()
country = country.upper()
zbir = (" ") + name + (" ") + country
print (zbir*4)


### BASIC WITH STRINGS
print('There once was a movie star icon ' + ', who preferred to sleep with the light on')
print('They learned how to code' + " , " + 'a device that sure glowed')
robus =("Python")
robus1 =robus.upper()
print("and lit up the night using " +  robus1)


#MONTHLY INSTALMENT CALCULATOR
#M = L[i(1+i)n] / [(1+i)n-1]
#•	mp = monthly payment
#•	Lla = Loan amount
#•	ir = interest rate (for an interest rate of 5%, i = 0.05)
#•	np = number of payments
mp = 0 #monthly payment
la = 0 #loan amount
ir = 0 #interest rate
np = 0 #number of payments
ld = 0 #loan duration
ti = 0 #total interest rate for the whole period

strla = input("How much money would You like to borrow? ")
strir = input("What is the interest rate on the loan? ")
strld = input("How many years will it take you to pay off the loan? " )
#Convert the strings into floating numbers so we can use them in teh formula
ld = float(strld)
la = float(strla)
ir = float(strir)
ti = float(str(ti))
#Since payments are once per month, number of payments is number of years for the loan * 12
np = ld*12
ir1 = ir/100
print (ir1)
#Calculate the monthly payment based on the formula
mp = la * (ir1 * (1+ ir1) * np) \
   / (((1 + ir1) * np) -1)
ti =(mp * np) - la
#Extra credit
print("Your monthly payment will be $%.2f" % mp)
print("Total interest rate for this perios is $%.2f" % ti)


### AGAIN STRINGS formatting
message = ("hello world, this is davor")
print (message)
print (message.find("davor"))
print (message.count("o"))
print (message.upper())
print (message.capitalize())
print (message.replace("davor","daki"))
postalcode = " "
postalcode = input("What is Your postal code ??? ")
print ("Your postal code is..." + postalcode)
print(postalcode.upper())


### PRINT FORMATTING
age1 = 42
print (age1)
duration = age1 + 34
print (duration)
print ("________________________")
#
age = "42"
print (age)
duration1 = age + " 34"
print (duration1)
print ("________________________")
#
age = "42"
print (age)
duration = age + " + 34 je " + str(duration)
print (duration)
print ("________________________")
#
age2 = 5
squer = age2**2
squer1 =age2**3
squer2 =age2**4
print (squer , squer1 , squer2)
print (squer + squer1 + squer2)
print ("________________________")
#
squer=str(squer)
squer1=str(squer1)
squer2=str(squer2)
print ("5 na 2 je " + (squer) ," ,5 na 3 je " + (squer1) ," ,5 na 4 je " + (squer2))


### LEARN THE PYTHON THE HARD WAY
print ("The capybera is the biggest world rodent")
print ("The capybera can swim")
print ("The capybera is the best")
print ("Its a buatifull day \nin the neigbourghood, so enjoy yourself quite \na bit like everybody ")
print ("here is a double quote " + "single quote ")
print("""This is the strangest way to
print the txt on screen
with multiple quotes """)
print("here is one string " + "and here is another ")


### SMALL CODE BLOCL
name=input("What is your name: ")
print (("Your name must be: "),name)


### SMALL CODE BLOCL
name = input("What is your name ")
city = input("Where do you live ")
country = input("What country is it ")
print ((name) + (" lives in city ") + (city) + (" which is in country ") + (country))



firstName = input("Your first name is ")
lastName = input("Your last name is ")
name = firstName + (" ") + lastName
print ("Your full name is",(name))


### SMALL CODE BLOCL
message=("Davor Svilar is the best so fuck the rest ")
print((message) +"\n")
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.swapcase())
print(message.lower())
print(message.capitalize())
print(message.swapcase())


### SMALL CODE BLOCL
recenica = input("Write a sentance in english: ")
slovo = input("Please input a letter which is repeating in a sentance above ")
print (slovo)
recenicaL = (recenica.count(slovo))
print (recenicaL)
recenicaM = str(recenicaL)
print (recenicaM)
print(("letter ") + (slovo) + (" is reapeating in a sentance ") + (recenicaM) + (" times"))


### Working with DATES !!!
import datetime
currentDate =datetime.date.today()
print (currentDate)
print (currentDate.year)
print (currentDate.month)
print (currentDate.day)
# Change the order of DATE
print (currentDate.day,currentDate.month,currentDate.year)
print ("___________________________________________")
print (currentDate.strftime("%d %b, %Y"))
print (currentDate.strftime("%d %b %Y"))
print (currentDate.strftime("%d %b %y"))
print ("___________________________________________")
print ("Please atend our seminar on %d %b on the current year of %Y ")
print (currentDate.strftime("Please atend our seminar on %d %b on the current year of %Y "))
print (currentDate.strftime("Please atend our seminar on %d %b, on the current year of %Y "))
print ("___________________________________________")
userInput = input("Your birthday is in a format dd/mm/yyyy ??? ")
birthday = datetime.datetime.strptime(userInput, "%d/%m/%Y")
print ("Your birthday is on", birthday)


# Working with DATES !!!
import datetime
currentDate =datetime.date.today()
print (currentDate)
print (currentDate.year)
print (currentDate.month)
print (currentDate.day)
userInput = input("Your birthday is in a format (dd/mm/yyyy) ")
birthday = datetime.datetime.strptime(userInput, "%d/%m/%Y").date()
print("Your birthday is on", birthday)
days = (birthday) - (currentDate)
print(days)


#Working with hours
import datetime
currentTime =datetime.datetime.now()
print (currentTime)
print (currentTime.hour)
print (currentTime.minute)
print (currentTime.second)


## WHOW MANY DAYS UNTILL THE END OF THE PROJECT !!!
import datetime
currentDate = datetime.date.today()
projectDateInput = input("Enter the last date when the project must be finished in (dd/mm/yyyy) format ??? ")
projectDate = datetime.datetime.strptime(projectDateInput, "%d/%m/%Y")
print ("Today is ", currentDate)
print ("___________________________")
print ("Until the end of the project You have left: ")
diffDate1 = projectDate.year - currentDate.year
diffDate2 = projectDate.month - currentDate.month
diffDate3 = projectDate.day - currentDate.day
print (diffDate1,"years ", diffDate2,"months ", diffDate3, "days ")


## IF STATEMENTS BASIC
##If answer == "YES" :
##If not answer == "NO" :
##If total > 100 :
##If not total <= 100 :
answer = input("Would you like an express shippment ")
if answer == "Yes" :
   print ("That will add 10$ to Your purchase")
if answer == "No" :
   print ("Your purchase will be sent via regular mail without extra charge ")
print ("Have a nice day ")


### NASIC INPUT
favoriteTeam = input("Whats Your favorite team ??? ")
favoriteTeam = favoriteTeam.upper()
if favoriteTeam == "SENATORS" :
   print("Go Sens, GO !!!")
   print("Senators are GRRRRRReeeeeat")
print ("Well, Its ok if You prefer footbal or soccer ")


### NASIC INPUT
deposit = input("How much would You like to deposit ??? ")
if int(deposit) >= 100 :
   print ("Deposit is greater the 100, You get a free Toaster ")
print ("Have a nice day ")


### NASIC INPUT
deposit = input("How much would You like to deposit ??? ")
if int(deposit) >= 100 :
   print ("Deposit is greater the 100, You get a free Toaster ")
else:
   print("You get a free coffe mug ")
print ("Have a nice day ")


### NASIC INPUT
freeToaster = False
deposit = input("How much would You like to deposit ??? ")
if int(deposit) > 100 :
   freeToaster = True
#Variuos code
#Variuos code
#Variuos code
if freeToaster :
   print ("Deposit is greater the 100, You get a free Toaster ")
else:
   print("You get a free coffe mug ")
print ("Have a nice day ")


### IF STATEMENT
print ("Welcome shopper on a shipping calculator !!! ")
print ("We are going to calculate based on the money You spent do You get a free shipping or not !!!")
totalPurchase = int(input("How much many did you spend in our store today ??? "))
if totalPurchase < 50 :
   totalPurchase1 = totalPurchase + 10
   print("Your total purchase with shipment is ", totalPurchase1,"in $")
else :
   print("Your total purchase with shipment is ", totalPurchase,"in $")
print("Thanx and have a nice day !!!")


### IF STATEMENT
people = int(input("Haw many people??? "))
cats = int(input("Haw many cats??? "))
dogs = int(input("Haw many dogs??? "))
if people < cats:
   print ("Too many cats! The world is doomed!")
if people > cats:
   print ("Not many cats! The world is saved!")
if people < dogs:
   print ("The world is drooled on!")
if people > dogs:
   print ("The world is dry!")
dogs += 5
if people >= dogs:
   print ("People are greater than or equal to dogs.")
if people <= dogs:
   print ("People are less than or equal to dogs.")
if people == dogs:
   print ("People are dogs.")


### IF STATEMENT
people = int(input("How many people are they??? "))
cars = int(input("How many cars are they??? "))
trucks = int(input("How many trucks are they??? "))
print ("___________________________________")
print ("They are ",people,"people also there is ",cars," cars and the number of trucks is ",trucks)


### IF STATEMENT ELSE
if cars > people:
   print ("We should take the cars.")
elif cars < people:
   print ("We should not take the cars.")
else:
   print ("We can't decide.")
if trucks > cars:
   print ("That's too many trucks.")
elif trucks < cars:
   print ("Maybe we could take the trucks.")
else:
   print ("We still can't decide.")
if people > trucks:
   print ("Alright, let's just take the trucks.")
else:
   print ("Fine, let's stay home then.")


### IF STATEMENT ELSE
print ("You enter a dark room with two doors.  Do you go through door #1 or door #2?")
door = input("Choose door1 or doot 2, with 1 or 2 ")
if door == "1":
   print ("There's a giant bear here eating a cheese cake.  What do you do?")
   print ("1. Take the cake.")
   print ("2. Scream at the bear.")
   bear = input("Choose 1 or 2 ")
   if bear == "1" :
       print ("The bear eats your face off.  Good job!")
   elif bear == "2":
       print ("The bear eats your legs off.  Good job!")
   else:
       print ("Well, doing %s is probably better.  Bear runs away." % bear
elif door == "2" :
   print ("You stare into the endless abyss at Cthulhu's retina.")
   print ("1. Blueberries.")
   print ("2. Yellow jacket clothespins.")
   print ("3. Understanding revolvers yelling melodies.")
   insanity = input("Choose 1,2, or 3 ")
   if insanity == "1" or insanity == "2" :
       print ("Your body survives powered by a mind of jello.  Good job!")
   else:
       print ("The insanity rots your eyes into a pool of muck.  Good job!")
else:
   print ("You stumble around and fall on a knife and die.  Good job!")

### IF STATEMENT ELSE
country = input("What country are you from ")
country = country.upper()
if country == ("CANADA") :
   print ("Helloooooo Canada")
elif country == ("GERMANY") :
   print ("Gutten Tag, wi getz")
elif country == ("FRANCE") :
   print ("bonjour, comment allez-vous")
else :
   print ("De si brate Srbine ")


### IF STATEMENT ELSE
team = input("Whats Your favorite hockey team: ").upper()
if team == "FLYERS":
   print("Best team ever")
if team == "SENATORS":
   print("GO SENS GO !!!")
if team == "RANGERS":
   print("GO RAANGEEEERRSSSSS, GO !!!")
else:
   print(" I don\`t have anything smart to say")


### IF STATEMENT ELSE
wonLottery = True
bigWin = True
wonLottery = input("Did You won the lottery ??? ").upper()
bigWin = input("Did You won big SCORE ??? ").upper()
if wonLottery =="YES":
   print ("So, You are a WIIIIINNNNEEERRRR !!!")
if wonLottery =="YES" and bigWin =="YES" :
   print("You can retire now and enjoy Your life in luxery:-) ")
elif wonLottery=="YES" or bigWin=="NO":
   print("You got something out of playing lottery, but no big Score")
else :
   print("Thats great, but now go back to work and kiss the bosses ass :-) ")
print("Well, we hope You will continue to play our lottery ")



### BE CAREFULL WITH AND and OR
team = input("Whats Your favorite team ??? ").upper()
sport = input ("Whats Your favorite sport ??? ").upper()
# if the sport is hockey and the team is senators or leafs display cup message
if sport=="HOCKEY" and (team=="SENATORS" or team=="LEAFS"):
   print("Get uck with the CUP this year !!!")


### IF STATEMENT ELSE
team = input("Whats Your favorite team ??? ").upper()
sport = input ("Whats Your favorite sport ??? ").upper()
sportisHockey = False
if sport =="HOCKEY":
   sportisHockey = True
teamCurrent = False
if team =="SENATORS" or team=="LEAFS":
   teamCurrent = True
if sportisHockey and teamCurrent :
   print("Good luck with winning the cup this year ")
else :
   print ("You are not into sports ")

### IF STATEMENT ELSE
team = input("Whats Your favorite team ??? ").upper()
sport = input ("Whats Your favorite sport ??? ").upper()
if sport =="HOCKEY":
   print ("GO Hockey !!!")
   if team =="SENATORS":
       print ("Good luck winning the cup !!!")
   print ("We do love hockey")
print("Hockey is the best game ever !!!")


### TURTLE DRAW
import turtle
turtle.color("yellow")
turtle.forward(200)
turtle.right(90)
turtle.color("red")
turtle.forward(200)
turtle.right(90)
turtle.color("blue")
turtle.forward(200)
turtle.right(90)
turtle.color("green")
turtle.forward(200)


### TURTLE DRAW
import turtle
loop = 6
for steps in range(loop):
   turtle.forward(50)
   turtle.right(60)
   turtle.color("red")
   for steps in range(loop):
       turtle.forward(120)
       turtle.right(60)
       turtle.color("blue")


### TURTLE DRAW
import turtle
loop = 7
for steps in range(loop):
   turtle.forward(60)
   turtle.right(360/7)
   turtle.color("red")
   for steps in range(loop):
       turtle.forward(120)
       turtle.right(360/7)
       turtle.color("blue")
       for steps in range(loop):
            turtle.forward(180)
            turtle.right(360/7)
            turtle.color("green")

### DOUBLE FOR LOOP
for steps in [1,2,3,4,5,6]:
   print (steps)
   for steps in [1,3,4,6]:
       print (steps)


###  LOOPS
answer = "0"
while answer !="4":
   answer = input("What is 2 + 2 ??? ")
   print ("Wrong answer ")
print ("YES, 2 + 2 = 4 ")


### WHILE LOOPS
answer = "0"
while answer !="42":
   answer = input("What is the meaning of life by Hitchikers Guide through Galaxy ???  ")
   print ("Wrong answer ")
print ("Damn, thats correct, the planet just exploded :-) ")

#### TURTLE DRAW
import turtle
counter = 0
while counter < 4 :
   turtle.forward(120)
   turtle.right(90)
   counter=counter + 1


### TURTLE DRAW
import turtle
loop = int(input("How many sides of the object You want ??? "))
color1 = input("Choose the colour of the object ??? (red/green/blue/black ")
for steps in range(loop):
   turtle.forward(60)
   turtle.right(360/loop)
   turtle.color(color1)
   for steps in range(loop):
       turtle.forward(120)
       turtle.right(360/loop)
       turtle.color(color1)
       for steps in range(loop):
            turtle.forward(180)
            turtle.right(360/loop)
            turtle.color(color1)



### CREATING A LIST
guests = ["Christopher","Susan","Bill","Satya"]
print(guests[0])


# WORKING WITH LISTS
guests = ["Susan","Christopher","Bill","Satya"]
count = (len(guests))
print (count)
print (guests)
print("First guest is",guests[0])
print("Third guest is", guests[2])
print(guests[-1])
print(guests[3])
# CHANGE THE VALUE IN THE LIST
guests[0]=("Steve")
print (guests)
print("First guest NOW is",guests[0])
# ADD A VALUE TO THE END OF THE LIST
guests.append("Davor")
guests.append("Biljana")
print (guests)
# REMOVE A VALUE FROM THE LIST
guests.remove(guests[3])
print (guests)
guests.remove("Biljana")
print (guests)


# WORKING WITH LISTS 2
guests = ["Susan","Christopher","Bill","Satya"]
guests.append("Colin")
guests.append("Biljana")
guests.append("Davor")
count = (len(guests))
for steps in range(count):
   print (guests[steps])


# WORKING WITH LISTS 3
guests = ["Susan","Christopher","Bill","Satya"]
guests.append("Colin")
guests.append("Biljana")
guests.append("Davor")
for guest in guests:
   print (guest)


# WORKING WITH LISTS 3 - SORTED
guests = ["Susan","Christopher","Bill","Satya"]
guests.append("Colin")
guests.append("Biljana")
guests.append("Davor")
for guest in guests:
   print (guest)
newlist = sorted(guests)
print (newlist)


### A TASK IS TO CREATE AND SORT THE LIST
print ("Please create a list of names invited to a party")
print ("Add a name by name to create a list ")
print ("When you are done, type DONE, to finish creating a list")
print(" ")
guests = []
name =" "
while name != ("DONE"):
   name = input("Please enter a name of the guest ??? ")
   name = name.upper()
   guests.append(name)
   print(" ")
   print("When done with adding names input DONE !!!")
print ("The list has been created ")
guests.remove(guests[-1])
print(" ")
print (guests)
newguests = sorted(guests)
print(" ")
print ("The list has been sorted ")
print (newguests)


## WRITE A LIST TO A FILE
fileName = "demo.txt"
acessMode = "w"
myFile = open(fileName,acessMode)
myFile.write(" This is a list of all people invited to the party: \n")
myFile.write(" ".join(guests))
myFile.close()
print ("The list have been saved in a file ")

## WRITE A LIST TO A FILE
fileName = "demo.csv"
acessMode = "w"
myFile = open(fileName,acessMode)
myFile.write(" This is a list of all people invited to the party: \n")
myFile.write(" Davor, 41 \n")
myFile.write(" Biljana, 39 \n")
myFile.write(" Mica, 70 \n")
myFile.close()
print ("The list have been saved in a file ")


## MORE LOOPS
i = 0
numbers = []
while i < 6:
   print ("At the top i is %d" % i)
   numbers.append(i)

   i = i + 1
   print ("Numbers now: ", numbers)
   print ("At the bottom i is %d" % i)
print ("The numbers: ")
for num in numbers:
   print (numbers)


# PROGRAM WHICH IS WRITING 5 SENTANCES IN A FILE IN DIFFERENT ROWS
print ("This program adds 5 sentances and write into a file")
fileName = "sentances.txt"
write = "w"
mode = "a"
for loop in range(5):
   data = input("Please enter a file info ???: ")
   data = data + (" ") + ("\n")
   file = open(fileName, mode)
   file.write(data)
   file.close()
print (" all 5 sentances has been written into a file !!!")


## BRAKING STRING AND ADDING TO THIS STRING FROM THE LIST
ten_things = ("Apples Oranges Crows Light Sugar")
print ("Wait there are not 10 things in that list. Let's fix that.")
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print (stuff)
print (more_stuff)
while len(stuff) != 10:
   next_one = more_stuff.pop()
   print ("Adding: "), next_one
   stuff.append(next_one)
   print ("There are %d items now." % len(stuff))
print ("There we go: ", stuff)
print ("Let's do some things with stuff.")
print (stuff[1])
print (stuff[-1]) # whoa! fancy
print (stuff.pop())
print (' '.join(stuff)) # what? cool!
print ('#'.join(stuff[3:5])) # super stellar!



## READING FROM A FILE
animalFile = open("tasmania.txt", "r")
allFileContents = animalFile.read()
print (allFileContents)


### READING FROM A FILE BY EASCH LINE
animalFile = open("tasmania.txt", "r")
firstAnimal = animalFile.readline()
print (firstAnimal)
secondAnimal = animalFile.readline()
print (secondAnimal)
thirdAnimal = animalFile.readline()
print (thirdAnimal)
fourthAnimal = animalFile.readline()
print (fourthAnimal)


# READING FROM CSV FILE
import csv
fileName = "demo.csv"
acessMode = "r"
with open(fileName,acessMode) as myCSVfile:
   datafromFile = csv.reader(myCSVfile)
   for currentDataRow in datafromFile:
       print (currentDataRow)



# WORDS IN A RAW FROM CSV FILE
import csv
fileName = "demo.csv"
acessMode = "r"
with open(fileName,acessMode) as myCSVfile:
   datafromFile = csv.reader(myCSVfile)
   for currentDataRow in datafromFile:
       print (currentDataRow)
       for currentWord in currentDataRow:
           print (currentWord)


## LETTERS IN ROWS IN A WORDS
import csv
fileName = "demo.csv"
acessMode = "r"
with open(fileName,acessMode) as myCSVfile:
   datafromFile = csv.reader(myCSVfile)
   for currentDataRow in datafromFile:
       print (",".join(currentDataRow))
       for currentWord in currentDataRow:
           print (" ".join(currentWord))


# DEFINING THE FUCTION ( small programs )
def printMessage():
   print ("Hello World")
   return

printMessage()


## DEFING THE MAIN afterwords define the function and exeecute the program which is "main"
def main():
   printMessage()
   return
def printMessage():
   print ("Hello World")
   return
main()

def main():
   printNames()
   return
def printNames():
   names = ["Christopher","Susan","Davor","Biljana"]
   print (names)
   for name in names:
       print (name)
   return
main()


def displayMessage(greeting,name):
   message = greeting + " , " + name
   print (message)
   return
displayMessage("Hi","Davor")


name1 = input("Whats your name ??? ")
name2 = input("Whats your name ??? ")
name3 = input("Whats your name ??? ")
def printNames(name1,name2,name3):
   names = name1 + " + " + name2 + " + " + name3
   print (names)
   return
printNames(name1,name2,name3)

# DEFINING THE FUCTION
def main():
   names = ["Christopher","Susan","Davor","Biljana"]
   print ("The guest list is: ",names)
   newName = input("Enter last guest so it could be added to the list ??? ")
   names.append(newName)
   printNames(names)
   return
def printNames(list):
   print (list)
   for name in list:
       print (name)
   return
main()

# DEFINING THE FUCTION
def main():
   names=getNames()
   printNames(names)
   return
def getNames():
    names = ["Christopher","Susan","Davor","Biljana"]
    newName = input("Enter last guest so it could be added to the list ??? ")
    names.append(newName)
    return names
def printNames(names):
   print (names)
   for name in names:
       print (name)
   return
main()

# DEFINING THE FUCTION save txt
### Store txt ina file somewhere
def writeText(data, filename):
   file = open(filename, mode = 'w')
   file.write(data)
   return
newTxt = input("Your txt that will be saved in a file ??? ")
writeText(newTxt, "c:\\temp\\newtxt.txt")


# DEFINING THE FUCTION time sort
def timeSort():
   import datetime
   currentDate =datetime.date.today()
   print (currentDate)
   print ("Today date is dd/mm/yyyy ")
   print (currentDate.day,".",currentDate.month,".",currentDate.year)
   return
timeSort()

## LISTS VS DICTIONARIES
things = ["a", "b", "c", "d"]
print (things[0:4])
things.append("Y")
print (things[0:5])
print ("____________________________________________________")
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print (stuff)
print (stuff['name'])
print (stuff['age'])
print (stuff['height'])
stuff['city'] = "San Francisco"
print (stuff['city'])
print (stuff ['name'],stuff['age'],stuff['height'],stuff['city'])


### UNDERSTANDING AND WORKING WITH DICTIONARIES
print ("____________________________________________________")
stuff = {'city': 'San Francisco', 2: 'Neato', 'name': 'Zed', 1: 'Wow', 'age': 39, 'height': 74}
print (stuff)
print ("____________________________________________________")
print (stuff["city"])
print (stuff[2])
print (stuff["name"])
print (stuff[1])
print (stuff["age"])
print (stuff["height"])
print ("____________________________________________________")
print (stuff)
print ("Now we are going to remove the city")
del (stuff["city"])
print ("____________________________________________________")
print (stuff)


## CLASSES
class Bird:
   def __init__(self, kind, call):
       self.kind = kind
       self.call = call
   def do_call(self):
       print ("a %s goes %s" % (self.kind,self.call))
class Parrot(Bird):
   def __init__(self):
       Bird.__init__(self,"Parrot","Kahhhh")
class Cuckoo(Bird):
   def __init__(self):
       Bird.__init__(self,"Cuckoo","Cuckooo Cuu Cuckooo")
if __name__ == ("__main__"):
   parrot = Parrot()
   cuckoo = Cuckoo()
   parrot.do_call
   cuckoo.do_call

## UNDERSTANDING CLASSES;MODULES;OBJECTS
a = 2
b = 3
print (id(a))
print (type(a))
print (a)
print ("__________________")
print (id(b))
print (type(b))
print (b)
print ("__________________")a = "2"
b = 3
print (id(a))
print (type(a))
print (a)
print ("__________________")
print (id(b))
print (type(b))
print (b)


### SAME VALUE SAME TYPE SAME CATEGORY FOR a=b
a = 3
b = a
print (id(a))
print (type(a))
print (a)
print ("__________________")
print (id(b))
print (type(b))
print (b)

### OOP
my_string = "Spam Spam"
print (id(my_string))
print (type(my_string))
print (my_string)


### MORE USING THE CLASSES EXAMPLES
class Song(object):
   def __init__(self, lyrics):
       self.lyrics = lyrics
   def sing_me_a_song(self):
       for line in self.lyrics:
           print (line)
happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family","With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


### HOW TO READ URL
import urllib.request
x = urllib.request.urlopen("http://learncodethehardway.org/words.txt")
print (x.read())

## How to get open source html from web and save it into a ile.txt
import urllib.request
import urllib.parse
x = urllib.request.urlopen("http://learncodethehardway.org/words.txt")
newTxt = (x.read())
newTxt = newTxt.decode("utf-8")
def writeText(data, filename):
   file = open(filename, mode = 'a')
   file.write(data)
   return
writeText(newTxt, "c:\\temp\\NEWtxt.txt")
print (newTxt)


### ERROR HANDLING problem when deviding a number to a 0 ### float divsion by zero !!!
import random
import sys
first =("")
second = ("")
first = input("Enter the first number ??? ")
second = input("Enter the second number ??? ")
first_number = float(first)
second_number = float(second)
try:
   result = first_number / second_number
   print (first + " / " + second + " = " + str(result))

except ZeroDivisionError:
   print("The answer is infinity !!! ")
   sys.exit
except:
   error = sys.exe_info()[0]
   print ("I am trully sorry, something went terrible wrong here ")
   print (error)
print ("I will always RUN !!!")

### ORD function is telling us the value of a letter or a sign on keyboard
x = ord("A")
y = ord("a")
z = ord("0")
w = ord(":")
print (x,y,z,w)


### ORD function with the for function example
characters = ("ABCDG abcdg")
for character in characters:
   print ("The value of character: " + str(character) + " is " + str(ord(character)))

### BE very carefull about simultanious assignements
a = 0
b = 1
a = b
b = a+b
print (a,b)
print ("")
a = 0
b = 1
a,b = b,a+b
print (a,b)

#### input gives us string
number = input("Please enter a number ??? ")
double_number = number*2
print (double_number)
#### converting the string to a interger
double_number = int(number)*2
print (double_number)
#### converting the string to a float
double_number = float(number)*2
print (double_number)


#### input with the eval function
number = eval(input("Please enter a number ??? "))
double_number = number*2
print (double_number)

### SMALL PROGS
result = eval("5+4+6-2-2+12")
print (result)

### EVAL FUNC
result = input("Please enter a calculation ??? ")
result = eval(result)
print (result)


#### Using the sep function for printin function
name = ("Davor")
a = 41
b = 191
c= 99
print ("Gradjanin " + name + " ima " + str(a) + " godina " + str(b) + " cm visine " + str(c) + " kg ")
print ("Gradjanin",name,"ima",a,"godina",b,"cm visine",c,"kilograma",sep = " ")

#### BASIC STRINGS
string1 = ("This is string 1")
string2 = ("This is string 2")
string3 = ("This is string 3")
print (string1)
print (string2)
print (string3)
print (string1,string2,string3,sep = " ")
print (string1,end=" ")
print (string2,end=" ")
print (string3,end=" ")
print ("")


### APSOLUTE abs function
a=(5)
b=(-5)
c=(4.0)
d=(-4.0)
e=(3 + 4j)
print (a)
print (b)
print (c)
print (d)
print (e)
print ("")
print (abs(a))
print (abs(b))
print (abs(c))
print (abs(d))
print (abs(e))
### ili može i ovako
a=abs(5)
b=abs(-5)
c=abs(4.0)
d=abs(-4.0)
e=abs(3 + 4j)
print(a,b,c,d,e)


### FIND out with type function what type of the object is
a=5
b="5"
c=(3,5,2)
d=[4,6,8,9,25]
e=(3 + 4j)
f={4,6,8,24,35}
print (type(a),type(b),type(c),type(d),type(e),type(f),sep=" : ")



### Iterating Python string
welcome = ("Hello World")
print (welcome)
for character in welcome:
   print (character)


### Iterating Python string
welcome = ("Hello World")
print (welcome)
for i in range (0,len(welcome),1):
   print (welcome[i])

### Iterating Python string
welcome = ("Hello World")
print (welcome)
for i in range (0,len(welcome),1):
   print (welcome[i],end=(":"))


### Iterating Python string
welcome = ("Hello World")
print (welcome)
for i in range (len(welcome)-1,-1,-1):
   print (welcome[i],end=(""))



### Iterating Python string
welcome = ("Hello World")
print (welcome)
for character in welcome:
   ansi_valeu = ord(character)
   print ("The ANSI code for character",character,"is",ansi_valeu,sep=" ")

### How mwany words in a sentance
sentance = input("Please input your sentance : ")
sentance = str(sentance)
print (sentance)
count = 0
for word in sentance:
   if word == (" "):
       count = count +1
words = int(count) + 1
print ("In sentance (",sentance,") there is",words,"words",sep=(" "))


### SLICING A STRING

long_string = input("Please input your long string : ")
long_string = str(long_string)
print ("Your long string has ",len(long_string),"characters !!!")
print (long_string)
i = 0
lenght = len(long_string)
print (lenght)

for i in range (0,(lenght),1):
       print (long_string[i],end=(":"))
print ("")
for y in range (0,(lenght),1):
   print(y,end=(":"))
print ("")
print ("Choose the parte in range from 0 to",str(lenght))
rangex = input ("enter range as [x] ")
rangex = int(rangex)
rangey = input ("enter range as [y] ")
rangey = int(rangey)
sliced_string = long_string[rangex:rangey:1]
print ("Selected slice range of long string is :",str(sliced_string))


### FIND WORD IN A SENTANCE
str_1 = ("Never test bath water in the bathroom with both of Your feet")
print (str_1)
lenght = int(len(str_1))
print ("The lenght of the sentance is",lenght,"characters",sep=(" "))
bit_str_1 = str_1.find("both")
print ("The word BOTH is on",bit_str_1,"place of sentance",sep=(" "))


### DEFINING A FUNCTION
def printMessage():
   message = input ("Whats Your message??? ")
   count = int(input("How many times to display this message??? "))
   for i in range (0,(count),1):
      print (message,end=(":"))
      return


### DEFINING A FUNCTION
def printMessage():
   message = input ("Whats Your message??? ")
   count = int(input("How many times to display this message??? "))
   for i in range (0,(count),1):
      print (message,end=(":"))
      return


### DEFINING A FUNCTION
def main():
   timeSort()
   printNames()
   return
def timeSort():
   import datetime
   currentDate =datetime.date.today()
   print (currentDate)
   print ("Today date is dd/mm/yyyy ")
   print (currentDate.day,".",currentDate.month,".",currentDate.year)
   return
def printNames():
   names = []
   count = int(input("How many names do you want, give me a number "))

   for i in range (0,(count),1):
      newName = input ("Tel me your names ??? ")
      names.append(newName)
   print (names)
   return
main()


### DEFINING A FUNCTION-S
def main():
   timeSort()
   print("Now lets consider creating a list of names and storing it in a file")
   newTxt = str(printNames())
   newTxt1 =str(timeSort())
   data = newTxt + newTxt1
   filename = ("c:\\temp\\newtxt.txt")
   writeText(data, filename)
   return
def timeSort():
   import datetime
   currentDate =datetime.date.today()
   print (currentDate)
   print ("Today date is dd/mm/yyyy ")
   newDate =(currentDate.day,currentDate.month,currentDate.year)
   print (newDate)
   return newDate
def printNames():
   names = []
   count = int(input("How many names do you want, give me a number "))
   for i in range (0,(count),1):
       newName = input ("Tel me your names ??? ")
       names.append(newName)
   print (names)
   return names

def writeText(data, filename):
   file = open(filename, mode = 'w')
   file.write(data)
   return
main()

### DEF GET TIME
import time
def get_time():
   epoch_time = time.time()
   total_seconds = int(epoch_time)
   current_seconds = total_seconds % 60
   total_minutes = total_seconds // 60
   current_minutes = total_minutes % 60
   total_hours = total_minutes // 60
   current_hours = total_hours % 24
   print ("HOURS: ",current_hours)
   print ("MINUTES: ",current_minutes)
   print ("SECONDS: ",current_seconds)
   return
get_time()


###DEF GET TIME how its should be with the return value
import time
def get_time():
   epoch_time = time.time()
   total_seconds = int(epoch_time)
   current_seconds = total_seconds % 60
   total_minutes = total_seconds // 60
   current_minutes = total_minutes % 60
   total_hours = total_minutes // 60 + 2
   current_hours = total_hours % 24
   time_now = ("HOURS:"+str(current_hours)+" MINUTES:"+str(current_minutes)+" SECONDS:"+str(current_seconds))
   return time_now
current_time = get_time()
print (current_time)


##DEF MULTIPLY DISPLAY
def multiply_display(message,times):
   for i in range(times):
       print (message)
times = int(input("how many time you like to dsiplay that messssage ??? "))
message = str(input("Whats Your message ??? "))
multiply_display(message,times)


## MULTIPLY DISPLAY MESSAGE by main()
def main():
   times = int(input("how many times you like to dsiplay that messssage ??? "))
   message = str(input("Whats Your message ??? "))
   multiply_display(message,times)
def multiply_display(message,times):
   for i in range(times):
       print (message)
main()

### LOCAL AND GLOBAL SCOPE I
product = 0
def find_product(number_one,number_two):
   product = number_one*number_two
   print ("The LOCAL variable of the product is ",product)
   return (product)


print ("The GLOBAL variable of the product is ",product)
product = find_product(2,4)
print ("The GLOBAL variable of the product is ",product)


### LOCAL AND GLOBAL SCOPE II
product = 0
def find_product(number_one,number_two):
   result = number_one*number_two
   print ("The LOCAL variable of the product is ",result)
   return (result)
print ("The GLOBAL variable of the product is ",product)
product = find_product(2,4)
print ("The GLOBAL variable of the product is ",product)


### LOCAL AND GLOBAL SCOPE
product = 0
def find_product(number_one,number_two):
   result = number_one*number_two
   print ("The LOCAL variable of the product is ",result)
   print ("The GLOBAL 1 variable of the product is ",product)
   return (result)
print ("The GLOBAL 2 variable of the product is ",product)
product = find_product(2,4)
print ("The GLOBAL variable of the product is ",product)


### LOCAL AND GLOBAL SCOPE
product = 0
def find_product(number_one,number_two):
   result = number_one*number_two
   print ("The LOCAL variable of the product is ",result)
   print ("The GLOBAL 1 variable of the product is ",product)
   return (result)

### LOCAL AND GLOBAL SCOPE
print ("The GLOBAL 2 variable of the product is ",product)
product = find_product(2,4)
print ("The GLOBAL variable of the product is ",product)
print ("The GLOBAL variable of the product is ",result)
#### SYSTEM CRASH becouse result is local variable not global


### LOCAL AND GLOBAL SCOPE III and IV
def display():
   print (id(variable1),variable1)
   return (variable1)
variable1 = 34
print (id(variable1),variable1)
display()
print (("_")*34)
# Variable1 inside local scope and in a global scope
def display():
   variable1 = 56
   print (id(variable1),variable1)
   return (variable1)
variable1 = 34
print (id(variable1),variable1)
display()


### LOCAL AND GLOBAL SCOPE V and VI
x = 30
def function():
   x = 50
   print (x)
   return x
print (x)
function()

### LOCAL AND GLOBAL SCOPE 8
x = 30
def function():
   global x
   print (x)
   return x
print (x)
function()


### MODULES MATH
import math
x = math.sqrt(16)
y = math.sin(90)
print (x,y)

# MATH EXAMPLES
from math import sqrt
from math import sin
print (sqrt(16),sin(90))


### HELP ON MODULES
import math
help (math)


##### Defining CLASSES
class Student:
   def __init__(self,name):
       self.name = name
       self.attend = 0
       self.grades = []
       print ("Hi,my name is :",(name).format(self.name))

   def addGrade(self):
       self.grades.append(grade)
   def attendDay(self):
       self.attend
   def getAverrage(self):
       self.grades=sum(self.grades)/len(self.grades)
       return self.grades
def display():
   print ("Thease are my students: Their Grades, Attendees, and Average Grades")
   print (student1.name,student1.grades,student1.attend,student1.getAverrage())
   print (student2.name,student2.grades,student2.attend,student2.getAverrage())
   print (student3.name,student3.grades,student3.attend,student3.getAverrage())
   print (student4.name,student4.grades,student4.attend,student4.getAverrage())

student1 = Student("Davor Svilar")
student2 = Student("Biljana Stanojevic")
student3 = Student("Andreja Komazec")
student4 = Student("Marija Jokanović")
student1.grades = [90,83,93]
student2.grades = [92,82,76]
student3.grades = [85,34,56]
student4.grades = [72,83,90]
student1.attend = 25
student2.attend = 21
student3.attend = 17
student4.attend = 14

display()



#### Defining CLASSES
class Person:
   def __init__(self,name,age):
       self.name = name
       self.age = age
       Person.population += 1
   def __str__(self):
       return ("{0} has been born with the age of {1}".format(self.name,self.age))
   def __del__(self):
       Person.population -= 1
       return ("{0} is dead :-( at the age of {1}".format(self.name,self.age))

Person.population = 0
p1 = Person("Davor Svilar",41)
print (p1)
p2 = Person("Biljana Stanojevic",39)
print (p2)
p3 = Person("Lidija Grozd",29)
print (p3)
p4 = Person("Milan Petrović",19)
print (p4)
print ("Number of persons in class: ",Person.population)



###DEFINING CLASSES FROM INHERITANCE
class Person():
   def __init__(self,name,age):
       self.name = name
       self.age = age
   def __str__(self):
       return ("my name is {0},and my age is {1}".format(self.name,self.age))

class Military(Person):
   def __init__(self,name,age,rank):
       Person.__init__(self,name,age)
       self.rank = rank
   def __str__(self):
       print ("MILITARY")
       return ("my name is {0},and my age is {1} and I am a soldier with the rank {1}".format(self.name,self.age,self.rank))

class Teacher(Person):
   def __init__(self,name,age,sub):
       Person.__init__(self,name,age)
       self.sub = sub
   def __str__(self):
       print ("TEACHER")
       return (Person.__str__(self) + " and I teach {0}".format(self.sub))
class Student(Person):
   def __init__(self,name,age,loans):
       Person.__init__(self,name,age)
       self.loans = loans
   def __str__(self):
       print ("STUDENT")
       return (Person.__str__(self) + " and my student loan is {0}".format(self.loans))

person = Person("Mike",25)
print (person)
person1 = Military("Bruce",34,"Captain")
print (person1)
person2 = Teacher("George",39,"Math")
print (person2)
person3 = Student("Johny",18,"20K EUR")
print (person3)


### DECORATORS SHOUT OR WHISPER
def getTalk(kind):
   # We define functions on the fly
   def shout(word="yes"):
       return word.capitalize()+"!"
##  # Then we return one of them
   if kind == "shout":
       # We don't use "()", we are not calling the function,
       # we are returning the function object
       return shout
   else:
       return whisper
kind = input("shout or whisper???: ")
print (getTalk(kind)())


### DECORATORS SHOUT OR WHISPER and before PRINT
def getTalk(kind):
   # We define functions on the fly
   def shout(word="yes"):
       return word.capitalize()+"!"
   def whisper(word="yes") :
       return word.lower()+"..."
   # Then we return one of them
   if kind == "shout":
       # We don't use "()", we are not calling the function,
       # we are returning the function object
       return shout
   else:
       return whisper
def doSomethingBefore(func):
   print ("I do something before then I call the function you gave me")
   print (func())
kind = input("shout or whisper???: ")
doSomethingBefore(getTalk(kind))



## WHILE CONDITION
condition = 1
while condition < 10:
   print("manje od 10")
   condition = condition + 1
## add for infinitive while loop
while True:
  print("always run)")

## FOR LOOP
example_list = (23,4,5,8,345,68,7890,2,31,234,554,78,)
for number in example_list:
   print (number)


## FOR LOOP with list range
for x in range (2,5):
   example_list = (23,4,5,8,345,68,7890,2,31,234,554,78,)
   print(example_list[x])


## BREAKING OUT OF THE WHILE LOOP
while name != ("DONE"):
   name = input("Please enter a name of the guest ??? ")
   name = name.upper()
   guests.append(name)
   print(" ")
   print("When done with adding names input DONE !!!")
print ("The list has been created ")
guests.remove(guests[-1])
print(" ")
print (guests)


## BASIC FUNC
def func (num1,num2):
   answer = num1+num2
   print ("num1 is ",num1)
   print ("num2 is ",num2)
   print (answer)
func(num1=3,num2=7)


## BASIC FUNC 2
def func (num1,num2):
   answer = num1+num2
   print ("num1 is ",num1)
   print ("num2 is ",num2)
   print (answer)
num1 = int(input("First number is: "))
num2= int(input("Second number is: "))
func(num1,num2)


## IMPORTING MODULES AND COMMANDS FROM MODULES
import statistics
list = [2,5,7,9,12,34,46,67]
x = statistics.mean(list)
print(x)

from statistics import mean
list = [2,5,7,9,12,34,46,67]
x = mean(list)
print(x)

from statistics import mean as y
list = [2,5,7,9,12,34,46,67]
x = y(list)
print(x)

## LISTS
x = [3,5,7,8,9,5,4,3,45,2,34,4]
print (x)
print (x[4])
x.append(100)
print (x)
# na mestu 4 ubaci 200
x.insert(4,200)
print (x)
x.remove(200)
print (x)
# na mestu broj 1 izbaci elemet
x.remove(x[1])
print (x)
# na mestu od 1 do 5 izbaci elemente
print (x[4:8])
x.insert(4,200)
print (x)
print(x.index(200))
print(x.count(4))
print(x.pop(4))
print (x)
x.sort()
print (x)
## LISTS 2
x = [[5,4,3],[6,3,18],[7,8,24],[16,2,10]]
print (x)
print (x[1])
print (x[1],x[2])
print (x[1][1])
print (x[1][0],x[1][1],x[1][2])


## READ DATA DROM CSV
import csv
with open("c:\\temp\\book1.csv") as csvfile:
   readCsv = csv.reader(csvfile, delimiter=",")
   for row in readCsv:
       print (row)
       print (row[0])
       print (row[0],row[1])
       print (row[0],row[1],row[-1])


## READ DATA DROM CSV
import csv
with open("c:\\temp\\book1.csv") as csvfile:
   readCsv = csv.reader(csvfile, delimiter=",")
   names = []
   dates = []
   for row in readCsv:
       print (row)
       name = row[0]
       date = row[3]
       names.append(name)
       dates.append(date)
print (names)
print (dates)


## READ DATA FROM CSV AND MANIPLULATE WITH ELEMENTS and TRY and EXCEPT
import csv
with open("c:\\temp\\book1.csv") as csvfile:
   readCsv = csv.reader(csvfile, delimiter=",")
   names = []
   dates = []
   for row in readCsv:
       print (row)
       name = row[0]
       date = row[3]
       names.append(name)
       dates.append(date)
print (names)
print (dates)
try:
   nameX = input("Whats the name on the list and its related date ???")
   dateX = (names.index(nameX))
   print (dates[dateX])
except:
   print ("This name is not on the list"


## READ DATA DROM CSV and MANIPLULATE WITH ELEMENTS and TRY and EXCEPT with exception (e)
import csv
with open("c:\\temp\\book1.csv") as csvfile:
   readCsv = csv.reader(csvfile, delimiter=",")
   names = []
   dates = []
   for row in readCsv:
       print (row)
       name = row[0]
       date = row[3]
       names.append(name)
       dates.append(date)
print (names)
print (dates)
try:
   nameX = input("Whats the name on the list and its related date ???")
   dateX = (names.index(nameX))
   print (dates[dateX])
except Exception as e:
   print(e)
print ("Continuing")



## READ DATA DROM CSV and MANIPLULATE WITH ELEMENTS and TRY and EXCEPT with exception (e) and before IF and ELSE statment
import csv
with open("c:\\temp\\book1.csv") as csvfile:
   readCsv = csv.reader(csvfile, delimiter=",")
   names = []
   dates = []
   for row in readCsv:
       print (row)
       name = row[0]
       date = row[3]
       names.append(name)
       dates.append(date)
print (names)
print (dates)
try:
   nameX = input("Whats the name on the list and its related date ???")
   if nameX in names:
       dateX = (names.index(nameX))
       print (dates[dateX])
   else:
       print("The name is not in the list of names !!!")
except NameError as e:
   print(e)
print ("Continuing")



## MULTI LINE PRINT !!!
print ("""
So, this is a simple multyline print
that will show You how to do a print
in diffrent rows !!!

*****************
*               *
*               *
*   HELL YEAH!  *
*               *
*               *
*****************

""")


## DICTIONARIES with keys amd values
## key is a single element, value can be lists, tupels, strings, another dictionary...
exDict = {"Bob":27,"Jane":25,"Mark":"Groovy","Pavle":"RED","Killer":[12,3,6,45],"Smurf":"blue"}
print (exDict)
print ("Jane is ",exDict["Jane"])
print ("Smurf is ",exDict["Smurf"])
## ADD TO DICTIONARY
exDict["Dick"] = ("QRAC")
print (exDict)
## DELETE A KEY deletes a value also
del exDict["Mark"]
print (exDict)
## REFERENCE A SPECIFIC VALUE INSIDE A VALEU OF A DICT
print ("Killer is",exDict["Killer"])
print ("First value of Killer is",exDict["Killer"][0])
print ("Second value of Killer is",exDict["Killer"][1])
print ("Third value of Killer is",exDict["Killer"][2])
print ("4th value of Killer is",exDict["Killer"][3])
print ("ALL values of Killer are",exDict["Killer"][0],exDict["Killer"][1]
      ,exDict["Killer"][2],exDict["Killer"][3])


## BUILT IN FUNCTIONS !!!
help ()
abs()
max()
min()
round()
import math
math.floor()
math.sin()
math.ceil()
from math import floor as ff
str()
int()
float()
eval()

## OS MODULE !!!!
import os
curDir = os.getcwd()
print (curDir)
make new dir inside of the project !!!
os.mkdir("NewDir1")
import time
time.sleep(2)
os.rename("NewDir1","NewDir2")
time.sleep(2)
os.rmdir("NewDir2")


## SYS MODULE !!!!
import sys
sys.stderr.write("This is stderr txt \n")
sys.stderr.flush()
sys.stdout.write("This is stdout txt \n")
print(sys.argv)


## LIB FINAL
import urllib.request
import urllib.parse
try:
   url = 'https://www.google.com/search?q=python'
   headers = {}
   headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
   req = urllib.request.Request(url, headers = headers)
   resp = urllib.request.urlopen(req)
   respData = resp.read()
   saveFile = open('withHeaders.txt','w')
   saveFile.write(str(respData))
   saveFile.close()
except Exception as e:
   print(str(e))


### URLLIB PARSING TXT WEBSITES AND SAVE
import os
import sys
import urllib.request
import urllib.parse
import re
try:
   url = 'https://en.wikipedia.org/wiki/Serbia'
   headers = {}
   headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
   req = urllib.request.Request(url, headers = headers)
   resp = urllib.request.urlopen(req)
   respData = resp.read()
   print (respData)
   paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
   print (str(paragraphs))
   for eachp in paragraphs:
       print (eachp)
   saveFile = open('newtxt.txt','w')
   saveFile.write(str(respData))
   saveFile.close()
except Exception as e:
   print(str(e))


### FIRST GUI
from tkinter import *
import time
import webbrowser
from PIL import Image, ImageTk
import winsound

class Window(Frame):
   def __init__(self, master=None):
       Frame.__init__(self, master)
       self.master = master
       self.init_window()
   def init_window(self):
       self.master.title("                                                                                    "
                         "GOOD LOOKING FUNDUROS ON THE ROAD")
       self.pack(fill=BOTH, expand=1)
       menu = Menu(self.master)
       self.master.config(menu=menu)
       edit = Menu(menu)
       edit.add_command(label="Show Img", command=self.showImg())
       edit.add_command(label="Show Text", command=self.showText(time))
       blackButton = Button(self, text="BLACK FUNDURO",command=self.goto_webblack)
       blackButton.place(x=15, y=200)
       redButton = Button(self, text="RED FUNDURO",command=self.goto_webred)
       redButton.place(x=700, y=200)
       exitButton = Button(self, text="CLICK TO EXIT",command=self.client_exit)
       exitButton.place(x=350, y=450)
  def showImg(self):
       load = Image.open("untitled.jpg")
       render = ImageTk.PhotoImage(load)
       img = Label(self, image=render)
       img.image = render
       img.place(x=0, y=0)
   def showText(self,time):
       self.time = time.sleep(0.1)
       self.sound1()
      text = Label(self, text="""
       WHICH ONE DO YOU LIKE MORE, THE BLACK ONE OR THE RED ONE ???
       """)
       text.pack()
   def goto_webblack(self):
       url = 'https://www.facebook.com/davor.svilar'
       webbrowser.open_new_tab(url)
       self.sound2()
   def goto_webred(self):
      url = 'https://www.facebook.com/pavle.bektasevic'
       webbrowser.open_new_tab(url)
       self.sound2()
   def sound1(self):
       winsound.PlaySound("tada.wav", winsound.SND_ALIAS)
   def sound2(self):
       winsound.PlaySound("intro.wav", winsound.SND_ALIAS)
   def client_exit(self):
       self.sound1()
       exit()
root = Tk()
root.geometry("800x483")
app = Window(root)
root.mainloop()


## TKINTERMORE WINDOWS
import tkinter as tk
from tkinter import *
from tkinter import ttk

class Demo1( Frame ):
   def __init__( self ):
       tk.Frame.__init__(self)
       self.pack()
       self.master.title("Demo 1")
       self.button1 = Button( self, text = "Button 1", width = 25,
                              command = self.new_window )
       self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )

  def new_window(self):
       self.newWindow = Demo2()
class Demo2(Frame):
   def __init__(self):
       new =tk.Frame.__init__(self)
       new = Toplevel(self)
       new.title("Demo 2")
       new.button = tk.Button(  text = "Button 2", width = 25,
                               command = self.close_window )
       new.button.pack()
   def close_window(self):
       self.destroy()
def main():
   Demo1().mainloop()
if __name__ == '__main__':
   main()


### TKINTER MORE WINDOWS
import tkinter as tk
class Demo1:
   def __init__(self, master):
       self.master = master
       self.frame = tk.Frame(self.master)
       self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
       self.button1.pack()
       self.frame.pack()
   def new_window(self):
       self.newWindow = tk.Toplevel(self.master)
       self.app = Demo2(self.newWindow)

class Demo2:
   def __init__(self, master):
       self.master = master
       self.frame = tk.Frame(self.master)
       self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
       self.quitButton.pack()
       self.frame.pack()
   def close_windows(self):
      self.master.destroy()

def main():
   root = tk.Tk()
   app = Demo1(root)
   root.mainloop()

if __name__ == '__main__':
  main()


### TKINTER EXAMPLE
import tkinter
class simpleapp_tk(tkinter.Tk):
   def __init__(self,parent):
       tkinter.Tk.__init__(self,parent)
       self.parent = parent
       self.initialize()
   def initialize(self):
       self.grid()
       self.entryVariable = tkinter.StringVar()
       self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
       self.entry.grid(column=0,row=0,sticky='EW')
       self.entry.bind("<Return>", self.OnPressEnter)
       self.entryVariable.set(u"Enter text here.")
       button = tkinter.Button(self,text=u"Click me !",                                command=self.OnButtonClick)
       button.grid(column=1,row=0)
       self.labelVariable = tkinter.StringVar()
       label = tkinter.Label(self,textvariable=self.labelVariable,
                             anchor="w",fg="white",bg="blue")
       label.grid(column=0,row=1,columnspan=2,sticky='EW')
       self.labelVariable.set(u"Hello !")
       self.grid_columnconfigure(0,weight=1)
       self.resizable(True,False)
       self.update()
       self.geometry(self.geometry())
       self.entry.focus_set()
       self.entry.selection_range(0, tkinter.END)
   def OnButtonClick(self):
       self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
       self.entry.focus_set()
       self.entry.selection_range(0, tkinter.END)
   def OnPressEnter(self,event):
       self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
       self.entry.focus_set()
       self.entry.selection_range(0, tkinter.END)
if __name__ == "__main__":
   app = simpleapp_tk(None)
   app.title('my application')
   app.mainloop()


### PARSING THAT WORKS
import urllib.request
import urllib.parse
import re
url = 'https://en.wikipedia.org/wiki/BMW_F_series_single-cylinder'
values = {"s":"basic","submit":"search"}

data = urllib.parse.urlencode(values)
data = data.encode("utf-8")
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
list = ("")
for eachP in paragraphs:
   list = list + eachP

print (list)
saveFile = open('new.txt','w')
saveFile.write(str(list))
saveFile.close()



# LIB FINAL PARSE IT DOES WORK FINE
import urllib.request
import urllib.parse
import re
try:
   url = 'http://learnpythonthehardway.org/book/intro.html'
   headers = {}
   headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
   req = urllib.request.Request(url, headers = headers)
   resp = urllib.request.urlopen(req)
   respData = resp.read()
   paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
   list = ("")
   for eachP in paragraphs:
       list = list + eachP
except Exception as e:
   print(str(e))

print (list)
saveFile = open('newTXT.txt','w')
saveFile.write(str(list))
saveFile.close()


### ANOTHER TKINTER
from tkinter import *
from tkinter.ttk import *

class TkCanvas():
   def __init__(self, root):
       self.frame = Frame(root)
       self.canvas = Canvas(self.frame)
       self.canvas.grid(row=0, column=0, sticky=(N,S,E,W))
       self.draw_rect()
       quit_button = Button(self.frame, text='Quit', command=self.quit)
       quit_button.grid(row=1, column=0, sticky=(S,E))
       self.frame.columnconfigure(0, weight=2)
       self.frame.rowconfigure(0, weight=2)
       self.frame.pack(fill=BOTH, expand=True)
       self.canvas.bind("<Button-1>", self.start_line)
       self.canvas.bind("<B1-Motion>", self.draw_line)
       self.initial = (0,0)
   def start_line(self, event):
       self.initial = (event.x, event.y)
   def draw_line(self, event):
       self.canvas.create_line((self.initial[0], self.initial[1], event.x, event.y))
       self.initial = (event.x, event.y)
   def draw_rect(self):
       self.canvas.create_rectangle((100,100), (30,40))
   def quit(self):
       self.frame.quit()
if __name__ == '__main__':
   root = Tk()
   app = TkCanvas(root)
   root.mainloop()


### ANOTHER TKINTER NOTEs
from tkinter import *
from tkinter.ttk import *
class TkNotebook():
   def __init__(self, root):

       self.frame = Frame(root)
       self.notebook = Notebook(self.frame)

       f1 = Frame(self.notebook, width=200, height=100)
       f2 = Frame(self.notebook, width=200, height=100)
       self.notebook.add(f1, text="Page 1")
       self.notebook.add(f2, text="Page 2")

       self.label = Label(self.frame, text="A Notebook on the left")

       # Layout
       self.frame.grid(row=0, column=0, sticky=(N, S, E, W))
       self.notebook.grid(row=0, column=0, sticky=(N, S, E, W))
       self.label.grid(row=0, column=1, sticky=(E,))

       # Resize rules
       root.columnconfigure(0, weight=1)
       root.rowconfigure(0, weight=1)
       self.frame.columnconfigure(0, weight=2)
       self.frame.rowconfigure(0, weight=2)
   def quit(self):
       self.frame.quit()
if __name__ == '__main__':
   root = Tk()

   app = TkNotebook(root)

   root.mainloop()



## ANOTHER TKINTER CHECK BOX
from tkinter import *
from tkinter.ttk import *
class TtkWidgets():
   def __init__(self, root):

       self.frame = Frame(root)

       self.build_window()

       self.frame.pack()

       menubar = Menu(root)
       root['menu'] = menubar

       menu_file = Menu(menubar)
       menu_file.add_command(label="Quit", command=self.quit)

       menubar.add_cascade(menu=menu_file, label='File')
   def build_window(self):
       cbv = StringVar()
       Combobox(self.frame, textvariable=cbv,
           values=('Canada', 'Sweden', 'Germany')).pack(side=TOP)

       Checkbutton(self.frame, text='Check').pack(side=TOP)
       Radiobutton(self.frame, text='Radio').pack(side=TOP)
       pb = Progressbar(self.frame, orient=HORIZONTAL, length=200, mode='indeterminate')
       pb.start()
   def quit(self):
       self.frame.quit()

if __name__ == '__main__':
   root = Tk()
   app = TtkWidgets(root)
   root.mainloop()


## ANOTHER TKINTER NOT TO SHABBY
from tkinter import *
class WithoutTtk():
   def __init__(self, root):

       self.frame = Frame(root)

       self.build_window()

       self.frame.pack(fill=BOTH)

       menubar = Menu(root)
       root['menu'] = menubar

       menu_file = Menu(menubar)
      menu_file.add_command(label="Quit", command=self.quit)

       menubar.add_cascade(menu=menu_file, label='File')


   def build_window(self):
       label = Label(self.frame, text="How do I look?")
       label.pack(side=TOP)

       button_bad = Button(self.frame, text="Terrible", command=self.quit)
       button_bad.pack(side=LEFT)

       button_good = Button(self.frame, text="Not too shabby", command=self.quit)
       button_good.pack(side=RIGHT)

   def quit(self):
       self.frame.quit()

if __name__ == '__main__':
   root = Tk()
   app = WithoutTtk(root)
   root.mainloop()


##TKINTER TREE
from tkinter import *
from tkinter.ttk import *
class TkTrees():
   def __init__(self, root):
       self.root = root
       self.notebook = Notebook(root)
       f1 = Frame(self.notebook)
       f2 = Frame(self.notebook)
       self.notebook.add(f1, text="Columned List")
       self.notebook.add(f2, text="Tree")
       self.column_treeview(f1)
       self.tree_treeview(f2)
       # Layout
       self.notebook.grid(row=0, column=0, sticky=(N, S, E, W))
       # Resize rules
       root.columnconfigure(0, weight=1)
       root.rowconfigure(0, weight=1)
   def column_treeview(self, parent):
       columns = ('Name', 'Description')
       self.ctree = Treeview(parent, columns=columns, show="headings")
       for col in columns:
           self.ctree.column(col, width=90)
           self.ctree.heading(col, text=col)
       self.ctree.insert('', 'end', values=('Example', 'One row...'))
       self.ctree.insert('', 'end', values=('Example Part 2', 'Another row...'))
       self.ctree.pack(fill=BOTH, expand=1)
   def tree_treeview(self, parent):
       self.ttree = Treeview(parent)
       id = self.ttree.insert('', 'end', text='Example')
       self.ttree.insert(id, 'end', text='First sub item')
       id = self.ttree.insert('', 'end', text='Example Part 2')
       self.ttree.insert(id, 'end', text='A different sub item')
       self.ttree.pack(fill=BOTH, expand=1)
   def quit(self):
       self.root.quit()
if __name__ == '__main__':
   root = Tk()

   app = TkTrees(root)

   root.mainloop()


## MATPLOTLIB BASICS
import matplotlib
from matplotlib import pyplot as plt
plt.plot([2,4,6,9],[4,6,9,12])
plt.show()


## MATPLOTLIB BASICS DAVOR
import matplotlib
from matplotlib import pyplot as plt
x = []
y = []
for count in range(0,3):
   xc = int(input("Give me the 3 values on X axis ????"))
   x.append(xc)
for count in range(0,3):
   yc = int(input("Give me the 3 values on Y axis ????"))
   y.append(yc)
plt.plot(x,y)
plt.title('Davor Svilar GRAPH')
plt.ylabel('Y AXIS')
plt.xlabel('X AXIS')
plt.show()


## MATPLOTLIB BASICS DAVOR 2
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import style
x = []
y = []
style.use('ggplot')
q = int(input("How many coordinates you have ??? :"))
print ("First enter the coordinates for X-axis, and then for Y-axis !!!")
for count in range(0,q):
   xc = int(input("Give me the "+str(q)+" values on X axis ????"))
   x.append(xc)
for count in range(0,q):
   yc = int(input("Give me the "+str(q)+" values on X axis ????"))
   y.append(yc)
plt.plot(x,y,'g',label='line one davor', linewidth=4)
plt.plot(y,x,'r',label='line two svilar', linewidth=8)
plt.grid(True,color='b')
plt.legend()
plt.bar(x, y, color="g",align='center')
plt.bar(y, x, color='r', align='center')

plt.title('Davor Svilar GRAPHICS CHART')
plt.ylabel('Y AXIS')
plt.xlabel('X AXIS')
plt.show(# )


## MATPLOTLIB BASICS DAVOR 3
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
x,y = np.loadtxt('numbers.csv',
                unpack=True,
                delimiter = ',')
plt.plot(x,y,"r",linewidth="3")
plt.plot(x+5,y+10,"b",linewidth="5")
plt.scatter(x+2, y+6, color='g')
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


## EVAL FUNCTION
string to list
list_str = "[1,5,7,8,2]"
list_str = eval(list_str)
print(list_str)
print(list_str[1])


evaluate a code
x = input("see this...")
check_this_out = eval(input("code:"))


## FLASK BEGINNNING !!!
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
   return "DAVOR SVILAR IS THE BEST SO FUCK THE REST"
if __name__ == "__main__":
   app.run()



## EXECUTE FUNCTION (exec)
#
list_str = "[5,6,2,1,6]"
list_str = exec(list_str)
print(list_str)
#
exec("list_str = [1,5,7,8,2]")
print(list_str)
#
exec("def test(): print('oooo snap!!!')")
test()


### WORKING WITH FLASK !!!
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
   return "Hello again world :-) "
@app.route("/gb")
def goodbye():
   return "Goodbye World :-)"
@app.route("/mn")
def mname():
   return "My name is Davor Svilar :-)"
if __name__ == "__main__":
   app.run()


### WORKING WITH FLASK !!!
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
   return ("Hello again world :-) ")

@app.route("/gb")
def goodbye():
   return ("Goodbye World :-)")

@app.route("/user/<username>")
def username(username):
   return ("Hello" + str(username) + "!!!")

@app.route("/mn")
def mname():
   return ("My name is Davor Svilar :-)")

if __name__ == "__main__":
   app.run()


### PYG GAME !!!
pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
if len(original) > 0 and original.isalpha():
   print original
else:
   print 'empty'
first =word[0]
new_word = word + first + pyg
new_word = new_w


## AT THE STORE
stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
def compute_bill(food):
   total = 0
   for item in food:
       if stock[item] >0:
           total = total + prices[item]
       else:
           total = total
   return total
food = ["banana", "orange", "apple"]
print (compute_bill(food))


## STUDENT BECOMES A TEACHER
lloyd = {
   "name": "Lloyd",
   "homework": [90.0, 97.0, 75.0, 92.0],
   "quizzes": [88.0, 40.0, 94.0],
   "tests": [75.0, 90.0]
}
alice = {
   "name": "Alice",
   "homework": [100.0, 92.0, 98.0, 100.0],
   "quizzes": [82.0, 83.0, 91.0],
   "tests": [89.0, 97.0]
}
tyler = {
   "name": "Tyler",
   "homework": [0.0, 87.0, 75.0, 22.0],
   "quizzes": [0.0, 75.0, 78.0],
   "tests": [100.0, 100.0]
}
def average(numbers):
   total = float(sum(numbers))
   return total / len(numbers)

def get_average(student):
   homework = average(student["homework"])
   quizzes = average(student["quizzes"])
   tests = average(student["tests"])
   return .1 * homework + .3 * quizzes + .6 * tests

def get_letter_grade(score):
   if score >= 90:
       return "A"
   elif score >= 80:
       return "B"
   elif score >= 70:
       return "C"
   elif score >= 60:
       return "D"
   else:
       return "F"

def get_class_average(students):
   results=[]
   for x in students:
       get_average(x)
       results.append(get_average(x))
   return average(results)

classList = [lloyd, alice, tyler]
print get_class_average(classList)
print get_letter_grade(get_class_average(classList))


#### SUBMARINES
from random import randint

board = []

for x in range(5):
   board.append(["O"] * 5)

def print_board(board):
   for row in board:
       print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
   return randint(0, len(board) - 1)

def random_col(board):
   return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

for turn in range(4):
   print "Turn", turn + 1

   if guess_row == ship_row and guess_col == ship_col:
       print "Congratulations! You sunk my battleship!"
       break
   else:
       if (guess_row < 0 or guess_row > 4) or \
           (guess_col < 0 or guess_col > 4):
           print "Oops, that's not even in the ocean."
       elif(board[guess_row][guess_col] == "X"):
           print "You guessed that one already."
       else:
           print "You missed my battleship!"
           board[guess_row][guess_col] = "X"
       # Print (turn + 1) here!
       # print_board(board)
       turn = turn + 1
       print turn
       if turn == 3:
           print "Game Over"



#### WHILE LOP CHOICE !!!
choice = input('Enjoying the course? (y/n)')
while choice != "y" and choice != "n":
   choice = input("Sorry, I didn't catch that. Enter again: ")
   print (" Try again and again ")
print ("You got it")


## ROLLING DICE
import random
print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")
count = 0
while count < 3:
   num = random.randint(1, 6)
   print (num)
   if num == 5:
       print ("Sorry, you lose!")
       break
   count += 1
else:
   print ("You win!")

#### INPUT INT instead of strings
while 10:
   x = input("Please enter how many persons do we need to store into database?? ")
   try:
       val = int(x)
       print ('integer entered', val)
       break
   except ValueError:
       print (x, ' is not an integer, You must give me a number')


### SQLITE DATABASE
import sqlite3
import datetime
import time
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()
def tableCreate():
   c.execute("CREATE TABLE stuffToPlot(ID INT, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
def dataEntry():
   c.execute("INSERT INTO stuffToPlot VALUES(1, 1365952181.288,'2013-04-14 10:09:41','Python Sentiment',5)")
   c.execute("INSERT INTO stuffToPlot VALUES(2, 1365952257.905,'2013-04-14 10:10:57','Python Sentiment',6)")
   c.execute("INSERT INTO stuffToPlot VALUES(3, 1365952264.123,'2013-04-14 10:11:04','Python Sentiment',4)")
   conn.commit()
idfordb = 4
keyword = 'Python Sentiment'
value = 7
def dataEntry2():
   date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
   c.execute("INSERT INTO stuffToPlot (ID, unix, datestamp, keyword, value) VALUES (?, ?, ?, ?, ?)",
             (idfordb, time.time(), date, keyword, value))
   conn.commit()


## DATA ENTRY SQLITE 3
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


## SMALL INPUT STRING VS INT
def loop():
   while 1:
       instr = input('Enter an integer')
       try:
           val = int(instr)
           print ('integer entered', val)
           break
       except ValueError:
           print (instr, ' is not an integer')
#loop()

################
#### FLASK PASSING VARIABLE FROM .PY TO .HTML
from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template("index.html",title = " Sviki Diki is the best", paragraph = " SO FUCK THE REST !!!")
if __name__ == "__main__":
    app.run()
#### .HTML
<!DOCTYPE html>
<html lang="en">

<head>

</head>

<body class="body">
	<header>

	</header>
	 <body>
	   <h3>{{ title }}</h3>
	   <br>
		{% for p in paragraph %}
		<p>{{ paragraph }}</p>
		{% endfor %}
	 </body>

</html>

################
#### FLASK PASSING VARIABLE FROM .PY TO .HTML WITH LOGIC
from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def homepage():
    title =  "Sviki Diki is the best"
    paragraph = [" SO FUCK THE REST !!! SO FUCK THE REST !!! SO FUCK THE REST !!!"," SO FUCK THE REST !!! SO FUCK THE REST !!! SO FUCK THE REST !!!"]
    return render_template("index.html",title = title, paragraph = paragraph)
if __name__ == "__main__":
    app.run()
#### .HTML
<!DOCTYPE html>
<html lang="en">

<head>

</head>

<body class="body">
	<header>

	</header>
	 <body>
	   <h3>{{ title }}</h3>
	   <br>
		{% for p in paragraph %}
		<p>{{ paragraph }}</p>
		{% endfor %}
	 </body>

</html>
#### .HTML FOR LOPS TO GET RID OF THE []

<!DOCTYPE html>
<html lang="en">

<head>

</head>

<body class="body">
	<header>

	</header>
	 <body>
	   <h2>{{ title }}</h2>
	   <br>
		{% for p in paragraph %}
		<p>{{ p }}</p>
		{% endfor %}
	 </body>

</html>

### ANOTHER FLASK APP WITH IF ELSE STATEMENT IN HTML AND FOR LOOP ALSO
from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def homepage():
    title =  "Sviki Diki is the best"
    paragraph = [" SO FUCK THE REST !!! SO FUCK THE REST !!! SO FUCK THE REST !!!"," SO FUCK THE REST !!! SO FUCK THE REST !!! SO FUCK THE REST !!!"]
    return render_template("index.html",title = title, paragraph = paragraph)

@app.route('/about')
def aboutpage():
    title =  "About this site"
    paragraph = ["blah blah blah memememememmemememe blah blah blah"]
    pagetype = "about"
    return render_template("index.html",title = title, paragraph = paragraph, pagetype = pagetype)
if __name__ == "__main__":
    app.run()
##### HTML FOR THIS APP
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body class="body">
	 <body>

	   <h2>{{ title }}</h2>
	   <br>
		{% for p in paragraph %}
		<p>{{ p }}</p>
		{% endfor %}

        <br>
        {% if pagetype == "about" %}
		<p>Contact box thing is here !!!</p>
        {% else %}
		<p>Not about page,Contact box thing is not  here !!!</p>
		{% endif %}
	 </body>
</body>
</html>


##### LOGIN PAGE TWO FUNDUROS TEMPLATE
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'TWO' or request.form['password'] != 'FUNDUROS':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
if __name__ == "__main__":
    app.run()

#### HTML FOR LOGIN PAGE !!!
<html>
<head>
	<meta charset="utf-8">
	<title>Login for two funduros page</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="{{ url_for('static', filename='css/bootstrap.min.css') }}" rel="stylesheet">
    <link href="{{ url_for('static', filename='css/full-slider.css') }}" rel="stylesheet">
	<link rel="shortcut icon" href="{{ url_for('static', filename='bmwfavicon.ico') }}">
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
</head>

<html>
  <head>
    <div class="row text-center"><title>Two Funduros login page</title>
  </head>
  <body>
    <div class="row text-center"><div class="container">
      </br>
      </br>
      <h1>Two Funduros login page</h1>
      <h3>You must enter "TWO" for username, and "FUNDUROS" for password to enter the site</h3>
      <br>
      <form action="" method="post">
        <input type="text" placeholder="Username" name="username" value="{{
          request.form.username }}">
         <input type="password" placeholder="Password" name="password" value="{{
          request.form.password }}">
        <input class="btn btn-default" type="submit" value="Login">
      </form>
      {% if error %}
        <p class="error"><strong>Error:</strong> {{ error }}
      {% endif %}
    </div>
  </body>
</html>
</br>
</br>
</br>
</br>

<iframe src="https://onedrive.live.com/embed?cid=8DD35AA789EB428A&resid=8DD35AA789EB428A%21407&authkey=AEDcN2p87CO-wmc" width="320" height="180" frameborder="0" scrolling="no"></iframe>

</html>

#### ANOTHER FLASK SIMPLE SOLUTIONWITH HTML INSIDE ROUTE,this is app.py
from flask import Flask
app = Flask(__name__)

wsgi_app = app.wsgi_app
from routes import *
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
##### This is route.py along with app.py
from flask import Flask, url_for, request, render_template
from app import app

@app.route('/')
def hello():
    return """
<html>
  <body>
  <div class="nav">
    <div class="container">
	<ul>
	  <li>Davor Svilar</li>
	  <li>Browse</li>
	</ul>
	<ul>
	<li>Sign Up</li>
	<li>Log in</li>
	<li>Help</li>
	</ul>
	</div>
	<div class="jumbotron">
	    <div>
	    <h3>"Travel"</h3>
	    <p>"From apartments and rooms to treehouses and boats: stay in unique spaces in 192 countries."</p>
	    <p>
	        <a href="#">"See how to travel on Airbnb"</a>
	    </p>
	    </div>
	    <div class="container">
	       <h1>"Find a place to stay."</h1>
	       <p>"Rent from people in over 34,000 cities and 192 countries."</p>
        </div>
        <div>
            <h3>Subheading</h3>
            <p>Description text.</p>
            <p>
                <a href="#">Link text</a>
            </p>
        </div>
    </div>
  </div>
  </body>
</html>"""


#### ANOTHER SMALL FLASK EXAMPLE of pitanje from routes.py !!!
from flask import Flask, url_for, request, render_template
from app import app
import redis

r=redis.StrictRedis('localhost',6379,0, decode_responses=True,charset='utf-8');
####
@app.route('/')
def hello():
    url = url_for('about');
    link = '<a href="' + url + '">About us!</a>';
    return link;
####
@app.route('/create')
def create():
    return "<h2>This is a create page</h2>"
####
@app.route('/about')
def about():
    return 'We are the knights who say Ni!!';
#####
@app.route('/pitanje/<naslov>')
def pitanje(naslov):
    return "<h2>" + "primer za parametar " + naslov + " koji smo ranije definisali" + "</h2>";


#### FLASK REDIS POP QUIZ AND APP AND ROUTES
from flask import Flask
app = Flask(__name__)
from routes import *

wsgi_app = app.wsgi_app
from routes import *
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
##### ROUTES
from flask import Flask, url_for, request, render_template;
from app import app;
import redis;
r = redis.StrictRedis('localhost',6379,0,charset="UTF-8",decode_responses=True);

@app.route('/')
def hello():
    createLink = "<a href='" + url_for('create') + "'>Create a question</a>";
    return """<html>
                   <head>
                       <title>Hello, world!</title>
                    </head>
                    <body>
                       """ + createLink + """
                    </body>
               </html>""";

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':

        return render_template('CreateQuestion.html');
    elif request.method == 'POST':

        title = request.form['title'];
        question = request.form['question'];
        answer = request.form['answer'];
        r.set(title +':question', question)
        r.set(title +':answer', answer)
        return render_template('CreatedQuestion.html', question = question);
    else:
        return "<h2>Invalid request</h2>";

@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        question = r.get(title+':question')
        return render_template('AnswerQuestion.html', question = question);
    elif request.method == 'POST':
        submittedAnswer = request.form['submittedAnswer'];
        answer = r.get(title+':answer')
        if submittedAnswer == answer:
            return render_template('Correct.html');
        else:
            return render_template('Incorrect.html', submittedAnswer = submittedAnswer, answer = answer);
    else:
        return '<h2>Invalid request</h2>';


### SMALL DEF PROGRAMMS
### reverse txt
def reverse(text):
    r_text = ''
    index = len(text) - 1
    while index >= 0:
        r_text += text[index] #string canbe concatenated
        index -= 1
    return r_text
print reverse("hello, world!")

##### DELETE VOWELS SMALL PROGRAM
def anti_vowel(text):
    resultat = ""
    for i in text:
        if i in "aeiouAEIOU":
            resultat = resultat + ""
        else:
            resultat = resultat + i
    print resultat
    return resultat
anti_vowel("Hey look Words!")