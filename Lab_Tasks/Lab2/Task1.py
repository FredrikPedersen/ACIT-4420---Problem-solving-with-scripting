monday, tuesday, wednesday, thursday, friday, saturday, sunday = ([None] * 22 for i in range(7))
days = {"Monday": monday, "Tuesday": tuesday, "Wednesday": wednesday, "Thursday": thursday, "Friday": friday,
        "Saturday": saturday, "Sunday": sunday}


def menu():

    user_choice = input("s - Add appointment\nl - List a schedule\nx - Exit\nWhat do you want to do? ")

    if user_choice == "s" or user_choice == "l":
        get_input(user_choice)
    elif user_choice == "x":
        exit()
    else:
        print("No valid choice was made, exiting program...")
        exit()

    menu()


def get_input(user_choice: str):

    chosen_day = input("What day? ")

    if user_choice == "s":
        chosen_time = int(input("What time? "))
        appointment = input("What is your appointment? ")
        save_appointment(chosen_day, chosen_time, appointment)

    if user_choice == "l":
        print_schedule(chosen_day)


def save_appointment(chosen_day: str, chosen_time: int, appointment: str):
    schedule = (days[chosen_day])
    schedule[chosen_time] = appointment

    print("Your schedule for that day now looks like this: ")
    print_schedule(chosen_day)


def print_schedule(chosen_day: str):

    schedule = days[chosen_day]
    output = ""

    for x in range(len(schedule)):
        output += format_number_string(x)
        output += format_appointment_value(schedule, x)

        output += "\n"

    print(output)


def format_number_string(number: int) -> str:
    formatted = ""

    if number < 10:
        formatted += "0" + str(number)
    else:
        formatted += str(number)

    formatted += ":00 "
    return formatted


def format_appointment_value(schedule: list, index: int) -> str:
    formatted = " "

    if schedule[index] is not None:
        formatted += str(schedule[index])

    return formatted
