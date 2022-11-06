print("Hello, world!")


def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds


amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)


def month_days(month, days):
    print(month + " has " + days + " days.")


month_days("June",  str(30))
month_days("July",  str(31))


def area_rectangle(x, y):

    print("The area is " + str(x*y))


area_rectangle(5, 6)

# 1) Complete the function to return the result of the conversion


def convert_distance(miles):
    km = miles * 1.6
    return km


my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2.0*my_trip_km))


compare = "tang" > "small"
print(compare)

sum = 11 % 5
print(sum)


def format_name(first_name, last_name):
    # code goes here
    string = "Name: "
    if first_name != "" and last_name != "":
        string += last_name + ", " + first_name
    elif first_name != "" and last_name == "":
        string += first_name
    elif first_name == "" and last_name != "":
        string += last_name
    else:
        string = ""
    return string


print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should be "Name: Madonna"

print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"

print(format_name("", ""))
# Should be ""


def sum(x, y):
    return (x+y)


print(sum(sum(1, 2), sum(3, 4)))

((10 >= 5*2) and (10 <= 5*2))
