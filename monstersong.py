apple = True


def monster_inc():
    global apple
    if apple:
        use = input("What's that song?\n")
        if use == "Monster.exe":
            print("Oh yes, you are right")
            apple = False
        else:
            print("Nah..it isn't that\n")


while apple:
    monster_inc()