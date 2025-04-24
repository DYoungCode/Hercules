# determine num of upper, lower, digits, special characters
# create function to determine how complex it is
# create function to calcualte number of years to break based on x type of pc
# run it against a breached database checker if possible

import math

print("Hercules will evaluate your password strength.")
password = input("Please enter a password: ")

length = len(password)
print("Length of string: ", length)

def char_count(password):
    
    char_counts = {
        "lowercase": 0,
        "uppercase": 0,
        "number": 0,
        "special": 0
    }

    for char in password:
        if char.islower():
            char_counts["lowercase"] += 1
        elif char.isupper():
            char_counts["uppercase"] += 1
        elif char.isdigit():
            char_counts["number"] += 1
        else:
            char_counts["special"] += 1
    
    return char_counts

# Make formating nicer
types_of_chars = char_count(password)
print(types_of_chars)

# Calculate strength of password based on:
# 26 special chars, 52 alpha, 10 numeric

def password_complexity(length):
    total = 0
    
    # returns number of bits
    # pwd entroy formula per mindpointgroup  log(C) / log(2) * L
    # Gemini formula E = log2(R^L) 
    for value in types_of_chars.values():
        if value > 0:
            #total = math.log(96) / math.log(2) + length
            total = math.log2(94**length)
        
    return total

bits = password_complexity(length)

def time_to_crack(bits):
    pwd_combinations = 0
    attempts_per_second = 300000000000 # Assumming 4090 at 300B pwd attempts per minute (see Hashcat stats)

    print('Bits', bits)
    if bits > 0:
        pwd_combinations = 2**int(bits)
    else:
        print("Not enough bits")
    
    time = int(pwd_combinations / attempts_per_second)

    if time > 0: #seconds in a year
        years = int(time / 31536000)
        remainder = time % 31536000
        print(remainder)
        
        days = int(remainder / 86400)
        remainder = time % 86400
        print(remainder)

        print(years, days)

        hours = int(remainder / 3600)
        remainder = time % 3600
        print(remainder)

        minutes = int(remainder / 60)
        seconds = minutes % 60
        print(remainder)

        print(years, "Years,", days, "Days,", hours, "Hours,", minutes, "Minutes,", seconds, "Seconds")

time_to_crack(bits)

