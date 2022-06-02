def main():
    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    print("Supermarket\n===========")
    total = 0
    while True:
        choice = int(input("Please select product (1-10) 0 to Quit: "))
        if choice == 0:
            break
        else:
            print("Product: ", choice, " Price: ", prices[choice-1])
            total = total + prices[choice-1]
    print("Total: ", total)
    pay = int(input("Payment: "))
    print("Change: ", pay-total)


if __name__ == "__main__":
    main()
