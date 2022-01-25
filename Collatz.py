# simple program demonstrating any collatz sequence.
def collatz (number):
        while number != 1:
            if number % 2 == 0:
                number = number / 2
            else:
                number = (3 * number) + 1
            print(int(number))
print ("Witness the Collatz Sequence, enter any number here and eventually the sequence will arrive at 1!")
while True:
    print ("Enter your number")
    try:
        collatz(int(input()))
    except ValueError:
        print("Please enter a number!")
        continue

