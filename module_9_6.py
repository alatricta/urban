def all_variants(text):
    for len_substr in range(1, len(text)+1):
        start_sub = 0
        while start_sub+len_substr <= len(text):
            yield text[start_sub:start_sub+len_substr]
        
            start_sub += 1
  
def all_variants2(text):
    len_substr = 1
    start_sub = 0
    while len_substr < len(text)+1:
        yield text[start_sub:start_sub+len_substr]
        if start_sub+len_substr >= len(text):
            start_sub = 0
            len_substr += 1 
        else:
            start_sub += 1 
    
    
a = all_variants("abcdf")
for i in a:
    print(i)

print('='*10)
b = all_variants2("abcdf")
for i in b:
    print(i)
    