def ran():
    lower_lim=int(input("enter lower end of range "))
    upper_lim=int(input("enter upper end of range "))
    number=int(input("enter a number to check in the range "))
    if number in range(lower_lim,upper_lim):
            print(str(number) +" is in the  range:" +str(lower_lim)+"-"+str(upper_lim))
    else:
            print(str(number) +" is not in the range:" +str(lower_lim)+"-"+str(upper_lim))

ran()
