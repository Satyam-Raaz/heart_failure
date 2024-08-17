class StringFormatter:
    @staticmethod
    def reverse_string(s):
        s=str(input("enter string"))
        n=len(s)
        ans=""
        j=n-1
        while j>=0:
            ans+=s[j]
            j-=1

        return ans        
s=str
print(StringFormatter.reverse_string(s))            

    
