balance = 999999
annualInterestRate = 0.18

lowestPayment = balance / 12.0
highestPayment = (balance * (1 + (annualInterestRate/12))**12)/12.0

done = False;

while (not done):  
    
    monthlyPayment = (lowestPayment + highestPayment)/2.0 # start guess in middle

    test_balance = balance # reset balance
    for month in range(1,13):
        unpaidBalance = test_balance - monthlyPayment
        test_balance = unpaidBalance + ((annualInterestRate/12) * unpaidBalance)
        
        if (abs(test_balance) < 0.01):
            done = True
            break 
    if test_balance > 0: # monthly payment too low
        lowestPayment = monthlyPayment
    else: # monthly payment too high
        highestPayment = monthlyPayment
    
print "Lowest Payment: %.2f" %monthlyPayment
