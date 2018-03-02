from math import floor


def is_leap_year(year):
    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:
        return False
    else:
        return True


def is_gregorian_date(year, month, date):
    if year > 1752:
        return True

    #if year <1752, not gregorian
    elif year < 1752:
        return False

    #need to check month and day
    elif year == 1752:
        if month > 9:
            return True
        elif month < 9:
            return False
        elif month == 9:
            if date >= 14:
                return True
            else:
                return False



def is_valid_date(year, month, date):
    #invalid date
    if not is_gregorian_date(year, month, date):
        return False

    #invalid month
    elif (month < 1) or (12 < month):
        return False

    #invalid day for february
    elif month == 2:
        if is_leap_year(year):
            return (1 <= date) and (date <= 29)
        else:
            return (1 <= date) and (date <= 28)

    #for 31 day months
    elif (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        return (1 <= date) and (date <= 31)

    #for 30 day months
    else:
        return (1 <= date) and (date <= 30)


def weekday_of(year, month, date):
    century = int(str(year)[:2])
    year1 = int(str(year)[2:])

    if (month == 1) or (month == 2):
        year -= 1
        century = int(str(year)[:2])
        year1 = int(str(year)[2:])
        month += 12
        weekday = ((date + ((13 * (month + 1)) // 5) + year1 + (year1 // 4) + (century // 4) + (5 * century)) % 7)
        return weekday
    else:
        weekday = ((date + ((13 * (month + 1)) // 5) + year1 + (year1 // 4) + (century // 4) + (5 * century)) % 7)
        return weekday

def weekday_name(weekday):
    if weekday == 0:
        return "Saturday"
    elif weekday == 1:
        return "Sunday"
    elif weekday == 2:
        return "Monday"
    elif weekday == 3:
        return "Tuesday"
    elif weekday == 4:
        return "Wednesday"
    elif weekday == 5:
        return "Thursday"
    else:
        return "Friday"



def main():
    birthday = input("Enter your birthday in YYYY-MM-DD format: \n")

    #finding locations to divide up the date
    hyphen1 = birthday.find("-")
    hyphen2 = birthday[hyphen1+1:].find("-") + hyphen1 +1

    #breaking the input apart into year, month, and date
    year = int(birthday[:hyphen1])
    month = int(birthday[hyphen1 + 1:hyphen2])
    date = int(birthday[hyphen2 + 1:])

    #validity of date
    if not is_valid_date(year, month, date):
        return "The date you entered is invalid."
    else:
        return ("You were born on a " + weekday_name(weekday_of(year, month, date)) + "!")


if __name__ == '__main__':
    print(main())