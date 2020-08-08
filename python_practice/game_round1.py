def game():
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 199
    my_final_hp = my_hp - your_power
    your_final_hp = your_hp - my_power

    if my_final_hp > your_final_hp:
        print("I Won.")
    else:
        print("You win")

game()