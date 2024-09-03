lista = [3,2,4,6,7,2,1,2,1,1,36,8,3,5,1]

def find_mode(lista): #O(n)
    counts = {}
    for i in lista:
        counts.setdefault(i, 0)
        counts[i] += 1

    max_count = 0
    mode = None
    for k, v in counts.items():
        if v > max_count:
            max_count = v
            mode = k
    return mode

print(find_mode(lista)) # 1