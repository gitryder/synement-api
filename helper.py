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


def get_row_with_keys(row):
    row[0] = row[0].replace('.', '')
    return dict(zip(data_keys, row))
