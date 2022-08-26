import json
import csv
from datetime import datetime

from constant import section_id_transfer, weekday_transger


def get_meets_reserve(login_session, reserve_name, weekday, output_csv=False):
    '''weekday:0 is Monday, 6 is Sunday'''
    url = 'https://eportal.104.com.tw/schedule/meetingData2.jsp?moid=2&section=4&viewMode=unit&d=Thu%20Aug%2025%202022%2023:26:22%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)&timeshift=-480&from=2022-08-01&to=2022-09-01'
    r = login_session.get(url).content
    rows = json.loads(r)
    target_rows = []
    for row in rows:
        reserve_date = datetime.strptime(row['start_date'], "%Y-%m-%d %H:%M")
        certain_day =  reserve_date > datetime.now() and reserve_date.weekday() == weekday
        if row['empName'] == reserve_name and certain_day :
            pick_column_row = {
                'empName': row['empName'], 
                'room_name': section_id_transfer[row['section_id']],
                'start_date': row['start_date'], 
                'end_date': row['end_date']
            }
            target_rows.append(pick_column_row)
    target_rows.sort(key = lambda row: datetime.strptime(row['start_date'], "%Y-%m-%d %H:%M"))

    ch_weekday = weekday_transger[weekday]

    if output_csv:
        fields = list(target_rows[0].keys())
        with open(f'{reserve_name}_{ch_weekday}會議預約.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(target_rows)

    return target_rows
