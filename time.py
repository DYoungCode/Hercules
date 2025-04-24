time = 440213453

if time > 31536000: #seconds in a year
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
    seconds= time % 60
    print(remainder)

    print(years, "Years,", days, "Days,", hours, "Hours,", minutes, "Minutes,", seconds, "Seconds")
