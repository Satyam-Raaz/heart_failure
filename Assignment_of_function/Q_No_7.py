def is_palindromic(n):
    number_str=str(n)
    if number_str==number_str[::-1]:
        return True
    else:
        return False


def generate_Palindrome(n):
    for i in range(1,n+1):
        if is_palindromic(i):
            yield i

number=int(input("enter number"))
gen=generate_Palindrome(number)
for num in gen:
    print(num)


