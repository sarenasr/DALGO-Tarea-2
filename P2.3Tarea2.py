set_n = {1,2,3}
set_m = {6,4,3}

def check_disjunction_c(set_n, set_m): #O(n)
    for i in set_n:
        if i in set_m:
            return False
    return True

def check_disjunction_b(set_n, set_m): #(O(m log(m) + n log(m))
    ordered_set_m = sorted(set_m)
    for i in set_n:
        if binary_search(ordered_set_m, i) != -1:
            return False
    return True

def check_disjunction_a(set_n, set_m): #(O(n log(n) + m log(n))
    ordered_set_n = sorted(set_n)
    for i in set_m:
        if binary_search(ordered_set_n, i) != -1:
            return False
    return True

def binary_search(lista, value):
    low = 0
    high = len(lista) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if lista[mid] < value:
            low = mid + 1
        elif lista[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1

print(check_disjunction_c(set_n, set_m)) 
print(check_disjunction_b(set_n, set_m)) 
print(check_disjunction_a(set_n, set_m)) 