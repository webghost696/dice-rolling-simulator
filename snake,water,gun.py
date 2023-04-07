# program to play snake water gun with the user
for i in range(0,100):
    import random
    f=int(input("If u want to exit press 1\nIf you want to continue press any key:"))
    if(f==1):
        break
    else:
        print("1.snake\n2.water\n3.gun")
        a=int(input("enter the choice:\n"))
        if(a>3):
            raise ValueError
        c=random.randint(1,3)
        dic={1:"snake",2:"water",3:"gun"}
        print(f"CPU: {dic[c]}")
        if(a==c):
            print("draw")
        elif(a==1 and c==2):
            print("you win!!")
        elif(a==2 and c==1):
            print("you lose!!")
        elif(a==1 and c==3):
            print("you lose!!")
        elif(a==2 and c==3):
            print("you win!!")
        elif(a==3 and c==2):
            print("you lose!!")
        elif(a==3 and c==1):
            print("you win!!")