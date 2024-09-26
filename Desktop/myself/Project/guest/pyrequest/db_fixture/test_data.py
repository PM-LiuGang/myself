import sys
sys.path.append(r'C:\Users\admin\guest\pyrequest\db_fixture')
from mysql_db import DB

datas = {
    'sign_event': [
        {'id': 1, 'name': '红米1', 'limit':2000, 'status': 1,
         'address':'北京1', 'start_time': '2017-08-01 12:00:00'},
        {'id': 2, 'name': '红米2', 'limit': 2000, 'status': 1,
         'address': '北京1', 'start_time': '2017-08-01 12:00:00'},
        {'id': 3, 'name': '红米3', 'limit': 2000, 'status': 1,
         'address': '北京1', 'start_time': '2017-08-01 12:00:00'},
        {'id': 4, 'name': '红米4', 'limit': 2000, 'status': 1,
         'address': '北京1', 'start_time': '2017-08-01 12:00:00'},
        {'id': 5, 'name': '红米5', 'limit': 2000, 'status': 1,
         'address': '北京1', 'start_time': '2017-08-01 12:00:00'},
    ],
    'sign_guest': [
        {'id': 1, 'realname': 'liugang1', 'phone':13012340001, 
         'email':'liugang1@139.com',
         'sign': 0, 'event_id': 1},
        {'id': 2, 'realname': 'liugang2', 'phone': 13012340002, 
         'email': 'liugang1@139.com',
         'sign': 0, 'event_id': 5},
        {'id': 3, 'realname': 'liugang3', 'phone': 13012340003, 
         'email': 'liugang1@139.com',
         'sign': 0, 'event_id': 4},
        {'id': 4, 'realname': 'liugang4', 'phone': 13012340004, 
         'email': 'liugang1@139.com',
         'sign': 0, 'event_id': 2},
        {'id': 5, 'realname': 'liugang5', 'phone': 13012340005, 
         'email': 'liugang1@139.com',
         'sign': 0, 'event_id': 2},
    ]
}


def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


if __name__ == '__main__':
    init_data()

