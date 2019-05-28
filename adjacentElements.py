def adjacentElementsProduct(inputArray):
    length = len(inputArray) 
     
    operacion = []
     
    for i in range(length-1):
        
        operacion.append(inputArray[i] * inputArray[i+1])
        
    return max(operacion)