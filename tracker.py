# NAME = HIMANSHU SAINI 
# ROLL N0. = 2501010201
# DATE = 23.10.2025 
# PROJECT = ALORIEC TRACKING CANAOLE APP



print("..........WELCOME..........")
print("Calorie Tracking Console App\n")

Meal_list = []
Cal_list = []

# Fixed 5 meal inputs
for i in range(1, 6):
    meal = input(f"Enter meal {i}: ")
    Meal_list.append(meal)
    cal = int(input(f"Enter calories for {meal}: "))
    Cal_list.append(cal)

Total = sum(Cal_list)
Avg_cal = Total / 5

if Avg_cal >= 600:
    print("\n___ WARNING ___")
    print("You are crossing the limit of average calories.\n")
else:
    print("\n___ SUCCESS ___")
    print("You are in the limit of average calories.\n")

print("Meal Name\tCalories")
print("----------------------------")
for i in range(5):
    print(Meal_list[i], "\t", Cal_list[i])

print("----------------------------")
print("Total:\t\t", Total)
print("Average:\t", Avg_cal)

