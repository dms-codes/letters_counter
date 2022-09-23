words = "The little red fox jumped over a fence and bit a python"
res = {}
for letter in words.lower().replace(" ",""):
    if letter not in res:
        res[letter]=1
    else:
        res[letter]+=1
print(sorted(res.items(), key=lambda x: x[1], reverse=True)[:3])
    

