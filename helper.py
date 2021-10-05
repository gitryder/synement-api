import datetime
import pickle
import pytz

ASG_BASE_URL = "https://xavier.qualcampus.com/Dashboard_Assignment_Student/SubmitAssignment?Assignment_ID="
QUIZ_BASE_URL = "https://xavier.qualcampus.com/Quiz_Attempt/Index?Quiz_ID="

data_keys = [
    'id',
    'subject',
    'type',
    'title',
    'desc',
    'date_due'
]


def get_date_today():
    return datetime.datetime.now(
        pytz.timezone('Asia/Kolkata')).strftime('%d-%b-%G')


def get_date_tomorrow():
    tomorrow = datetime.datetime.now(
        pytz.timezone('Asia/Kolkata')) + datetime.timedelta(days=1)
    return tomorrow.strftime('%d-%b-%G')


def get_work_with_valid_dues(all_work):
    work_with_valid_dues = []
    for work in all_work:
        if work['date_due'] != 'N/A':
            work_with_valid_dues.append(work)
    return work_with_valid_dues


def get_row_with_keys(row):
    row[4] = row[4].replace('Pending', '').replace('Submitted', '')
    # if row[3] == '':
    #    row[3] = 'N/A'
    return dict(zip(data_keys, row))


def get_work_base_url():
    return ASG_BASE_URL


def get_quiz_base_url():
    return QUIZ_BASE_URL


def serialize_to_file(filename, data):
    with open('data/' + filename + '.pkl', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def deserialize_from_file(filename):
    with open('data/' + filename + '.pkl', 'rb') as handle:
        data = pickle.load(handle)
    return data

def get_zero_padded_date(date_string):
    if date_string == '':
        return date_string

    separator = '-'
    split_date = date_string.split(separator)
    split_date[0] = format(int(split_date[0]), '02')
    return separator.join(split_date)