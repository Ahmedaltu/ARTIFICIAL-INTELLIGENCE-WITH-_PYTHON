def main():

    while True:
        a = input("Write something (quit ends): ")

        if a == "quit":
            break
        else:

            tester(a)


def tester(str, givenstring="Too Short"):
    if len(givenstring) > len(str):

        print(givenstring)

    else:
        print(str)


if __name__ == "__main__":
    main()
