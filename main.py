import puppy
import check_input


def main():
    print("Congratulation on your new puppy")
    pup = puppy.Puppy()
    choice = 0
    while choice != 3:
        print("What would you like to do?")
        print("1. Feed the puppy")
        print("2. Play with the puppy")
        print("3. Quit")
        choice = check_input.get_int_range("enter choice: ", 1, 3)
        if choice == 1:
            print(pup.give_food())

        elif choice == 2:
            print(pup.throw_ball())


main()
