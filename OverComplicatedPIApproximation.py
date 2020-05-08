import math
s=0
k=int(input("Accuracy? (Larger the input, greater the accuracy) \n"))
for i in range(1,k+1):
    s=s+1/(i**2)

print(math.sqrt(6*s))