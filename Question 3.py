def sample(n):
    if(n==1):
        return n
    return n * sample(n-1)
    
print(sample(int(input("Enter The Number"))))