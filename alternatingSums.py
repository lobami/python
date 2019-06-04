def alternatingSums(number):
    v1 = sum(number[0::2])
    v2 = sum(number[1::2])
    return [v1, v2]