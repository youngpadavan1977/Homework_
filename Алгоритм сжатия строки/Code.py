a = input()
b = ""
word = ""
for c, d in enumerate(a):
    if a[c] == a[c-1] and c > 0:
        b = b + d
    elif c == 0:
        b = d     
    else:
      word = word + b[0] + str(len(b))  
      b = d
    if c + 1 == len(a):
        word = word + b[0] + str(len(b))

print(word)    
