import icalendar
calFile = open('S19_schedule.ics', 'rb')
calendar = icalendar.Calendar.from_ical(calFile.read())

print(calendar)
