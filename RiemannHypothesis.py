
n = float(input("Enter n for summation: "))
k=int(input("Range of accuracy?"))
s=0
for i in range(1,k+1):
    s=s+1/(i**n)

print(s)