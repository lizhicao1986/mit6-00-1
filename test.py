

def alpha(string):
    ## string is lower case characters
    runCount = longestRun = 1
    beginIndex = 0
    index = 0
    tempString = ''
    found = False
    longestString = string[0]
    
    previousChar = string[0] # keep track of previous character
    
    for char in string: # check each character
        if char >= previousChar: # in order
            found = True # found one
            runCount += 1
            tempString = tempString + char # add to tempString
            
            if len(tempString) > len(longestString):
                longestString = tempString
            if runCount > longestRun:
                longestRun = runCount
        else:
            found = False
            runCount = 0 # reset runCount
            tempString = char # reset temp string
            
      #  print "Previous char: %s" %previousChar,
      #  print "Current char: %s" %char, 
      #  print "In order" if found else "Not in order",
     #   print "Longest string: %s" %longestString 
        previousChar = char # update pervious char

    
    return longestString
                 
        
s = 'azcbobobegghakl'
s2 = 'abcbcd'

print "Longest substring in alphabetical order is:  " + alpha(s)
print "Longest substring in alphabetical order is:  " + alpha(s2)

