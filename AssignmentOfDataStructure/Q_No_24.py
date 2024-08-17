s1={"cat","dog","eye"}
s2={"cat","dog"}

for i in s1:
    for j in s2:
        if i not in s2:
            print(i)
            break

