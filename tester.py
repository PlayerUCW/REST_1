from requests import get, post, delete


print(post('http://localhost:5000/api/users', json={
    'id': 7,
    'surname': 'c',
    'name': 'c',
    'age': 0,
    'sex': 'Мужской',
    'position': 'c',
    'speciality': 'c',
    'address': 'c',
    'email': 'c@c.c',
    'password': '3'
}).json())

print(get('http://localhost:5000/api/users/7').json())
print(post('http://localhost:5000/api/users/7', json={
    'surname': 'EDITED',
    'name': 'EDITED',
    'age': 0,
    'sex': 'Мужской',
    'position': 'c',
    'speciality': 'c',
    'address': 'c',
    'email': 'c@c.c',
    'password': '3'
}).json())
print(get('http://localhost:5000/api/users/7').json())
print(delete('http://localhost:5000/api/users/7').json())