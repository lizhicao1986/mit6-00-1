def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif (exp%2 == 0): # even
        return recurPowerNew(base*base, exp/2)
    else: # odd
        return base * recurPowerNew(base, exp-1)
        
print recurPowerNew(2, 8)