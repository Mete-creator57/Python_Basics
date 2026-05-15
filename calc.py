import sys
# Compound Interest Calculator
is_active = True
while is_active:
    start = input('Press anything to start: ')
    if start:
        pass
    
    print('NOTE: Provide only numerical values')
    principal = input('Enter the amount you started with (principal): ')
    if principal.lower() == 'q':
        principal = 0
        sys.exit()
    
    
    try:
        principal = float(principal)
    except ValueError:
        print("Invalid Input. Try again...")
        continue
    else:
        if principal < 0:
                print('Principal can not be less than 0!')
                continue
        else:
            pass

    while True: 
        inter_rate = input('Enter the interest rate: ')
        if inter_rate.lower() == 'q':
            inter_rate = 0
            raise SystemExit()
            
    
        try:
            inter_rate = int(inter_rate)
        except ValueError:
            print("Invalid Input. Try again...")
            continue
        else:
            try:
                 if inter_rate < 0:
                    raise Exception('Interest rate can not be less than 0!')
            except Exception as err:
                print(f'An Exception was raised: {err}')
                continue
            else:
                    break
         


    while True: 
        time = input('Enter the time in years: ')
        if time.lower() == 'q':
            time = 0
            sys.exit()

        try:
            time = int(time)
        except Exception as error:
            print('An exception happened: ' + error)
            continue
        else:
            if time < 0:
                print('Time can not be less than 0!', end=' ')
                print('Try again!')
                continue
            else:
                 break
    
    formula = principal * pow(1 + inter_rate / 100, time)
    print(f"Principal: {principal}")
    print("Interest rate: %d" % inter_rate)
    print('Years: ' + str(time))
    print('Result: ' + str(formula))


            
    
    

    

        