# https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/
# No more hiding from your alarm clock! You've decided you want your computer to keep you updated on the time so you're never late again. A talking clock takes a 24-hour time and translates it into words.
# Input Description
# An hour (0-23) followed by a colon followed by the minute (0-59).
# Output Description
# The time in words, using 12-hour format followed by am or pm.
# Sample Input data=> 00:00 '\n' 01:30 '\n' 12:05 '\n' 14:01 '\n' 20:29 '\n' 21:00
# Sample Output data=> '\n' It's twelve am '\n' It's one thirty am '\n' It's twelve oh five pm '\n' It's two oh one pm '\n' It's eight twenty nine pm '\n' It's nine pm

def TalkingClock(time):
#Define the hour and minutes
    hour = time[0:2]
    minute = time[3:]

#Create the string for output
    current_time = 'It\'s '
#List to contain the names of the hours
    hours = ['midnight', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
#The first part of the names of minutes
    tens = ['oh', 'twenty', 'thirty', 'forty', 'fifty']
#The name of the minutes between 11 and 19
    ten_fwd = ['','eleven', 'twelve', 'thirteen', 'forteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

#Hours    
#12-23
    if int(hour) > 12:
        current_time += hours[int(hour) - 12]
#Noon
    elif int(hour) == 12 and int(minute) == 0:
        current_time += 'noon'
#1-12
    else:
        current_time += hours[int(hour)]


#Minutes
    if int(minute) == 0:
        pass
    else:
#Zero-Nine
        if int(minute) < 10 and int(minute) > 0:
            current_time += ' ' + tens[0] + ' ' + hours[int(minute[1])]
#Tens
        elif int(int(minute)/10) == 1:
            current_time += ' ' + ten_fwd[int(minute)-10]
#Twenties
        elif int(int(minute)/10) == 2:
            current_time += ' ' + tens[1]
    #Test if it's exact hour or not
            if int(minute) == 0:
                pass
            else:
    #Test if the minute is a multiple of ten
                if int(minute[1]) != 0:
                    current_time += ' ' + hours[int(minute[1])]
#Thirties
        elif int(int(minute)/10) == 3:
            current_time += ' ' + tens[2]
    #Test if it's exact hour or not
            if int(minute) == 0:
                pass
            else:
    #Test if the minute is a multiple of ten
                if int(minute[1]) != 0:
                    current_time += ' ' + hours[int(minute[1])]
#Forties
        elif int(int(minute)/10) == 4:
            current_time += ' ' + tens[3]
    #Test if it's exact hour or not
            if int(minute) == 0:
                pass
            else:
    #Test if the minute is a multiple of ten
                if int(minute[1]) != 0:
                    current_time += ' ' + hours[int(minute[1])]
#Fifties
        elif int(int(minute)/10) == 5:
            current_time += ' ' + tens[4]
    #Test if it's exact hour or not
            if int(minute) == 0:
                pass
            else:
    #Test if the minute is a multiple of ten
                if int(minute[1]) != 0:
                    current_time += ' ' + hours[int(minute[1])]

#am/pm
#Midnight/Noon
    if int(hour) == 0 or int(hour) == 12:
#Test if it is Noon or between 12am-13pm
        if int(minute) == 0:
            pass
        else:
            current_time += ' am'
#am
    elif int(hour) <= 12:
        current_time += ' am'
#pm
    else:
        current_time += ' pm'

    return current_time
    
print('00:00 =>', TalkingClock('00:00'))
print('01:30 =>', TalkingClock('01:30'))
print('06:04 =>', TalkingClock('06:04'))
print('12:00 =>', TalkingClock('12:00'))
print('12:35 =>', TalkingClock('12:35'))
print('14:01 =>', TalkingClock('14:01'))
print('15:15 =>', TalkingClock('15:15'))
print('20:29 =>', TalkingClock('20:29'))
print('21:00 =>', TalkingClock('21:00'))
print('22:40 =>', TalkingClock('22:40'))