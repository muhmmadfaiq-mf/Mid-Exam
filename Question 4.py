# ch = input("Enter a character: ")

# if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
#  or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
#     print(ch, "is a Vowel")
# else:
#     print(ch, "is a Consonant")

def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = input("Enter the Word")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

