s1={'a','b','c'}
s2={'c','e','f','c'}

for i in s1:
    if i not in s2:
        print(i)
for i in s2:
    if i not in s1:
        print(i)
    
    
