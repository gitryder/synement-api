from bs4 import BeautifulSoup
import helper as helper
import requests

session = requests.Session()

payload = {
    'AY_ID': 21,
    'UserName': '2020012004',
    'Password': 'testtesttest'
}

s = session.post("https://xavier.qualcampus.com/Account/LogOn", data=payload)
s = session.get('https://xavier.qualcampus.com/Dashboard_Assignment_Student')

soup = BeautifulSoup(s.text, 'html.parser')
table = soup.find('table', attrs={
    'id': 'AssignmentListTable'
})


def get_all_data():
    rows = []
    trs = table.find_all('tr')
    headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')]
    if headerow:
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs:
        rows.append([td.get_text(strip=True) for td in tr.find_all('td')])
    return helper.clean_data(rows)
