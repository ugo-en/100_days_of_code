import math

"""
The aim of tyhis program is to convert integers to roman numerals
"""

# contains the basic integers and their roman numeral equivalents
romans = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}

def get_units(number):
    """
    Converts a single unit to roman numeral
    """
    result = ""
    try:
        if 10 > number > 0:
            if number in romans.keys():
                result = romans[number]
            elif number < 4:
                result = romans[1]*number
            elif number == 4:
                result = "IV"
            elif 5 > number < 9:
                result = f"{romans[5]}{romans[1]*(number%5)}"
            elif number == 9:
                result = "IX"
    except Exception as ex:
        print(ex)
    return result

def get_tens(number):
    """
    Converts a multiple of 10 to roman numerals
    """
    result = ""
    try:
        if number % 10 == 0 and 100 > number >= 10:
            if number in romans.keys():
                result = romans[number]
            elif number < 40:
                result = romans[10]*(number/10)
            elif number == 40:
                result = "XL"
            elif 50 > number < 90:
                result = f"{romans[50]}{romans[10]*(number%50)}"
            elif number == 90:
                result = "XC"
    except Exception as ex:
        print(ex)
    return result 


def get_hundreds(number):
    """
    Converts a multiple of 100 to roman numerals
    """
    result = ""
    try:
        if number % 100 == 0 and 1000 > number >= 100:
            if number in romans.keys():
                result = romans[number]
            elif number < 400:
                result = romans[100]*int(number/100)
            elif number == 400:
                result = "CD"
            elif 900 > number > 500:
                result = f"{romans[500]}{romans[100]*int((number-500)/100)}"
            elif number == 900:
                result = "CM"
    except Exception as ex:
        print(ex)
    return result 


def get_thousands(number):
    """
    Converts a multiple of 1000 to roman numerals
    """
    result = ""
    try:
        if number % 1000 == 0 and 3000 > number >= 1000:
            result = f"{romans[1000]*int(number/1000)}"
    except Exception as ex:
        print(ex)
    return result 

# welcome user
print("WELCOME TO THIS SIMPLE APP THAT CONVERTS INTEGERS TO ROMAN NUMERALS")

# make it repeat continuously
while True:
    # the final result
    result = 0

    # get the integer from the user. No Decimals!!! NO Strings!!!
    number = 0
    while number == 0:
        try:
            number = int(input("Enter a number you want to convert to roman numerals: "))

            if number >= 4000:
                print("Sorry, we can only process numbers less than 4000")
                raise Exception
        except:
            number = 0
    
    # solve for basic numbers
    if number in romans.keys():
        result = romans[number]
    # for numbers not  in the dictionary
    else:
        # string representaion of the number
        num_str = str(number)

        # every number is comprised of thousand, hundred, tens and units
        thousands = 0
        hundreds = 0
        tens = 0
        units = 0

        if number < 10:
            units = number

        elif len(num_str) == 2:
            # any two digit number is comprised of a multiple of 10, and a unit
            tens = int(num_str[0])*10
            units = int(num_str[1])

        elif len(num_str) == 3:
            # any three digit number is comprised of a multiple of 100, 10, and a unit
            hundreds = int(num_str[0])*100
            tens = int(num_str[1])*10
            units = int(num_str[2])

        elif len(num_str) == 4:
            # any four digit number is comprised of a multiple of 1000, 100, 10, and a unit
            thousands = int(num_str[0])*1000
            hundreds = int(num_str[1])*100
            tens = int(num_str[2])*10
            units = int(num_str[3])
        
        # convert each part to their roman string
        thousands = get_thousands(thousands)
        hundreds = get_hundreds(hundreds)
        tens = get_tens(tens)
        units = get_units(units)

        # combine them
        result = f"{thousands}{hundreds}{tens}{units}"

    # show the result
    print(f"{number} in roman numerals is {result}")

    # ask for permission to proceed
    proceed = input("Do you want to proceed? ('y','n'):").lower().strip()
    if proceed != "y":
        break

# print Goodbye message
print("Goodbye!")







