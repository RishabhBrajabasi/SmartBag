from ics import Calendar
from ics import timeline

import datetime
import arrow

read_calendar = open("S19_schedule.ics").read()
c = Calendar(read_calendar.decode('iso-8859-1'));


#TODO: String and time and stuff. 
#now = datetime.datetime.now().replace(microsecond=0)
#now7 = now + datetime.timedelta(days = 7)
#now = now.isoformat()
#now = arrow.utcnow()
#print(now)
#print(now7)


# Events which are on the same day
# Events which are after the current time
#print len(c.events)
#for eve in range(0,len(c.events)):
#    print c.events[eve].begin
#    print c.events[eve].end
#    print(type(c.events[eve].begin))
#    if(c.events[eve].begin < now):
#        print("There is an event")
#now = datetime.datetime.now()
#print now.isoformat()


