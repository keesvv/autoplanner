import datetime
import iso8601

def parse_item(item):
    #date_obj = datetime.datetime.strptime(item['Start'], '%Y-%m-%dT%H:%M:%SZ')
    date_obj = iso8601.parse_date(item['Start'])
    friendly_date = date_obj.strftime('%a, %d %b %Y %H:%M:%S')

    return item['Vakken'][0]['Naam'] + ';'\
        + item['Inhoud'] + ';'\
        + friendly_date + ';'

class Exporter:
    def __init__(self, data):
        self.data = data

    def export_csv(self):
        columns = [
            'Subject',
            'Description',
            'Date'
        ]
        
        contents = map(parse_item, self.data)

        file = open('roster.csv', 'w')
        file.writelines(map(lambda c: c + ';', columns))
        file.write('\n')
        file.writelines(contents)
        file.close()

