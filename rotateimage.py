def rotateImage(valor):

    valor = list(zip(*valor))    
    valor = [list(l[::-1]) for l in valor]
    
    return valor
