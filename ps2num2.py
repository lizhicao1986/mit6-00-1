balance = 3926
annualInterestRate = 0.2

lowestPayment = balance / 12
highestPayment = (balance * (1 + (annualInterestRate/12)**12))/12.0

done = False;

while (not done):  
    
    monthlyPayment = (lowestPayment + highestPayment)/2 # start guess in middle
    
    test_balance = balance # reset balance
    for month in range(1,13):
        unpaidBalance = test_balance - monthlyPayment
        test_balance = unpaidBalance + ((annualInterestRate/12) * unpaidBalance)
        
        if (abs(test_balance) < 0.01):
            done = True
            break
    
    if test_balance > 0: # monthly payment too low
        lowestPayment = monthlyPayment
    elif test_balance < 0: # monthly payment too high
        highestPayment = monthlyPayment
    
print "Payment: %d" %monthlyPayment
