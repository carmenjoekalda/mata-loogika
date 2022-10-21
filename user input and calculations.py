# 1. Asking user's name, allowed speed and actual speed

name = input("Sisestage oma nimi: ")
allowed_speed = input("Sisestage lubatud kiirus (km/h): ")
actual_speed = input("Sisestage tegelik kiirus (km/h): ")

# 2. Calculate the fine

fine = (int(actual_speed) - int(allowed_speed)) * 3
final_fine = min(190, int(fine))

# 3. Print the result

print(str(name) + ", " + "kiiruse ületamise eest on teie trahv " + str(final_fine) + " eurot.")



