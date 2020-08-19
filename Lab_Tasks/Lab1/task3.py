# Task 3

def calculate_average(amount_of_numbers: int) -> str:
    if amount_of_numbers == 0:
        return "You need to specify an amount of numbers!"

    total_sum = 0

    for x in range(amount_of_numbers):
        total_sum += int(input("What is the " + str(x+1) + ". number? "))

    return "The average of your numbers is: " + str(round(total_sum/amount_of_numbers, 2))


amount_input = int(input("How many numbers do you have? "))
print(calculate_average(amount_input))
