# Collatz Conjecture!

def reachesOne(num):
    while num>1:
        if num%2==0:
            num=num/2
        else:
            num=(3*num+1)
    if num == 1.0:
        return True
    else:
        return False


count=0
num=[]
test=int(input("Upper limit for test?"))
for i in range(1,test):
    if  not reachesOne(i):
        count+=1
        num.append(i)
if count>0:
    print("The Collatz Conjecture is disproven!")
    print(i+"do(es) not follow Collatz Conjecture")
else:
    print("Collatz is a genius")
