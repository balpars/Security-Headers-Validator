def write_report(data_list, desc_str, color):
    """
    Takes a list of data objects and prints them with specified color
    """
    if len(data_list) == 0:
        return

    color_function = None
    if color == 'red':
        color_function = red
    elif color == 'green':
        color_function = green
    elif color == 'yellow':
        color_function = yellow

    if color_function is None:
        print("Invalid color specified.")
        return

    print(color_function(desc_str))
    print()
    for data in data_list:
        print(color_function(data.__str__()))
        print()
    print("-" * 50)


def write_report_short(data_list, desc_str, color):
    """
    Takes a list of data objects and prints their title with specified color
    """
    if len(data_list) == 0:
        return
    color_function = None
    if color == 'red':
        color_function = red
    elif color == 'green':
        color_function = green
    elif color == 'yellow':
        color_function = yellow

    if color_function is None:
        print("Invalid color specified.")
        return

    print(color_function(desc_str))
    print()

    for data in data_list:
        print(color_function(data.get_title()))
    print("-" * 50)


def green(string):
    return "\033[92m" + string + "\033[0m"


def red(string):
    return "\033[91m" + string + "\033[0m"


def yellow(string):
    return "\033[93m" + string + "\033[0m"
