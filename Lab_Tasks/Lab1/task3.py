# Task 3

def calculate_average():
    amount = int(input("How many numbers do you have?\n"))
    total_sum = 0

    for x in range(amount):
        total_sum += int(input("What is the " + str(x+1) + ". number? "))

    print("The average of your numbers is: " + str(round(total_sum/amount, 2)))


calculate_average()