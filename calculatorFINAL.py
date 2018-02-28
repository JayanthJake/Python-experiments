import re
# This is written by JayanthJake. Feel free to modify
# I am a very intense, die hard patriot of Britain.
existence = True # As long as this is true, the condition runs
condition = 0 # This one stores and prints the value
print("Calculator written in Python.\n")
print("Type 'quit' to exit.\n")
def my_love(): # defining a function
    global condition
    global answer
    global existence
    if condition == 0:
        answer = input("Enter an equation.\n")
    else:
        answer = input(str(condition)) # evaluate the previous value of continue
    if answer == 'quit':
        print("Quitting...Have a good day.\nGOD BLESS BRITAIN ")
        existence = False
    else:
        answer = re.sub('[A-Za-z .," "]', '', answer)
        if condition == 0:
            condition = eval(answer)
        else:
            condition = eval(str(condition) + answer)
    if answer != 'quit':
        print(answer)
while existence:
    my_love()
# Code ends here