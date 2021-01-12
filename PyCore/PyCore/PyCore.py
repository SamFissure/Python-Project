import math
import random

def getScale():
    while(True):
        CorF=int(input("\nenter 1 for Celcius to Farenheit, 2 for Farenheit to Celcius: "))
        if(CorF==1 or CorF == 2):
            return CorF
        else:
            print("error input: ")


def getChoice():
    while(True):
        #basic interface for numbers
        choice=int(input ("\nenter 1 for primality check, 2 for Temperature Conversion and 3 for lotto numbers: "))
        if(choice==1):
            return choice
        elif (choice>0 and choice <3):
            CorF=getScale()
            if (CorF==1):
                return 2
            else:
                return 4
                

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





def isTemp(n,CorF):
    #F = (tc * 9/5) + 32 Farenheit from Celcius
    #C = (tf − 32) * 5/9 Celcius from Farenheit
    if (CorF==1):
        return ((n-32)*5/9)
    else:
        return ((n*9/5)+32) 



def main():
    choice=0
    CorF=0
    while(True):
        choice = getChoice()
        n=getInput()

        if(choice==1):
            isPrime(n)
        elif(choice==2):
            k=isTemp(n, 1)
            print("Temperature in chosen scale is ", k)
        elif(choice==4):
            k=isTemp(n,2)
            print("Temperature in chosen scale is ", k)
        else:
            print("error input")
if __name__=="__main__":
    main()



class SDlotto:
    #a Lottery number picker that socially distances its values.
    #Constants for ball range
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