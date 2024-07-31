import random
from Data import data
import Art

#print(Art.logo)

score=0

while True:
    A=random.choice(data)
    name_a=A["name"]
    f_count_a=A["follower_count"]
    description_a=A["description"]
    country_a=A["country"]
    print(f"Compare A: {name_a}, {description_a}, from {country_a}")


    #print(Art.vs)

    B=random.choice(data)
    name_b=B["name"]
    f_count_b=B["follower_count"]
    description_b=B["description"]
    country_b=B["country"]
    print(f"Compare B: {name_b}, {description_b}, from {country_b}")



    question=input("Who has more followers? Type 'A' or 'B' : ").upper()
    if question=='A':
        if f_count_a>f_count_b:
            score+=1
        else:
            print(score)
            print("Better luck next time")
            break

    elif question=='B':
        if f_count_b>f_count_a:
            score+=1
        else:
            print(score)
            print("good try")
            break
    else:
        print("Invalid Input")
        break


