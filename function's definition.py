import math

#print hello

def print_hello():
    '''Print Hello at screen.'''
    print("Hello")

def get_hello():
    '''
    Return Hello string.

    :return: Returns string value
    '''
    return "Hello"

'''
Ask user name and print question with it.

If name is Thanos print another text.
'''
def ask_name_and_greet_user():
    name = input("Insert your name please: ")
    name = name.capitalize()
    if name == "Thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else :
        print("Hi, " + str(name) + ". Would you like to have a Hamburger?")

def calculate_hypotenuse_length(a: int, b: int):
    '''
    Calculate the length of hypotenuse.

    :param a: Integer value
    :param b: Integer value
    :return: Float value - calculated length
    '''
    c = math.sqrt(a ** 2 + b ** 2)
    return c

result = calculate_hypotenuse_length(3, 4)
#print(result)

def calculate_cathetus_length(b: int, c: int):
    '''
    Calculate the length of cathetus.

    :param b: Integer value
    :param c: Integer value
    :return: Float value - calculated length
    '''
    a = math.sqrt(c ** 2 - b ** 2)
    return a

result_2 = calculate_cathetus_length(4, 5)
#print(result_2)

#print_hello()
#greeting = get_hello()
#print(greeting)
#ask_name_and_greet_user()
