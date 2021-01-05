import math
import random



def getChoice():
    while(True):
        #basic interface for numbers
        choice=input("\nenter 1 for primality check, 2 for Temperature Conversion and 3 for lotto numbers: ")
        if(choice==1):
            return choice
        elif (choice>0 and choice <3):
            CorF=int(input("\nenter 1 for Celcius, 2 for Farenheit: "))
            if(choice>1 and choice <3):
                return choice, CorF
        elif(choice==3):
            return choice
        else:
            print("\nerror input")


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

def getInput():
    n=int(input("\nenter a number: "))
    return n



class SDlotto:
    #a Lottery number picker that socially distances its values.
    #Constants
    LOW=1
    HIGH_PB=69
    HIGH_MEGA=70
    PB_REDBALL=26
    MEG_YELLOWBALL=25
    #need to track selections and valid ranges....  Perhaps a list?
    #OK solution is a list with boundaries for each pick.  
    #The only reqirement is that the odd number index be the low end of exclusion and the even number index be high.
    #It can be in any order.

    #whitePB = random.randint(LOW,HIGH_PB)
    #whiteMeg = random.randint(LOW,HIGH_MEGA)
    #powBall = random.randint(LOW,PB_REDBALL)
    #megBall = random.randint(LOW,MEG_YELLOWBALL)

def isTemp(n,CorF):
    #F = (tc * 9/5) + 32 Farenheit from Celcius
    #C = (tf − 32) * 5/9 Celcius from Farenheit
    if (CorF):
        celc=(n-32)*5/9
        return celc
    else:
        faren = (n*9/5)+32 
        return faren



def main():
    choice=0
    CorF=0
    while(True):
        choice, CorF = getChoice()
        n=getInput()

        if(choice==1):
            isPrime(n)
        elif(choice==2):
            n=isTemp(n, CorF)
            print("Temperature in chosen scale is ", n)
        else:
            print"error input"
if __name__=="__main__":
    main()

