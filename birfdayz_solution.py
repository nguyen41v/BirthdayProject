# IS_LEAP_YEAR


def is_leap_year(year):
    if int(year % 4) > 0:
        return False
    elif int(year % 100) != 0:
        return True
    elif int(year % 400) == 0:
        return True
    else:
        return False


# IS_GREGORIAN_DATE


# Ada
def is_gregorian_date(year, month, date):
    if int(year) <= 1751:
        # before 1751 is false
        return False
    elif int(year) > 1752:
        # after 1752 is true
        return True
    elif int(year) == 1752 and int(month) > 9:
        # if year is 1752 and after September is true
        return True
    elif int(year) == 1752 and int(month) == 9 and int(date) >= 14:
        # if year is 1752 and its September, the day has to be on or after 14
        return True
    elif int(year) == 1752 and int(month) == 9 and int(date) < 14:
        # if year is 1752 and its September, and the day is before 14, return false
        return False
    else:
        return False


# Lani
def is_gregorian_date(year, month, date):
    if year < 1752:
        # if the year is before 1752 it can't be Gregorian
        return False
    elif year == 1752:
        # if the year is 1752, we have to consider the following options
        if month < 9:
            return False
        elif month == 9:
            # if the month is September, it MAY be Gregorian
            if date >= 14:
                # but only if the day is greater than or on the 14th
                return True
            return False
        elif month > 9:
            return True
        return False
    else:
        # The only option left is past the year 1752
        return True


# Honor
def is_gregorian_date(year, month, date):
    if year > 1752:
        return True
    elif year == 1752 and month > 9:
        return True
    elif year == 1752 and month == 9 and date >= 14:
        return True
    else:
        return False


# IS_VALID_DATE

# Robby
def is_valid_date(year, month, date):
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    if not is_gregorian_date(year, month, date):
        return False
    if not is_leap_year(year):
        if month == 2 and date > 28:
            return False
    elif is_leap_year(year):
        if month == 2 and date > 29:
            return False
    if month not in month_31 and date > 30:
        return False
    elif month in month_31 and date > 31:
        return False
    elif date == 0:
        return False
    else:
        return True


# Sherry
def is_valid_date(year, month, date):
    if is_gregorian_date(year, month, date) and (1 <= month <= 12):
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10
            or month == 12) and (1 <= date <= 31):
            return True
        if (month == 4 or month == 6 or month == 9 or month == 11) and (1 <= date <= 30):
            return True
        if month == 2 and (not is_leap_year(year)) and (1 <= date <= 28):
            return True
        elif is_leap_year(year) and (1 <= date <= 29):
            return True
        else:
            return False
    else:
        return False


# Justin
def is_valid_date(year, month, date):
    if not is_gregorian_date(year, month, date):
        return False
    if not 1 <= month <= 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= date <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= date <= 30
    elif is_leap_year(year):
        return 1 <= date <= 29
    else:
        return 1 <= date <= 28


# WEEKDAY_OF


# Maddie
def weekday_of(year, month, date):
    if month < 3:
        month = month + 12
        year = str(year - 1)
    else:
        year = str(year)
    century = int(year[0:2])
    year = int(year[2:])
    z = (date + year + (5 * century) + (floor(((13 * (month + 1)) / 5))) + (floor(year / 4)) + (floor(century / 4))) % 7
    return z


# Jacob M.
def weekday_of(year, month, date):
    if month == 1 or month == 2:
        month += 12
        year -= 1
    J = year // 100
    K = year % 100
    m = month
    q = date
    h = int((q + 26 * (m + 1) // 10 + K + (K // 4) + (J // 4) - (2 * J)) % 7)
    return h


# WEEKDAY_NAME


# Alyssa
def weekday_name(weekday):
    if weekday == 0:
        return 'Saturday'
    elif weekday == 1:
        return 'Sunday'
    elif weekday == 2:
        return 'Monday'
    elif weekday == 3:
        return 'Tuesday'
    elif weekday == 4:
        return 'Wednesday'
    elif weekday == 5:
        return 'Thursday'
    elif weekday == 6:
        return 'Friday'


# Emma
def weekday_name(weekday):
    day_names = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return day_names[weekday]


# MAIN


# Tori
def main():
    user_date = input("Enter your birthday in YYYY-MM-DD format:")
    year = int(user_date[0:4])
    month = int(user_date[5:7])
    date = int(user_date[8:])
    if is_valid_date(year, month, date):
        weekday = weekday_of(year, month, date)
        return "You were born on a " + str(weekday_name(weekday)) + "!"
    if not is_valid_date(year, month, date):
        return "The date you entered is invalid."


# Vanessa
def main():
    birthday = input("Enter your birthday in YYYY-MM-DD format: \n")

    #finding locations to divide up the date
    hyphen1 = birthday.find("-")
    hyphen2 = birthday[hyphen1 + 1:].find("-") + hyphen1 + 1

    #breaking the input apart into year, month, and date
    year = int(birthday[:hyphen1])
    month = int(birthday[hyphen1 + 1:hyphen2])
    date = int(birthday[hyphen2 + 1:])

    #validity of date
    if not is_valid_date(year, month, date):
        return "The date you entered is invalid."
    else:
        return "You were born on a " + weekday_name(weekday_of(year, month, date)) + "!"
