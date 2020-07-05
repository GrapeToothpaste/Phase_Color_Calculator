from time import sleep
#Circuit Phase Color Calculator
print("Welcome to the 2 Phase Color Calculator")
number = int(input("Enter a Number: "))
phase = number % 4
if phase in (1, 2):
    print("Black")
elif phase in (3, 0):
    print("Red")
sleep(5)
