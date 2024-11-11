import sys
import time



print(f"""==== PYTHON CALCULATOR ====
powered by Python [{sys.version}]
this calculator supports addition, subtraction, multiplication and division
type your problem when READY, type "exit" to exit the program
READY.\n""")

exit = False

while not exit :
    inp = input()

    if inp == 'exit' :
        time.sleep(.5)
        exit = True

    try :
        res = eval(inp)
    except ArithmeticError :
        res = 'Error >>> [ArithmeticError]'
    except Exception :
        res = 'Error >>> [Exception]'

    print(f"{inp} = {res}")
    print("")