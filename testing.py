
while 10:
    x = input("Please enter how many persons do we need to store into database?? ")
    try:
        val = int(x)
        print ('integer entered', val)
        break
    except ValueError:
        print (x, ' is not an integer, You must give me a number')