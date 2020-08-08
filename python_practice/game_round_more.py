import random
def game():
    my_hp = 1000
    my_power = random.randint(0,200)
    your_hp = 1000
    your_power = random.randint(0,200)
    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        if my_hp <=0:
            print("You Won.", my_hp, your_hp)
            break
        elif your_hp <= 0:
            print("I win", my_hp, your_hp)
            break

game()