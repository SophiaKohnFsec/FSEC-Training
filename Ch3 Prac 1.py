# Sophia Kohn
#Practice Assignmet "The Collatz Sequence"

number= 0

#Defining collatz function to test for odd/even number
def collatz(number):
    if number % 2==0:
        return (number // 2)

    else:
        return(number*3 +1)
    number= int(input("Enter a number:"))


#Setting a while loop to run until the function call equals 1.
while (collatz(number) != 1):
    number= int(input("Enter a number:"))
    print(collatz(number))

