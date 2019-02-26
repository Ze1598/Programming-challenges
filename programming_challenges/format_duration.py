# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

'''
Write a function which formats a duration, given as a number of seconds, in a human-friendly way.
The function must accept a non-negative integer. If it is zero, it just returns "now". 
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds:
    format_duration(62)    # returns "1 minute and 2 seconds"
    format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

Here, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of units of the format a positive integer and one of the valid 
units of time, separated by a space. The unit of time is used in plural if the integer is 
greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which 
is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 
"1 second and 1 year" is not correct, but "1 year and 1 second" is.

Different components have different unit of times. So there is not repeated units like in 
"5 seconds and 1 second".

A component will not appear at all if its value happens to be zero. Hence, "1 minute and 
0 seconds" is not valid, it should be just "1 minute".

A unit of time must be used as much as possible. It means that the function should not 
return "61 seconds", but "1 minute and 1 second" instead. Formally, the duration 
specified by a component must not be greater than any valid more significant unit of time.
'''

def format_duration(seconds):
    # If the argument is zero, immediately return 'now'
    if seconds == 0:
        return 'now'
    
    # If the argument is bigger than zero, define the time units
    conversions = {'second': 1, 'minute': 60, 'hour':3600, 'day':86400, 'year':31536000}
    # Dictionary to hold the value of each time unit, relative to the passed argument
    used = {'years':0, 'days':0, 'hours':0, 'minutes':0, 'seconds':0}
    # A list to hold the used time components of the formatted string
    string = []

    # Try to convert seconds to years
    if seconds >= conversions['year']:
        # Calculate how many years are contained in the seconds
        used['years'] += int(seconds/conversions['year'])
        # Then subtract the number of seconds used for the conversion
        seconds = seconds%conversions['year']
        if used['years'] > 1:
            string.append('{} years'.format(used['years']))
        else:
            string.append('1 year')

    # Try to convert seconds to days
    if seconds >= conversions['day']:
        used['days'] += int(seconds/conversions['day'])
        # Then subtract the number of seconds used for the conversion
        seconds = seconds%conversions['day']
        if used['days'] > 1:
            string.append('{} days'.format(used['days']))
        else:
            string.append('1 day')

    # Try to convert seconds to hours
    if seconds >= conversions['hour']:
        used['hours'] += int(seconds/conversions['hour'])
        # Then subtract the number of seconds used for the conversion
        seconds = seconds%conversions['hour']
        if used['hours'] > 1:
            string.append('{} hours'.format(used['hours']))
        else:
            string.append('1 hour')

    # Try to convert seconds to minutes
    if seconds >= conversions['minute']:
        used['minutes'] += int(seconds/conversions['minute'])
        # Then subtract the number of seconds used for the conversion
        seconds = seconds%conversions['minute']
        if used['minutes'] > 1:
            string.append('{} minutes'.format(used['minutes']))
        else:
            string.append('1 minute')

    # If there are any seconds remaining, simply treat them as seconds
    if seconds > 0:
        used['seconds'] += seconds
        if used['seconds'] > 1:
            string.append('{} seconds'.format(used['seconds']))
        else:
            string.append('1 second')

    # Now create and return the properly formatted string
    if len(string) > 2:
        return ", ".join(string[0:-1]) + ' and {}'.format(string[-1])
    elif len(string) > 1:
        return " and ".join(string)
    else:
        return string[0]
        
        

print(format_duration(1))
print()
print(format_duration(62))
print()
print(format_duration(120))
print()
print(format_duration(3600))
print()
print(format_duration(3662))