from bs4 import BeautifulSoup
import os
import helper
import requests

session = requests.Session()


def get_tables_for(year=""):
    if (year == "se"):
        username = os.environ.get('SYNE_SE_USER')
        password = os.environ.get('SYNE_SE_PASS')
    elif (year == "be"):
        username = os.environ.get('SYNE_BE_USER')
        password = os.environ.get('SYNE_BE_PASS')
    else:
        username = os.environ.get('SYNE_USER')
        password = os.environ.get('SYNE_PASS')

    payload = {'AY_ID': 21, 'UserName': username, 'Password': password}

    s = session.post(
        "https://xavier.qualcampus.com/Account/LogOn", data=payload)

    s = session.get(
        'https://xavier.qualcampus.com/Dashboard_Assignment_Student')
    soup = BeautifulSoup(s.text, 'html.parser')
    asg_table = soup.find('table', attrs={'id': 'AssignmentListTable'})

    s = session.get('https://xavier.qualcampus.com/Dashboard_Quiz_Student')
    soup = BeautifulSoup(s.text, 'html.parser')
    quiz_table = soup.find('table', attrs={'id': 'QuizSummaryTbl'})

    return [asg_table, quiz_table]


def get_clean_tables_list(list, asg_ids, quiz_ids):
    asg_table = list[0]
    quiz_table = list[1]

    del asg_table[0]
    for asg in asg_table:
        del asg[0]
        del asg[2:5]
        del asg[3:]

    del quiz_table[0]
    for quiz in quiz_table:
        quiz[3] = 'Quiz'
        del quiz[:2]
        del quiz[3:]

    for i in range(0, len(asg_table)):
        asg_id = int(asg_ids[i][0])
        asg_table[i].insert(0, asg_id)
        asg_table[i].append(f"{helper.get_work_base_url()}{asg_id}")

    for i in range(0, len(quiz_table)):
        quiz_id = int(quiz_ids[i][0])
        quiz_table[i].insert(0, quiz_id)
        quiz_table[i].append(f"{helper.get_quiz_base_url()}{quiz_id}")

    return asg_table + quiz_table


def get_all_data_for(year):
    tables = get_tables_for(year)

    rows = []
    clean_tables = []

    assignment_ids = []
    for tr in tables[0].find_all('tr'):
        assignment_ids.append([td['assignment_id']
                              for td in tr.find_all(attrs={'type': 'button'})])

    quiz_ids = []
    for tr in tables[1].find_all('tr'):
        quiz_ids.append([td['quiz_id']
                        for td in tr.find_all(attrs={'type': 'button'})])

    # Delete the first items because
    # they're always going to be empty
    del assignment_ids[0]
    del quiz_ids[0]

    for table in tables:
        trs = table.find_all('tr')
        headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')]
        if headerow:
            rows.append(headerow)
            trs = trs[1:]
        for tr in trs:
            rows.append([td.get_text(strip=True) for td in tr.find_all('td')])
        clean_tables.append(rows)
        rows = []

    return get_clean_tables_list(clean_tables, assignment_ids, quiz_ids)
