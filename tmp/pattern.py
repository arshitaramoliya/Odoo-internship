def printstar1():
    n=6
    for i in range (n):
        for j in range (n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print ("*",end=" ")
            else:
                print(" ",end=" ")
        print()

def printstar2():
    n=6
    for i in range (n):
        for j in range (n):
            if j>=i:
                print("*",end="")
            else:
                print(" ",end="")
        print()

def printstar3():
    n=6
    for i in range (n):
        for j in range (n):
            if i+j >= (n-1):
                print("*",end="")
            else:
                print(" ",end="")
        print()

printstar1()
print()
printstar2()
print()
printstar3()