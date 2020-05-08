#A very simple python function to test values of the Riemann Zeta Function(Z(s)) for different values of s
def summation(limit,s):
    result=0
    for i in range(1,limit+1):
        result+=1/(s**i)
    return result

print("The Riemann Zeta function is defined by Z(s)= summation of n from 1 to infinity of (1/n)^s\n")
print("Here, although the sum can't be done till infinity, we can define an upper limit for the summation\n")
print("------------------------------------------------------------------------------------------------\n")
n=int(input("Enter upper limit of summation\n"))
zeta=int(input("Enter s\n"))

print(summation(n,zeta))
