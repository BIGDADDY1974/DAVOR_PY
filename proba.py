def loop():
    while 1:
        instr = input('Enter an integer')
        try:
            val = int(instr)
            print ('integer entered', val)
            break
        except ValueError:
            print (instr, ' is not an integer')
loop()