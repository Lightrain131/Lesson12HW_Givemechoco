x = int(input("Hello there. Please tell me how many friends do you have"))
y = int(input("And also, please tell me how many chocolates they want to give to your friends."))
if x<=0 and y>0:
    print("I'm sorry you don't have any friends")
elif x>0 and y<=0:
    print("If you do not have any chocolate, you need not to share anything.")
elif x<=0 and y<=0:
    print("I'm sorry you don't have any friends")
    print("If you do not have any chocolate, you need not to share anything.")
else:
    z = int(y//x)
    w = int(y%x)
    print("You have", w, "chocolates for yourself")
    print(z, "chocolates should be given to each friends")