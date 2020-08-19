# Task 1 & 2

def cookies(name: str, number_of_cookies: int) -> str:
    message = "Hello " + name + "!\n"

    if 0 < number_of_cookies < 10:
        message += "Are you sure that is enough cookies?\n"
    elif 9 < number_of_cookies < 20:
        message += "I agree, cookies are delicious!\n"
    elif 19 < number_of_cookies < 51:
        message += "Be careful, that's a lot of cookies!\n"
    elif number_of_cookies > 50:
        message += "No way, that is waaaaay too many! You get 50 cookies.\n"
        number_of_cookies = 50
    else:
        message += "Something must be wrong, I give you 10 cookies!\n"
        number_of_cookies = 10

    message += "Here are your cookies: " + "cookie " * number_of_cookies
    return message


name_input = input("What is your name? \n")
cookies_input = int(input("How many cookies do you want? \n"))
print(cookies(name_input, cookies_input))
