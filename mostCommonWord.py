#   Most Common Word
#   Amazon Interview Question

def mostCommonWord(paragraph, banned):
    normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
    words = normalized_str.split()
    hash_banned = set(banned)
    hash_para = dict()

    for i in range(len(words)):
        if words[i] not in hash_para and words[i] not in hash_banned:
            hash_para[words[i]] = 1
        if words[i] in hash_para:
            hash_para[words[i]] += 1
        else:
            pass

    key_list = list(hash_para.keys()) 
    val_list = list(hash_para.values()) 

    return key_list[val_list.index(max(val_list))]

# paragraph = "a, a, a, a, b,b,b,c, c"
# banned = ["a"]
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph, banned))
