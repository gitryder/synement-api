import scraper
import helper
import time

data = scraper.get_all_data()


def is_before_today(date_string):
    if date_string == '':
        return True
    today = time.strptime(helper.get_date_today(), "%d-%b-%Y")
    day = time.strptime(date_string, "%d-%b-%Y")
    return day < today


def all_course_work():
    all_course_work = []

    for row in data[1:]:
        if not is_before_today(row[6]):
            all_course_work.append(helper.get_row_with_keys(row))
    return all_course_work


def all_assignments():
    all_assignments = []

    for row in data[1:]:
        if row[2] == 'Assignment':
            all_assignments.append(helper.get_row_with_keys(row))
    return all_assignments


def all_due_today():
    all_work_due_today = []
    all_work = all_course_work()
    today = helper.get_date_today()

    for row in all_work:
        if row['date_due'] == today:
            all_work_due_today.append(row)
    return all_work_due_today


def all_due_tomorrow():
    all_work_due_tomorrow = []
    all_work = all_course_work()
    tomorrow = helper.get_date_tomorrow()

    for row in all_work:
        if row['date_due'] == tomorrow:
            all_work_due_tomorrow.append(row)
    return all_work_due_tomorrow


def all_due_after_tomorrow():
    all_work_due_after_tomorrow = []
    all_work = all_course_work()

    today = helper.get_date_today()
    tomorrow = helper.get_date_tomorrow()

    for row in all_work:
        if row['date_due'] != today and row['date_due'] != tomorrow:
            all_work_due_after_tomorrow.append(row)
    return all_work_due_after_tomorrow


def all_experiments():
    all_experiments = []
    for row in data[1:]:
        if row[2] == 'Experiment':
            all_experiments.append(helper.get_row_with_keys(row))
    return all_experiments
