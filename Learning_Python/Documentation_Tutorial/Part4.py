# If statements
x = 3

if x < 0:
    x = 0
    print("Negative changed to zero!")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

# For loops

words = ["Hello", "There", "General", "Kenobi"]

for word in words:
    print(word, len(word))

for i in range(len(words)):
    print(i, words[i])

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, '*', n // x)
            break
    else:
        # No breaks occured, the for-loop's else statement is triggered
        print(n, 'is a prime number')

for n in range(2, 10):
    if n % 2 == 0:
        # print("Found an even number: ", n)
        continue
    print("Found a number: ", n)


# Functions

def fib(number):
    a, b = 0, 1
    while a < number:
        print(a, end=" ")
        a, b = b, a + b
    print()


# Functions may also have default/optional arguments.
def optional_args(number, message="Hello There"):
    if message == "Hello There" :
        print(number)
    else:
        print(message)


optional_args(3)
optional_args(3, "Nope")


# May use * and / to mark arguments as keyword and positional arguments
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# Invalid calls:
# combined_example(1, 2, 3)
# combined_example(pos_only = 1, standard=2, kwd_only=3)

# Valid calls:
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)

