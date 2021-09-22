import random
import math

if __name__ == '__main__':

    ## RANDOM NUMBER
    start = 5   # min number
    end = 10    # max number
 
    n = 10      # size
 
    x = random.randint(start, end)
    # print(x)

    ## CALCULATE NUMBER OF CHANCES
    print("Vous avez", round(math.log(end - start + 1,2)), "chances de trouver le nombre")

    ## INITIALIZE NUMBER OF GUESS
    count = 0

    ## CALCULATE
    while count < math.log(end - start + 1,2):
        count +=1 

        ## INPUT GUESSING NUMBER
        print("Le nombre se situe entre 5 et 10")
        guessNumber = int(input("Trouve le nombre:- "))

        ## TESTING
        if x == guessNumber: 
            print("Bravo, vous avez trouver le nombre au(x)", count, "eme essai(s)")
            break
        elif x > guessNumber:
            print("Le nombre est plus grand !")
        elif x < guessNumber:
            print("Le nombre est plus petit")