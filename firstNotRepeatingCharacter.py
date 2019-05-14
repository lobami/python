def firstNotRepeatingCharacter(s):
    cadena = []
    diccionario = {}
    for i in s:
      if i in diccionario:
        diccionario[i] += 1
      else:
        diccionario[i] = 1 
        cadena.append(i)
    for i in  cadena:
      if diccionario[i] == 1:
        return i
    return None