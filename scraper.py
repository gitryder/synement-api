from bs4 import BeautifulSoup
import os
import helper
import requests

session = requests.Session()

def get_tables_for(year=""):
    if (year == "se"):
        username =  os.environ.get('SYNE_SE_USER')
        password =  os.environ.get('SYNE_SE_PASS')
    elif (year == "be"):
        username =  os.environ.get('SYNE_BE_USER')
        password =  os.environ.get('SYNE_BE_PASS')
    else:
        username =  os.environ.get('SYNE_USER')
        password =  os.environ.get('SYNE_PASS')

    payload = {'AY_ID': 21, 'UserName': username, 'Password': password}

    s = session.post("https://xavier.qualcampus.com/Account/LogOn", data=payload)

    s = session.get('https://xavier.qualcampus.com/Dashboard_Assignment_Student')
    soup = BeautifulSoup(s.text, 'html.parser')
    asg_table = soup.find('table', attrs={'id': 'AssignmentListTable'})

    s = session.get('https://xavier.qualcampus.com/Dashboard_Quiz_Student')
    soup = BeautifulSoup(s.text, 'html.parser')
    quiz_table = soup.find('table', attrs={'id': 'QuizSummaryTbl'})

    return [asg_table, quiz_table]


def get_all_data_for(year):
    tables = get_tables_for(year)

    rows = []
    for table in tables:
        trs = table.find_all('tr')
        headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')]
        if headerow:
            rows.append(headerow)
            trs = trs[1:]
        for tr in trs:
            rows.append([td.get_text(strip=True) for td in tr.find_all('td')])
    return helper.clean_data(rows)