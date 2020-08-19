# Task 1 & 2

def cookies(name, number_of_cookies):
    default_message = "Hello " + name + "!\n"

    if 0 < number_of_cookies < 10:
        print(default_message + "Are you sure that is enough cookies?")
    elif 9 < number_of_cookies < 20:
        print(default_message + "I agree, cookies are delicious!")
    elif 19 < number_of_cookies < 51:
        print(default_message + "Be careful, that's a lot of cookies!")
    elif number_of_cookies > 50:
        print(default_message + "No way, that is waaaaay too many! You get 50 cookies.")
        number_of_cookies = 50
    else:
        print(default_message + "Something must be wrong, I give you 10 cookies!")
        number_of_cookies = 10

    print("Here are your cookies: " + "cookie " * number_of_cookies)


name_input = input("What is your name? \n")
cookies_input = int(input("How many cookies do you want? \n"))
cookies(name_input, cookies_input)
