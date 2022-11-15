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


def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)
        n += 1


print_range(1, 5)  # Should print 1 2 3 4 5
print("")

# Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.


def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            # If it's not, increment the factor by one
            factor += 1
    return "Done"


print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

print(" ")


def is_power_of_two(number):
    # Check if the number can be divided by two without a remainder
    while number % 2 == 0:
        if number <= 0:
            return False
        else:
            number = number / 2
            return True
        break
    # If after dividing by two the number is 1, it's a power of two
    if number == 1:
        return True

    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False

print(" ")


print("")

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " play against the " + away_team)

print("")

# The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.


def show_letters(word):
    for words in word:
        print(words)


show_letters("Hello")
# Should print one line per letter
for xx in range(10):
    for y in range(xx):
        print(y)
