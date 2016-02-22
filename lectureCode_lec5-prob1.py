def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else
        result = base
        for pwr in range(1,exp):
            result = result * base
        return result


print iterPower(2,3)