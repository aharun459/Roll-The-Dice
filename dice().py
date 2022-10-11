def main():
    import random
    roll_the_dice = input("Roll the dice:Press Enter")
    first_dice = random.randint(0,6)
    second_dice = random.randint(0,6)
    print(first_dice , second_dice)

    if first_dice == 1 and second_dice == 1:
        print("Snake Eyes")
    restart_dice = input("Reroll: Type yes")
    if restart_dice == "yes":
        main()
main()