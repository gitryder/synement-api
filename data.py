import scraper
import helper
import time

te_data = scraper.get_all_data_for("te")


def is_before_today(date_string):
    if date_string == '' or date_string == 'N/A':
        return False
    today = time.strptime(helper.get_date_today(), "%d-%b-%Y")
    day = time.strptime(date_string, "%d-%b-%Y")
    return day < today


def all_course_work(year):
    # TODO: Set data according to the year
    data = te_data

    all_course_work = []

    for row in data:
        if not is_before_today(row[5]):
            all_course_work.append(helper.get_row_with_keys(row))
    return all_course_work


def all_due_today(year):
    all_work_due_today = []
    all_work = helper.get_work_with_valid_dues(all_course_work(year))
    today = helper.get_date_today()

    for row in all_work:
        if row['date_due'] == today:
            all_work_due_today.append(row)
    return all_work_due_today


def all_due_tomorrow(year):
    all_work_due_tomorrow = []
    all_work = helper.get_work_with_valid_dues(all_course_work(year))
    tomorrow = helper.get_date_tomorrow()

    for row in all_work:
        if row['date_due'] == tomorrow:
            all_work_due_tomorrow.append(row)
    return all_work_due_tomorrow


def all_due_after_tomorrow(year):
    all_work_due_after_tomorrow = []
    all_work = all_course_work(year)

    today = helper.get_date_today()
    tomorrow = helper.get_date_tomorrow()

    for row in all_work:
        if (row['date_due'] != today and row['date_due'] != tomorrow) \
                or row['date_due'] == '':
            all_work_due_after_tomorrow.append(row)
    return all_work_due_after_tomorrow
