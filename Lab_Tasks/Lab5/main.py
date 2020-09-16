import re
from typing import List


def find_standard_emails(file_content: str) -> List[str]:
    """
    Specifically matches words that starts with an s, followed by 6 or 7 digits and then @oslomet.no.
    """
    return re.findall("s\d{6,7}@oslomet.no", file_content)


def find_all_emails(file_content: str) -> List[str]:
    """
    Mathces any non-whitespace character an unlimited amount of times before and after an @.
    """
    return re.findall("\S+@\S+", file_content)


def find_last_activity(file_content: str) -> List[str]:
    """
    Matches phrases starting with one or two digits followed by a space, three instances of any alphabetic character,
    a space, one or two digits, a colon and finally two digits.
    """
    return re.findall("\d{1,2} [A-Za-z]{3} at \d{1,2}:\d{2}", file_content)


def find_sys_ids(file_content: str) -> List[str]:
    """
    Mathces phrases starting with fs: followed by three digits, another colon and then six or seven digits.
    """
    return re.findall("fs:\d{3}:\d{6,7}", file_content)


def find_activity_times(file_content: str) -> List[str]:
    """
    x, y, z = digits.
    Matches a new line where there is text on the format xx:yy:zz. The ":zz"-part is optional.
    """
    return re.findall("\n(\d{2}:\d{2}(?::\d{2})?)", file_content)


def find_names(file_content: str) -> List[str]:
    """
    Matches phrases starting with alphabetical characters repeated one or more time, followed by alphabetical characters
    or hyphens repeated one or more times.

    Only includes matches followed by a a tab indentation and a student mail, this to prevent random words to get
    included, and for names to not appear multiple times.
    """
    return re.findall("[A-ZÆØÅa-zæøå]+[A-ZÆØÅa-zæøå -]+(?=\ts\d{6,7})", file_content)


def find_activity_over_10_hours(file_content: str) -> List[str]:
    """
    Statement is getting rather complex, so split into three parts:
    find_name: Same regex as described in find_names
    skip_four_lines: passes through four new lines in the document.
    find_over_10_hours: matches with a string on the format yx:xx:xx where y > 1 and 0 <= x < 9

    The combined regex matches with a student's name, then tries to match with a string where the value is more than
    ten hours four lines up, and then excludes the four lines and the line containing the activity values from the
    match.
    """

    find_name = "[A-ZÆØÅa-zæøå]+[A-ZÆØÅa-zæøå -]+(?=\ts\d{6,7})"
    skip_four_lines = "(?:.*\n){4}"
    find_over_10_hours = "[1-9]\d{1}:\d{2}:\d{2}"

    return re.findall(find_name + "(?=" + skip_four_lines + find_over_10_hours + ")", file_content)


def find_users_last_login_august(file_content: str) -> List[str]:
    """
        Statement is getting rather complex, so split into three parts:
        find_name: Same regex as described in find_names
        skip_three_lines: passes through three new lines in the document.
        last_login_august: matches with a string on the format "xx Aug" where 0 <= x < 9

        The combined regex matches with a student's name, then tries to match with a string where there is two digits
        followed by the word "Aug" three lines up, and then excludes the three lines and the line containing the last
        login value from the match.
        """

    find_name = "[A-ZÆØÅa-zæøå]+[A-ZÆØÅa-zæøå -]+(?=\ts\d{6,7})"
    skip_three_lines = "(?:.*\n){3}"
    last_login_august = "\d{2} Aug"

    return re.findall(find_name + "(?=" + skip_three_lines + last_login_august + ")", file_content)


fileData = open("canvas.txt", "r+").read()
print(find_standard_emails(fileData))
print(find_all_emails(fileData))
print(find_last_activity(fileData))
print(find_sys_ids(fileData))
print(find_activity_times(fileData))
print(find_names(fileData))
print(find_activity_over_10_hours(fileData))
print(find_users_last_login_august(fileData))