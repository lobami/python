def allLongestStrings(inputArray):
    var = 0
    for i in range(0,len(inputArray)):
        var = max(var,len(inputArray[i]))
    
    return [i for i in inputArray if len(i)==var]
