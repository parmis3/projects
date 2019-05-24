secret = 7

while True:
    answer = input("Enter Number:")
    answer = int(answer)
    if answer < secret:
        print("secret is greater than your number")
    elif answer > secret:
        print("secret is lesser than your number")
    else:
        print("Bingo!")
