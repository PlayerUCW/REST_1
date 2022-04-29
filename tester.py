from requests import get, post, delete
import datetime


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
print(delete('http://localhost:5000/api/jobs/42').json())