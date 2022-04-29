from requests import get, post, delete
import datetime


# геты харошые
print(get('http://localhost:5000/api/jobs').json())
print(get('http://localhost:5000/api/jobs/1').json())

# пост плохой 1
print(post('http://localhost:5000/api/jobs', json={
    'id': 1,
    'team_leader': 1,
    'job': 'procrastinate',
    'work_size': 42,
    'collaborators': '2, 3',
    'start_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
    'end_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
    'is_finished': False
}).json())

# пост плохой 2
print(post('http://localhost:5000/api/jobs', json={
    'id': 42,
    'team_leader': 1,
    'job': 'procrastinate',
    'work_size': 42,
    'collaborators': '2, 3',
    'start_date': 'намедни',
    'end_date': 'к завтрему',
    'is_finished': False
}).json())

# пост харошый
print(post('http://localhost:5000/api/jobs', json={
    'id': 42,
    'team_leader': 1,
    'job': 'procrastinate',
    'work_size': 42,
    'collaborators': '2, 3',
    'start_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
    'end_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
    'is_finished': False
}).json())
print(get('http://localhost:5000/api/jobs/42').json())

# перепост плохой 1
print(post('http://localhost:5000/api/jobs/43', json={
    'team_leader': 1,
    'job': 'EDITED',
    'work_size': 42,
    'collaborators': '2, 3',
    'start_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
    'end_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
    'is_finished': True
}).json())

# перепост харошый
print(post('http://localhost:5000/api/jobs/42', json={
    'team_leader': 1,
    'job': 'EDITED',
    'work_size': 42,
    'collaborators': '2, 3',
    'start_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
    'end_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
    'is_finished': True
}).json())
print(get('http://localhost:5000/api/jobs/42').json())

# удаление плохой
print(delete('http://localhost:5000/api/jobs/12345').json())

# удаление харошый
print(delete('http://localhost:5000/api/jobs/42').json())

# бд не поменялась