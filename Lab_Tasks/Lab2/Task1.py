monday, tuesday, wednesday, thursday, friday, saturday, sunday = ([None] * 22 for i in range(7))
days = {"Monday": monday, "Tuesday": tuesday, "Wednesday": wednesday, "Thursday": thursday, "Friday": friday,
        "Saturday": saturday, "Sunday": sunday}


def task1_menu():
    """
    Recursive function serving as an entry point for the user, allowing them to choose what program flow they
    wish to follow. Terminates at the user's request or if invalid input is detected.
    """

    user_choice = input("s - Add appointment\nl - List a schedule\nx - Continue to Task 2\nWhat do you want to do? ")

    if user_choice == "s" or user_choice == "l":
        get_input(user_choice)
    elif user_choice == "x":
        return
    else:
        print("No valid choice was made, continuing to Task 2...")
        return

    task1_menu()


def get_input(user_choice: str):
    """
    Gathers necessary input from the user, dependent on what program flow they have
    indicated they wish to follow.

    :param user_choice: The user's desired program flow
    """

    chosen_day = input("What day? ")

    if user_choice == "s":
        chosen_time = int(input("What time? "))
        appointment = input("What is your appointment? ")
        save_appointment(chosen_day, chosen_time, appointment)

    if user_choice == "l":
        print_schedule(chosen_day)


def save_appointment(chosen_day: str, chosen_time: int, appointment: str):
    """
    Finds the schedule corresponding to the user's chosen day from the days dictionary, then adds
    their appointment at the time indicated by the user.

    :param chosen_day: User defined value for what day's schedule should be updated
    :param chosen_time: User defined value for what time their appointment takes place
    :param appointment: User defined value representing their appointment
    """

    schedule = (days[chosen_day])
    schedule[chosen_time] = appointment

    print("Your schedule for that day now looks like this: ")
    print_schedule(chosen_day)


def print_schedule(chosen_day: str):
    """
    Prints the entire schedule for the chosen day

    :param chosen_day: User defined value for what day's schedule should be printed
    """

    schedule = days[chosen_day]
    output = ""

    for x in range(len(schedule)):
        output += format_number_string(x)
        output += str(schedule[x]) if schedule[x] is not None else " "

        output += "\n"

    print(output)


def format_number_string(number: int) -> str:
    """
    Adds leading and trailing zeroes to integers to return a HH:MM format string

    :param number: Number to be formatted
    :return: Argument number converted to a HH:MM format
    """

    formatted = ""

    if number < 10:
        formatted += "0" + str(number)
    else:
        formatted += str(number)

    formatted += ":00 "
    return formatted
