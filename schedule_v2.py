import datetime
import icalendar 

calFile = open('S19_schedule.ics', 'rb')
calendar = icalendar.Calendar.from_ical(calFile.read())

now = datetime.datetime.now().replace(microsecond=0)
#print(now)
#print(type(now))

#print(calendar.get("VEVENT"))
for e in calendar.walk():
    if e.name == "VEVENT":
        print('____________________________________________________')
        print(e.get('dtstart').dt)
        print(e.get('location'))
        print(e.get('dtstamp'))
        print(e.get('rrule'))
        print(e.get('freq'))
        print(e.get('until'))
        print(e.get('description'))
        print(e.get('dtstart'))
        print(e.get('dtend'))
        print(e.get('summary'))
        print('\n')
