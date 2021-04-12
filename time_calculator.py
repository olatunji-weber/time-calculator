def add_time(start, duration, day=None):
    meridians = 0
    daysAdded = 0
    initialModifier = modifier = start.split(" ")[1]
    daysInWeek = ("Sunday", "Monday", "Tuesday","Wednesday","Thursday", "Friday", "Saturday")

    start = start.split(" ")
    start.pop(1)
    start = "".join(start)

    hour = int(start.split(":")[0]) + int(duration.split(":")[0])
    minute = int(start.split(":")[1]) + int(duration.split(":")[1])

    if minute > 59:
        minute -= 60
        hour += 1
    
    hourModifier = hour
    while hour > 12:
        hour -= 12
        
    while hourModifier > 11:
        hourModifier -= 12
        if modifier == "AM":
            modifier = "PM"
        else:
            modifier = "AM"
        meridians += 1

    if meridians % 2 != 0:
        if initialModifier == "AM":
            meridians -= 1
        else:
            meridians += 1
    daysAdded = meridians/2
    
    resultantTime = f"{hour}:{str(minute).zfill(2)} {modifier}"

    if day:
        weekday = daysInWeek.index(day.title())
        newWeekday = int((weekday + daysAdded) % 7)
        resultantTime += f", {daysInWeek[newWeekday]}"

    if daysAdded == 1:
        resultantTime += " (next day)"

    if daysAdded > 1:
        resultantTime += f" ({int(daysAdded)} days later)"
    
    return resultantTime