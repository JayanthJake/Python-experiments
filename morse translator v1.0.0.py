import morse_talk as m
# MADE BY JAYANTHJAKE
# version 1.0.0
# program has a lot of suggested errors
# Type 'yogh' to quit
peas = True
x=0
def continuum():
    global peas
    x = str(input("Do you want to 1\)encode or 2\)decode?\n"))
    if x=="1":
        x1=str(input("Do you want to convert it to binary? \n"))
        if x1 == "yes" or x1 == "Yes" or x1=="y":
            user2 = input("Enter your message")
            if user2 == "yogh":
                peas = False
            if peas != False:
                print(m.encode(user2, encoding_type='binary'))
            print("\n")
        else:
            user = input("Enter the message you want to convert to Morse code\n")
            if user == "yogh":
                peas = False
            if peas != False:
                print(m.encode(user))
    elif x=="2":
        x3=str(input("Do you want to decode a binary code?"))
        if x3 == "yes" or x3 == "Yes" or x3 == "y":
            user3 = input("Enter the binary code")
            if user3 == "yogh":
                peas = False
            if peas != False:
                print(m.decode(user3, encoding_type='binary'))
            print("\n")
        else:
            user1 = str(input("Enter the Morse code you want to decode\n"))
            if user1=="yogh":
                peas = False
            if peas != False:
                print(m.decode(user1))
    print("\n")
while peas:
    continuum()
