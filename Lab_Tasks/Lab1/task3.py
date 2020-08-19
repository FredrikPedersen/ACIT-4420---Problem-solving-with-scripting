# Task 3

def calculate_average(amount_of_numbers=0):
    if amount_of_numbers == 0:
        print("You need to specify an amount of numbers!")
        return

    total_sum = 0

    for x in range(amount_of_numbers):
        total_sum += int(input("What is the " + str(x+1) + ". number? "))

    print("The average of your numbers is: " + str(round(total_sum/amount_of_numbers, 2)))


amount_input = int(input("How many numbers do you have? "))
calculate_average(amount_input)
