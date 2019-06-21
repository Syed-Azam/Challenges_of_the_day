from random import randint
r = randint(1, 10)
print("Guess the Number Game")
print("---------------------")
print("I have a number in mind from 1 to 10")
t = ["First", "Second", "Last"]
for c in range(3):
    n = int(input(t[c]+" Guess [1/10] : "))
    if n == r:
        print("We Have a Winner!!!!")
        print("Yes! It was :", r)
        quit()
    elif n > r and c < 2:
        print("Try Again with a Smaller Number")
    elif n < r and c < 2:
        print("Try Again with a Larger Number")
print("We Have a Looser!!!!")
print("The Correct Number was : ", r)