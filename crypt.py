def isCryptSolution(crypt, solution):
    m={}
    for x in solution:
        m[x[0]] = int(x[1])
    r=[]
    for x in crypt:
        r.append(0)
        for y in x:
            r[-1]=r[-1]*10+m[y]
    if r[0]+r[1]==r[2]:
        if len(r[0]) == len(crypt[0]):
            if len(r[1]) == len(crypt[1]):
                if len(r[2]) == len(crypt[2]):
                    return 1
    return 0
            
    
