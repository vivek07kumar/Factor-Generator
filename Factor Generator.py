done = True
print()
print('             >>>>>>>>>>>>>>>>> Factor Generator <<<<<<<<<<<<<<<<<')
print()
print()
while done :
    done2 = True
    print()
    userinput = eval(input('>> Please enter a number to know its Factor(s) : '))
    print()
    if userinput > 0 and type(userinput) != float:
        print('-------------------------------------------------------------------------')
        print()
        print('>> Factor(s) of',userinput,':  ',end='')
    else :
        print('                               >> Wrong Input ! <<')
        print()
        print('> Please enter a number Greater than 0.')
        print('> Float number are not accepted.')
    for factor in range(1,userinput + 1,1) :
        remainder = userinput % factor
        if remainder == 0 :
            if factor > 1 :
                print(',',end='')
            print(factor,end='')
    if userinput > 0 and type(userinput) != float :
        print()
        print()
        print('-------------------------------------------------------------------------')
    while done2 :
        print()
        choice = input('>> Press C to Continue or Press E to Exit : ')
        if choice == 'c' or choice == 'C' :
            done2 = False
        elif choice == 'e' or choice == 'E' :
            done2 = False
            done = False
            print()
        else :
            print()
            print('                               >> Wrong Input ! <<')
