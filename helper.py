import datetime
import pytz

data_keys = [
    'id', 
    'subject', 
    'type', 
    'title', 
    'description', 
    'date_assigned',
    'date_due'
]


def clean_data(table_data):
    data = []
    for row in table_data:
        row[4] = row[4].replace('Pending', '').replace('Submitted', '')
        data.append(row[:7])
    return data


def get_date_today():
    return datetime.datetime.now(
        pytz.timezone('Asia/Kolkata')).strftime('%d-%b-%G')


def get_date_tomorrow():
    tomorrow = datetime.datetime.now(
        pytz.timezone('Asia/Kolkata')) + datetime.timedelta(days=1)
    return tomorrow.strftime('%d-%b-%G')


def get_row_with_keys(row):
    row[0] = row[0].replace('.', '')
    return dict(zip(data_keys, row))
