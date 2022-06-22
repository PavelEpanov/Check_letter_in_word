def main():

    tracker = 0

    name = input("Введите предложение: ")

    for letter in name:
        if letter == "Т" or letter == "т":
            tracker += 1
    print(tracker)

main()
