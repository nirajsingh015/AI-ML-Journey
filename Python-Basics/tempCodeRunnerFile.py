x=int(input("Enter the value of x:"))
# xis a variable to match.
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _ if x!=80:
        print(x)
    case _ if x!=90:
        print(x)
    #case _:
      #  print(x)