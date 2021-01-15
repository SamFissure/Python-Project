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
        

        if(choice==1):
            n=getInput()
            isPrime(n)
        elif(choice==2):
            n=getInput()
            k=isTemp(n, 1)
            print("Temperature in chosen scale is ", k)
        elif(choice==4):
            n=getInput()
            k=isTemp(n,2)
            print("Temperature in chosen scale is ", k)
        else:
            print("error input: ")
            lottoPrint()
            choose= random.randint(1, 69)
            addToChosen(choose)
            addToDistance(choose)
            print("picked numbers ", Chosen)
            for i in range (4):
                checkSocialDistance()
                print("picked numbers ", Chosen)
            print("Powerball", random.randint(1,26))




    #a Lottery number picker that socially distances its values.
    #Constants for ball range
    
Chosen = []
Distance = []

def lottoPrint():
    print("lottery number chooser")
def addToChosen(n):
    Chosen.append(n)

def addToDistance(n):
    Distance.append(n-7)
    Distance.append(n+6)

def checkSocialDistance():
    isNotDone=True
    while (isNotDone==True):
        choose= random.randint(1,69)
        print("random int", choose)
        print("list size", len(Distance))
        print("list", Distance)
        i=0
        isInLoop=True
        while(isInLoop):
            if ((Distance[i]<=choose) and (choose<=Distance[i+1])):
                isInLoop=False
            elif(i==(len(Distance)-2)):
                addToChosen(choose)
                addToDistance(choose)
                isNotDone=False
                isInLoop=False
            else:
                i+=2


    return
        
    #def listload(n):

    #need to track selections and valid ranges....  Perhaps a list?
    #OK solution is a list with boundaries for each pick.  
    #The only reqirement is that the odd number index be the low end of exclusion and the even number index be high.
    #It can be in any order.

    #whitePB = random.randint(LOW,HIGH_PB)
    #whiteMeg = random.randint(LOW,HIGH_MEGA)
    #powBall = random.randint(LOW,PB_REDBALL)
    #megBall = random.randint(LOW,MEG_YELLOWBALL)
if __name__=="__main__":
    main()
