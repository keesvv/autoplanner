import datetime
import iso8601
import html2text
import textwrap
import functools

"""
Convert HTML markup to plain text
"""
def to_plain(html):
    return html2text.html2text(html)\
        .replace('\n', ' ')\
        .strip()

"""
Join chunks together
"""
def join_chunks(chunks):
    return functools.reduce(
        lambda a, b: a + b,
        list(
            map(lambda c: c + '\n;', chunks)
        )
    )

"""
Parse a roster item
"""
def parse_item(item):
    date_obj = iso8601.parse_date(item['Start'])
    friendly_date = date_obj.strftime('%a, %d %b %Y %H:%M:%S')
    contents = item['Inhoud']

    # Set contents to '' if None
    if contents == None:
        contents = ''
    else:
        contents = to_plain(contents)
        split_contents = textwrap.wrap(contents, 100)
        contents = join_chunks(split_contents)

    # Return a parsed line
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
        file.write('\n\n')

        # Write the roster contents to the roster file
        file.writelines(contents)
        file.close()

