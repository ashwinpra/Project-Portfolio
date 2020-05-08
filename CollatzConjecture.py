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

print("The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:\nstart with any positive integer n. Then each term is obtained from the previous term as follows:\nif the previous term is even, the next term is one half of the previous term.\nIf the previous term is odd, the next term is 3 times the previous term plus 1.\nThe conjecture is that no matter what value of n, the sequence will always reach 1.")
print("------------------------------------------------------------------------------------------------\n")

count=0
num=[]
test=int(input("How many numbers should be tested?\n"))
for i in range(1,test):
    if  not reachesOne(i):
        count+=1
        num.append(i)
if count>0:
    print("The Collatz Conjecture is disproven!")
    print(i+"disprove(s) the Conjecture!")
else:
    print("Collatz Conjecture holds true!")
