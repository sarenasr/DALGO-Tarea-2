word_1 = "animal"
word_2 = "manila"

def check_anagram(word_1, word_2):#O(n)
    if len(word_1) != len(word_2):
        return False
    hash_table_1 = {}
    for i in word_1:
        hash_table_1.setdefault(i, 0)
        hash_table_1[i] += 1
    
    hash_table_2 = {}
    for i in word_2:
        hash_table_2.setdefault(i, 0)
        hash_table_2[i] += 1
    
    for k, v in hash_table_1.items():
        if k not in hash_table_2 or v != hash_table_2[k]:
            return False
    return True
print(check_anagram(word_1, word_2)) # True