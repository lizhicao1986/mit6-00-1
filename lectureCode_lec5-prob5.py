def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = 1
    
    if (a >= b):
        trial = b
    else:
        trial = a
        
    for index in range(1, trial+1):
            if b%index == 0 and a%index == 0: # found divisor
                if index > gcd:
                    gcd = index
    # Your code here
    return gcd
    
print gcdIter(17, 12)