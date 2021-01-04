import math
def isPrime(n):
    k=int(math.sqrt(n))
    while(True):
        if k==1:
            print("\n",n,"is Prime")
            break
        elif n%k==0:
            print("\n",n,"is not Prime")
            break
        else:
            k-=1
    print("\n done")
def main():
    n=int(input("enter a number to check primality: "))
    isPrime(n)


if __name__=="__main__":
    main()
