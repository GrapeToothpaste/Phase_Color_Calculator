from time import sleep
#Circuit Phase Color Calculator
print("Welcome to the 3 Phase Color Calculator")
number = int(input("Enter a Number: "))
phase = number % 6
if phase in (1, 2):
    print("Black/Brown")
elif phase in (3, 4):
    print("Red/Orange")
elif phase in (5, 0):
    print("Blue/Yellow")
sleep(5)
