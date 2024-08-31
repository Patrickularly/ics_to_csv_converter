import csv
from icalendar import Calendar

def convert_ics_to_csv(ics_file, csv_file):
    with open(ics_file, 'rb') as f:
        cal = Calendar.from_ical(f.read())

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Event', 'Datum'])

        for event in cal.walk('vevent'):
            summary = event.get('summary')
            start_date = event.get('dtstart').dt.strftime('%d.%m.%Y')

            writer.writerow([summary, start_date])

# Usage example
convert_ics_to_csv('/Users/ps/Desktop/Comedy.ics', '/Users/ps/Desktop/Hahahahaha.csv')
