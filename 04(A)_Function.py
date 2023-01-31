

#factorial

def Fact(number):
        res=1
        while(number>=1):
            res=res*number
            number-=1
        return res
            

print("Factorial for numberv1 to 10 are : ")
print("\n================================\n")
for i in range(10):
    f=Fact(i+1)
    print(f"{i+1} ! = {f}")

print("\n================================")


"""
Output1:

Factorial for numberv1 to 10 are : 

================================

1 ! = 1
2 ! = 2
3 ! = 6
4 ! = 24
5 ! = 120
6 ! = 720
7 ! = 5040
8 ! = 40320
9 ! = 362880
10 ! = 3628800

================================

"""