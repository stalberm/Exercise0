#Micah Stalberg
#Simple math bot that performs simple arithmetic on 2 numbers

def bot():

    while True:
        command = input("SuperMathyBot> ")
        if command == "quit":
            break
        try:
            command, v0, v1 = command.split()
            if command not in ('add','sub','mul','div'):
                raise
            v0, v1 = float(v0), float(v1)
        except:
            print("usage: add|sub|mul|div v0 v1\n       quit")
        else:
            if command == 'add':
                print(v0 + v1)
            elif command == 'sub':
                print(v0-v1)
            elif command == 'mul':
                print(v0*v1)
            elif command == 'div':
                if v1 == 0:
                    print("Can't divide by zero.")
                else:
                    print(v0/v1)

bot()