VCALENDAR(
	{
		u'CALSCALE': vText('GREGORIAN'),
		u'VERSION': vText('2.0'),
		u'PRODID': vText('-CMU SIOiCal4j 1.0EN')
	}
,
VEVENT(
	{
		u'LOCATION': vText('GHC- 4102'),
		u'DTSTAMP': <icalendar.prop.vDDDTypes object at 0x7f034d529610>, 
		u'RRULE': vRecur(
				{
					u'BYDAY': [u'TU', u'TH'], 
					u'FREQ': [u'WEEKLY'], 
					u'UNTIL': [datetime.date(2019, 5, 5)]
				}), 
		u'DESCRIPTION': vText('Building User-Focused Sensing Systems :: 17722 A\n\nInstructors: Agarwal\; Goel\n'), 
		u'DTEND': <icalendar.prop.vDDDTypes object at 0x7f034b8a8550>, 
		u'DTSTART': <icalendar.prop.vDDDTypes object at 0x7f034ba56250>, 
		u'SUMMARY': vText('Building User-Focused Sensing Systems :: 17722 A')
	}), 

VEVENT(
	{	u'LOCATION': vText('PH- 226B'), 
		u'DTSTAMP': <icalendar.prop.vDDDTypes object at 0x7f034ba24290>, 
		u'RRULE': vRecur(
				{
					u'BYDAY': [u'TU', u'TH'], 
					u'FREQ': [u'WEEKLY'], 
					u'UNTIL': [datetime.date(2019, 5, 5)]
				}), 
		u'DESCRIPTION': vText('Networked Cyber-Physical Systems :: 18651 A\n\nInstructor: Marculescu\n'), 
		u'DTEND': <icalendar.prop.vDDDTypes object at 0x7f034b8a8610>, 
		u'DTSTART': <icalendar.prop.vDDDTypes object at 0x7f034b8a85d0>, 
		u'SUMMARY': vText('Networked Cyber-Physical Systems :: 18651 A')
	}), 

VEVENT(
	{	u'LOCATION': vText('WEH- 5312'), 
		u'DTSTAMP': <icalendar.prop.vDDDTypes object at 0x7f034b8a8650>, 
		u'RRULE': vRecur(
				{
					u'BYDAY': [u'MO', u'WE'], 
					u'FREQ': [u'WEEKLY'], 
					u'UNTIL': [datetime.date(2019, 5, 5)]
				}), 
		u'DESCRIPTION': vText('Wireless Sensor Networks :: 18748 A\n\nInstructor: Rajkumar\n'), u'DTEND': <icalendar.prop.vDDDTypes object at 0x7f034b8a86d0>, 
		u'DTSTART': <icalendar.prop.vDDDTypes object at 0x7f034b8a8690>, 
		u'SUMMARY': vText('Wireless Sensor Networks :: 18748 A')
	}), 

VEVENT(
	{
		u'LOCATION': vText('HL- A5'), 
		u'DTSTAMP': <icalendar.prop.vDDDTypes object at 0x7f034b8a8710>, 
		u'RRULE': vRecur(
				{
					u'BYDAY': [u'SU'], 
					u'FREQ': [u'WEEKLY'], 
					u'UNTIL': [datetime.date(2019, 3, 6)]
				}), 
		u'DESCRIPTION': vText('IDeATe: 3D Modeling and 3D Printing :: 99359 A3\n\nInstructor: Lyness\n'), 
		u'DTEND': <icalendar.prop.vDDDTypes object at 0x7f034b8a8790>, 
		u'DTSTART': <icalendar.prop.vDDDTypes object at 0x7f034b8a8750>, 
		u'SUMMARY': vText('IDeATe: 3D Modeling and 3D Printing :: 99359 A3')
	})
)

