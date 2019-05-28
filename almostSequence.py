def check_increasing(seq):
    for i in range(len(seq)-1):
        if seq[i] >= seq[i+1]:
            return i
    return -1

def almostIncreasingSequence(sequence):
    check = check_increasing(sequence)
    if check == -1:
        return True
    if check_increasing(sequence[check-1:check] + sequence[check+1:]) == -1 or check_increasing(sequence[check:check+1] + sequence[check+2:]) == -1:
        return True
    
    return False