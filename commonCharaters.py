from collections import Counter

def commonCharacterCount(s1, s2):

    comunes = Counter(s1) & Counter(s2)
    return(sum(comunes.values()))
