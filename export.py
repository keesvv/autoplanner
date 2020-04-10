import datetime
import iso8601

def parse_item(item):
    date_obj = iso8601.parse_date(item['Start'])
    friendly_date = date_obj.strftime('%a, %d %b %Y %H:%M:%S')
    contents = item['Inhoud']

    # Set contents to '' if None
    if contents == None:
        contents = ''

    return item['Vakken'][0]['Naam'] + ';'\
        + contents + ';'\
        + friendly_date + ';'\
        + '\n'

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

        # Write the columns to the roster file
        file.writelines(map(lambda c: c + ';', columns))
        file.write('\n')

        # Write the roster contents to the roster file
        file.writelines(contents)
        file.close()

