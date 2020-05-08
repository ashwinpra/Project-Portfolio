import random
import time
count=0
check=0
a = ' 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9'
print("Tic Tac Toe!")
t = True
print(a)
while t:

    print("Where do you want to place the X? [1-9]")
    b = input()
    check=int(b)
    a=a.replace(b,'X')


    if 'X | X | X' in a:
        print(a)
        print("Congrats fam!!")
        print("Play again? [y/n]")
        if input()=='y':
            t=True
        else:
            t=False
    try:
        i=str(random.randint(0,9))
        a=a.replace(i, 'O')
        print("Computer's turn...")
        time.sleep(1)

    except Exception as i:
        if i == b:
            i=str(random.randint(0,9))


    print(a)







