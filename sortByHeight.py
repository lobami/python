def sortByHeight(a):
    b = sorted([
        i for i in a 
        if i!=-1])
    j = 0
    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            a[i]=b[j]
            j+=1
    return a

