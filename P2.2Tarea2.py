lista = [3,5,2,1,6,7,8,4,9]

def find_median(lista): #O(n log(n))
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        return (lista[n//2 - 1] + lista[n//2]) / 2
    else:
        return lista[n//2]
print(find_median(lista)) 