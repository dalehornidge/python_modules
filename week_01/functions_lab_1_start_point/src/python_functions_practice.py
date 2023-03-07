# Dale attempts below. Solutions here:
# def return_10():
#     return 10

# def add(num_1, num_2):
#     return num_1 + num_2

# def subtract(num_1, num_2):
#     return num_1 - num_2

# def multiply(num_1, num_2):
#     return num_1 * num_2

# def divide(num_1, num_2):
#     return num_1 // num_2

# def length_of_string(string):
#     return len(string)

# def join_string(string_1, string_2):
#     return string_1 + string_2

# def add_string_as_number(string_1, string_2):
#     return int(string_1) + int(string_2)

# def number_to_full_month_name(month_number):
#     if month_number == 1:
#         return "January"
#     elif month_number == 3:
#         return "March"
#     elif month_number == 4:
#         return "April"
#     elif month_number == 9:
#         return "September"
#     elif month_number == 10:
#         return "October"

# def number_to_short_month_name(month_number):
#     short_month_name = number_to_full_month_name(month_number)[0:3]
#     return short_month_name

# def volume_of_cube(length_of_side):
#     return length_of_side ** 3

# def string_reverse(str):
#     string_reversed = ''
#     index = len(str)
#     while index > 0:
#         string_reversed += str[ index - 1 ]
#         index = index - 1
#     return string_reversed

# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * (5.0/9.0)
#     return round(celsius, 2)


def return_10():
    return 10

def add(number_1, number_2):
    combine_number = 0
    combine_number = number_1 + number_2
    return combine_number

def subtract(number_1, number_2):
    subtract_number = 0
    subtract_number = number_1 - number_2
    return subtract_number

def multiply(number_1, number_2):
    multi = 0
    multi = number_1 * number_2
    return multi

def divide(number_1, number_2):
    div = 0
    div = number_1 / number_2
    return div

def length_of_string(string):
    length = 0
    length = len(string)
    return length

def join_string(word_1, word_2):
    joint = word_1 + word_2
    return joint


def add_string_as_number(string_1, string_2):
    string_to_int_1 = int(string_1)
    string_to_int_2 = int(string_2)
    return string_to_int_1 + string_to_int_2

# correct answer
def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

# not working
# def number_to_full_month_name(number: 1;12):
#     month_number = (number, )
#     return month_number


# def number_to_full_month_name(list):
#     month_number = (list) == "January"
#     return month_number

# def number_to_full_month_name(int):
#     Jan_1 = (1)
#     return "January"
# works but seems too simple?

# def number_to_full_month_name_1(number):
#     jan_1 = number == 1
#     return "January"



def number_to_full_month_name(months):
    months_of_the_year = ["blank", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months_of_the_year[months]

def number_to_short_month_name(months):
    short_months_of_the_year = ["blank", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    return short_months_of_the_year[months]

def length_input(int):
    volume = int ** 3
    return volume