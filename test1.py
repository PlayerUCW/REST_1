from requests import get, post, delete


# геты харошые
print(get('http://localhost:5000/api/users').json())
print(get('http://localhost:5000/api/users/2').json())

# пост плохой 1
print(post('http://localhost:5000/api/users', json={
    'id': 1,
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

# пост плохой 2
print(post('http://localhost:5000/api/users', json={
    'id': 1337,
    'surname': 'c',
    'name': 'c',
    'age': 0,
    'sex': 'Мужской',
    'position': 'c',
    'speciality': 'c',
    'address': 'c',
    'email': 'idk@mars.org',
    'password': '3'
}).json())

# пост харошый
print(post('http://localhost:5000/api/users', json={
    'id': 42,
    'surname': 'c',
    'name': 'c',
    'age': 0,
    'sex': 'Мужской',
    'position': 'c',
    'speciality': 'c',
    'address': 'c',
    'email': 'c@mars.org',
    'password': '3'
}).json())
print(get('http://localhost:5000/api/users/42').json())

# перепост плохой 1
print(post('http://localhost:5000/api/users/43', json={
    'surname': 'EDITED',
    'name': 'EDITED',
    'age': 0,
    'sex': 'Мужской',
    'position': 'c',
    'speciality': 'c',
    'address': 'c',
    'email': 'idk@mars.org',
    'password': '3'
}).json())

# перепост харошый
print(post('http://localhost:5000/api/users/42', json={
    'surname': 'EDITED',
    'name': 'EDITED',
    'age': 0,
    'sex': 'Мужской',
    'position': 'c',
    'speciality': 'c',
    'address': 'c',
    'email': 'c@mars.org',
    'password': '3'
}).json())
print(get('http://localhost:5000/api/users/42').json())

# удаление плохой
print(delete('http://localhost:5000/api/users/12345').json())

# удаление харошый
print(delete('http://localhost:5000/api/users/42').json())

# бд не поменялась