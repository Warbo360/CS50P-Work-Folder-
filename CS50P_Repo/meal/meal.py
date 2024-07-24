def main():
    time = input('What time is it? ') # Asking user to input a time
    time = convert(time) # Calling the convert() function we define below

    if 7.00 <= time <= 8.00: # Control flow of the time being checked to see if it falls into any of the categories and printing out the associated string
        print('breakfast time')
    elif 12.00 <= time <= 13.00:
        print('lunch time')
    elif 18.00 <= time <= 19.00:
        print('dinner time')
    else:
        print('not time to eat')

def convert(time): # Convert() that can take in both 24-hour or 12-hour inputs (assuming user inputs 'a.m.' or 'p.m' strictly)
    if time.endswith(' a.m.'):
        time = time.strip(' a.m.')
        hour, minute = time.split(':')
        hour = float(hour)
        minute = float(minute)
        hour = hour + (minute / 60)
        return hour
    elif time.endswith(' p.m.'):
        time = time.strip(' p.m.')
        hour, minute = time.split(':')
        hour = float(hour) + 12.0
        minute = float(minute)
        hour = hour + (minute / 60)
        return hour
    else:
        hour, minute = time.split(':')
        hour = float(hour)
        minute = float(minute)
        hour = hour + (minute / 60)
        return hour


if __name__ == "__main__":
    main()






