import math

'''Practice different math expressions and calculations.'''

# Declare num_a and num_b

num_a = 9
num_b = 4

a = 15
b = 20
c = 25

# 1. Sum and difference

sum = num_a + num_b
print(f"{num_a} + {num_b} = {sum}")

difference = num_a - num_b
print(f"{num_a} - {num_b} = {difference}")

print("--------------------------------------")

# 2. Float division

division = num_a / num_b
print(f"{num_a} / {num_b} = {division}")

print("--------------------------------------")

# 3. Integer division

division = num_a // num_b
print(f"{num_a} // {num_b} = {division}")

print("--------------------------------------")

# 4. Powerful operations

multiply_numbers = num_a * num_b
power = num_a ** num_b
reminder = num_a % num_b

print(multiply_numbers)
print(power)
print(reminder)

print("--------------------------------------")

# 5. Find average

average = (num_a + num_b) / 2
print(average)

print("--------------------------------------")

# 6. Area of a circle

radius = 5

circle_area = 2 * math.pi * radius

circle_area_final = round(circle_area, 2)

print(circle_area_final)

print("--------------------------------------")

# 7. Area of an equilateral triangle

side_length = 9

triangle_area = round(math.sqrt(3) / 4 * side_length ** 2)

print(triangle_area)

print("--------------------------------------")

# 8. Calculate discriminant

discriminant = b ** 2 - 4 * a * c

print(discriminant)

print("--------------------------------------")

# 9. Calculate hypotenuse length

c_hypotenus = math.sqrt(a ** 2 + b ** 2)

print(c_hypotenus)

print("--------------------------------------")

# 10. Calculate cathetus length

b_cathetus = math.sqrt(c ** 2 - a ** 2)

print(b_cathetus)

print("--------------------------------------")

#11. Time converter

seconds = 745901

minutes = seconds // 60

print(minutes)

hours = minutes // 60

print(hours)

print("--------------------------------------")

# 12. Student helper

angle = 57

sine = round(math.sin(angle), 1)
cosine = round(math.cos(angle), 1)

print(sine)
print(cosine)

print("--------------------------------------")

# 13. Greetings

n = 3

lots_of_heys = n * "Hey"
print(lots_of_heys)

print("--------------------------------------")

# 14. Adding numbers

string_numbers = str(num_a) + str(num_b)
print(string_numbers)

















