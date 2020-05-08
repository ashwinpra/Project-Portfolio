
import math

def ramanujanPi(upperlimit):
    s=0
    for i in range(upperlimit):
        s+=((math.factorial(4*i))*(1103+26390*i))/(((math.factorial(i))**4)*396**(4*i))

    coeff=(math.sqrt(8))/9801
    oneOverpi=coeff*s
    return oneOverpi**-1

def zeta2givesPi(upperlimit):
    s = 0
    for i in range(1,upperlimit+1):
        s+=1/(i**2)
    return math.sqrt(6*s)


print("This is a program(that nobody asked for!) that approximates pi using certain functions in Mathematics\n")

print("This program uses both the Riemann-Zeta function and Ramanujan's approximation of Pi\n")

print("------------------------------------------------------------------------------------------------\n")

lim=int(input("Enter an upper limit for evaluation (Larger the value, more the accuracy, but more the time)\n"))

print("According to the Riemann-Zeta Function, pi= " ,zeta2givesPi(lim))

print("According to Ramanujan, pi= ",ramanujanPi(lim))
