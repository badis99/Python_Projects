def add_time(start, duration, day=''):
    week_days = {
        'MONDAY': 1,
        'TUESDAY': 2,
        'WEDNESDAY': 3,
        'THURSDAY': 4,
        'FRIDAY': 5,
        'SATURDAY': 6,
        'SUNDAY': 7,
    }

    hours = int(start[:start.find(':')])
    minutes = int(start[start.find(':') + 1:start.find(' ')])
    date_format = start[start.find(' ') + 1:]
    hours_to_add = int(duration[:duration.find(':')])
    minutes_to_add = int(duration[duration.find(':') + 1:])

    hours_to_add += (minutes + minutes_to_add) // 60
    minutes = (minutes + minutes_to_add) % 60
    if len(str(minutes)) == 1:
        minutes = '0' + str(minutes)
    days = (hours + hours_to_add) // 12
    hours = (hours + hours_to_add) % 12
    if hours == 0:
        hours = '12'
    next_day = 0
    if date_format == 'PM':
        if days % 2 == 1:
            date_format = 'AM'
            next_day = (days // 2) + 1
        else:
            next_day = (days // 2)
    else:
        if days % 2 == 0:
            next_day = (days // 2)
        else:
            date_format = 'PM'
            next_day = (days // 2)

    if len(day) != 0:
        num = week_days[day.upper()]
        num = (num + next_day) % 7
        if num == 0:
            num = 7
        for i, j in week_days.items():
            if num == j:
                day = i
                break
        day = day.lower().capitalize()
        new_time = str(hours) + ':' + str(minutes) + ' ' + date_format + ',' + ' ' + day
    else:
        new_time = str(hours) + ':' + str(minutes) + ' ' + date_format
    if next_day == 1:
        new_time += ' ' + '(next day)'
    elif next_day > 1:
        new_time += ' ' + f'({next_day} days later)'

    return new_time


print(add_time('2:59 AM', '24:00', 'saturDay'))