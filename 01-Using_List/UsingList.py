def main():
    MyList = []

    while True:
        choice = input(
            "Would you like to \n(1)Add or \n(2)Remove items or \n(3)Quit?: ")

        if choice == "1":
            AddItem(MyList)

        elif choice == "2":
            RemoveItem(MyList)

        elif choice == "3":
            PrintList(MyList)
            break

        else:
            print("Incorrect selection.")


def AddItem(list):

    addedItem = input("What will be added?: ")

    list.append(addedItem)


def RemoveItem(list):

    print("There are", len(list), "items in the list.")
    removedItemIndex = input("Which item is deleted?: ")

    if int(removedItemIndex) >= len(list) or int(removedItemIndex) < 0:
        print("Incorrect selection.")

    else:
        list.remove(list[int(removedItemIndex)])


def PrintList(list):
    print("The following items remain in the list:")
    [print(item) for item in list]


if __name__ == "__main__":
    main()
