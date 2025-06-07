Birth_day = input("Birth day: ")
current_year = int(input("Current year: "))
print("----------------------")
year = int(Birth_day[:4])
print(f"Birth_year: {Birth_day[:4]}")
print(f"Birth moon: {Birth_day[5:7]}")
print(f"Birth Day: {Birth_day[8:]}")
print(f"Age: {current_year - year}")

  
