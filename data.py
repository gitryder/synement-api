import scraper
import helper

data = scraper.get_all_data()


def all_course_work():
    all_course_work = []
    for row in data[1:]:
        all_course_work.append(helper.get_row_with_keys(row))
    return all_course_work


def all_assignments():
    all_assignments = []
    for row in data[1:]:
        if row[2] == 'Assignment':
            all_assignments.append(helper.get_row_with_keys(row))
    return all_assignments


def all_experiments():
    all_experiments = []
    for row in data[1:]:
        if row[2] == 'Experiment':
            all_experiments.append(helper.get_row_with_keys(row))
    return all_experiments
