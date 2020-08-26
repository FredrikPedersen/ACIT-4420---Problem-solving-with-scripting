import re


def task2():
    """
    Convenience function to trigger all functions in task 2
    """
    print()
    print("Counting words in file...")
    file_content = open("python.txt", "r+").read()
    stripped = strip_special_character(file_content)
    word_count_dict = find_word_occurrences(stripped)
    print_word_count(word_count_dict)
    print("...Done!")


def strip_special_character(content: str) -> str:
    """
    Iterate through a string using a regex to remove special characters except for spaces

    :param content: The string content to be iterated through
    :return: A new string stripped of non-alphanumerical characters, excluding spaces.
    """

    only_words = " "
    for character in content:
        only_words += (re.sub(r"[^a-zA-Z0-9]+", ' ', character))

    return only_words


def find_word_occurrences(content: str) -> dict:
    """
    Iterates through a string to find the number of occurrences of each unique word in it

    :param content: The string content to be iterated through
    :return: A dictionary with each unique word as a key and number of occurrences as values
    """
    all_words = content.split(" ")
    word_count = {}

    for word in all_words:
        count_words(word, word_count)

    return word_count


def count_words(word: str, word_count: dict):
    """
    Checks whether a word already exists in a dictionary.
    It is added with a value of 1 if it does not exist.
    it's value is incremented by 1 if it does.

    :param word: word to be checked versus the dictionary
    :param word_count: dictionary with the word counts
    """

    # Do not count spaces
    if word == "":
        return

    if word in word_count:
        word_count[word] += 1
    else:
        word_count.update({word: 1})


def print_word_count(occurrences: dict):
    """
    Print all keys in the word count dictionary with a value larger than 3

    :param occurrences: Dictionary with word occurrences
    """

    for key in occurrences:
        if occurrences[key] > 3:
            print("Frequency of " + key + ": " + str(occurrences[key]))