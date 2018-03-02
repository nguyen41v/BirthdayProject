from math import floor


def is_leap_year(year):
    """Determines whether a year is a leap year.

    Leap years were "invented" to account for how the time for earth's orbit
    around the sun does not divide even into the time for earth's rotation.
    Details on leap years can be found at:

    https://en.wikipedia.org/wiki/Leap_year#Algorithm

    Args:
        year (int): The year.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Examples:

        >>> print(is_leap_year(1995))
        False

        >>> print(is_leap_year(1996))
        True

        >>> print(is_leap_year(2000))
        True

        >>> print(is_leap_year(2100))
        False

    """
    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:
        return False
    else:
        return True


def is_gregorian_date(year, month, date):
    """Determines whether a date is after the start of the Gregorian calendar.

    The Gregorian calendar was instituted by Pope Gregory XIII to make the
    seasons appear on the same dates every year, forever. The US adopted the
    Gregorian calendar on September 14, 1752.

    You can read about the Gregorian calendar on Wikipedia, or watch this 20-
    minute video by Vsauce:

    https://www.youtube.com/watch?v=IJhgZBn-LHg

    Args:
        year (int): The year.
        month (int): The month.
        date (int): The date.

    Returns:
        bool: True if the date is on or after September 14, 1752. False
            otherwise.

    Examples:

        >>> print(is_gregorian_date(0, 0, 0))
        False

        >>> print(is_gregorian_date(1752, 9, 13))
        False

        >>> print(is_gregorian_date(1752, 9, 14))
        True

        >>> print(is_gregorian_date(1753, 1, 1))
        True

        >>> print(is_gregorian_date(2016, 2, 3))
        True

    """

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
    """Determines whether a date is valid.

    For our purposes, a "valid" date means:

    * it is a Gregorian date
    * the month is between 1 and 12, inclusive
    * the date is appropriate for the month, taking leap years into account

    Args:
        year (int): The year.
        month (int): The month.
        date (int): The date.

    Returns:
        bool: True if the date meets the above criteria, False otherwise.

    Examples:

        >>> print(is_valid_date(1752, 9, 13))
        False

        >>> print(is_valid_date(1752, 9, 14))
        True

        >>> print(is_valid_date(2016, 2, 3))
        True

        >>> print(is_valid_date(2015, 2, 29))
        False

        >>> print(is_valid_date(2016, 2, 29))
        True

    """
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
    """Calculate the day of the week of a date.

    This function uses Zeller's congruence to calculate the weekday. Assumes
    that the date is valid. See documentation and Wikipedia for details:

    https://en.wikipedia.org/wiki/Zeller's_congruence

    Args:
        year (int): The year.
        month (int): The month.
        date (int): The date.

    Returns:
        int: The integer corresponding to the day of the week. 0 is Saturday,
            1 is Monday, etc.

    Examples:

        >>> print(weekday_of(1752, 9, 14))
        5

        >>> print(weekday_of(1887, 4, 20))
        4

        >>> print(weekday_of(2000, 2, 3))
        5

        >>> print(weekday_of(2001, 9, 11))
        3

        >>> print(weekday_of(2016, 2, 3))
        4

    """
    century = int(str(year)[:2])
    year1 = int(str(year)[2:])

    #jan/feb conversion for Zeller's equation
    if (month == 1) or (month == 2):
        year -= 1
        century = int(str(year)[:2])
        year1 = int(str(year)[2:])
        month += 12
        weekday = ((date + floor((13 * (month + 1)) / 5) + year1 + floor(year1 / 4) + floor(century / 4) + (5 * century)) % 7)
        return weekday
    else:
        weekday = ((date + floor((13 * (month + 1)) / 5) + year1 + floor(year1 / 4) + floor(century / 4) + (5 * century)) % 7)
        return weekday


def weekday_name(weekday):
    """Convert the weekday integer to its name.

    This function takes the output of weekday_of and turns it into the days of
    the week we are familiar with.

    Args:
        weekday (int): The day of the week, as an integer.

    Returns:
        String: The day of the week, as a string.

    Examples:

        >>> print(weekday_name(0))
        Saturday

        >>> print(weekday_name(1))
        Sunday

        >>> print(weekday_name(6))
        Friday

    """
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
    """The main entry point for this program.

    This program should ask the user for their birthday, then check if the date
    is valid. If it is, the program should print the day of the week of the
    user's birthday. Otherwise, tell the user that their date is invalid.

    Example run 1:

        Enter your birthday in YYYY-MM-DD format: 1887-04-20
        You were born on a Wednesday!

    Example run 2:

        Enter your birthday in YYYY-MM-DD format: 1961-08-04
        You were born on a Friday!

    Example run 3:

        Enter your birthday in YYYY-MM-DD format: 1215-06-15
        The date you entered is invalid.

    Example run 4:

        Enter your birthday in YYYY-MM-DD format: 2013-17-42
        The date you entered is invalid.

    """
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
        return "You were born on a " + weekday_name(weekday_of(year, month, date)) + "!"


if __name__ == '__main__':
    print(main())