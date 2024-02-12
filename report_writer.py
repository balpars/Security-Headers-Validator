def red(string):
    """
    Takes string and returns the string in red.
    """
    return "\033[91m" + string + "\033[0m"


def green(string):
    """
    Takes string and returns the string in green.
    """
    return "\033[92m" + string + "\033[0m"


def yellow(string):
    """
    Takes a string and returns the string  in yellow.
    """
    return "\033[93m" + string + "\033[0m"


def write_report(data_list):
    """
    Takes a list of data objects and prints them
    """
    print("-" * 50)
    for data in data_list:
        print(data)
        print("-" * 50)  # Add a separator between each data entry
