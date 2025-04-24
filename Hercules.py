# Hercules calculates how "strong" your password.  It calculates the time it would take for a modern PC
# with a 4090 GPU running Hashcat to break a password.  Based on current data (April 2025), 300B password hashes 
# can be checked per second

# Still to do:
# can you connect it to breached password databases to tell use if password is insecure

import math

print("Hercules will evaluate the strength of your password.")
password = input("Please enter a password: ")

length = len(password)
print("Length of password: ", length, "\n")

def char_count(password):
    
    char_counts = {
        "Lowercase": 0,
        "Uppercase": 0,
        "Digit": 0,
        "Special": 0
    }

    for char in password:
        if char.islower():
            char_counts["Lowercase"] += 1
        elif char.isupper():
            char_counts["Uppercase"] += 1
        elif char.isdigit():
            char_counts["Digit"] += 1
        else:
            char_counts["Special"] += 1
    
    return char_counts

# Make formating nicer
types_of_chars = char_count(password)
print("Password contains the following number of character types: ")
for key, value in types_of_chars.items():
    print(f"{key}: {value}")
#print(types_of_chars)

# Calculate strength of password based on 94 lower, upper, digit and special characters
# function returns number of bits
def password_complexity(length):
    total = 0
    

    # Password entropy formula E = log2(R^L) 
    for value in types_of_chars.values():
        if value > 0:
            total = math.log2(94**length)
        
    return total

def time_to_crack(bits):
    pwd_combinations = 0
    attempts_per_second = 300000000000 # Assumming 4090 at 300B pwd attempts per minute (see Hashcat stats)
    seconds_in_year = 31536000
    seconds_in_day = 86400
    seconds_in_hour = 3600

    #print('Bits: ', bits)
    if bits > 0:
        pwd_combinations = 2**int(bits)
    
    #calculate total # of seconds to break given x number of password combinations
    time = (pwd_combinations / attempts_per_second)

    #convert total seconds(time) into years, days, hours, minutes, seconds
    if time > 0: #seconds in a year

        years = int(time / seconds_in_year)
        remainder = time % seconds_in_year
        
        days = int(remainder / seconds_in_day)
        remainder = time % seconds_in_day

        hours = int(remainder / seconds_in_hour)
        remainder = time % seconds_in_hour

        minutes = int(remainder / 60)
        seconds = minutes % 60

        print("\nTime required to crack password:", years, "Years,", days, "Days,", hours, "Hours,", minutes, "Minutes,", seconds, "Seconds")

def strength(bits):
    if bits < 44:
        print("Password is completely insecure. Password can be cracked instantly.")
    elif bits < 46:
        print("Password is completely insecure. Password can be cracked under 2 minutes.")
    elif bits < 53 :
        print("Password is very insecure. Password can be cracked in under 5 hours.")
    elif bits < 59:
        print("Weak password. Password can be cracked in 11 days or less.")
    elif bits < 65:
        print("Password is ok, not great. Password can be cracked in about 3 years with a current computers")
    elif bits < 73:
        print("Strong Password! Password can be cracked in the next 500 years with a current computers")
    else:
        print("Excellent password! A modern PC would take over 30,000 years to crack this password!")

bits = password_complexity(length)
time_to_crack(bits)
strength(bits)

