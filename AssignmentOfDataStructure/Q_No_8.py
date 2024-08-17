s=input("enter string")
n=len(s)
ans=""
i=0
while(i<n):
    ascii=ord(s[i])
    if(ascii>=65 and ascii<=90):
        ascii=ascii+32
        ans=ans+chr(ascii)
        i=i+1
    elif(ascii>=97 and ascii<=122):
        ascii=ascii-32 
        ans=ans+chr(ascii)
        i=i+1
    

print(ans)
