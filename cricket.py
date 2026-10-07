import random
score = 0
while True:
    try:
        n = int(input("Choose 1/2/3/4/5/6 :"))
    except ValueError:
        print("Invalid !")
        continue
    print(f"You Choose {n}")
    comp = random.randint(1,6)
    print(f"Computer Choose {comp}")
    if n <1 or n > 6 :
        print("Invalid! Choose 1/2/3/4/5/6")

    elif n != comp:
        score = score + n 
        print(f" Your score is {score}")

    else :
        print("Out!")
        print(f"Score {score}") 
        break
    