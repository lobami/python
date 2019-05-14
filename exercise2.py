def adjacentElementsProduct(inputArray):
    code = inputArray[1]
    product = code * inputArray[0]
    for i in inputArray[0::]:
        if(code * i > product):
            product = code * i
        
        code = i
    else:
        return product