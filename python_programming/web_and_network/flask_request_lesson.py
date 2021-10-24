import requests

r = requests.get('http://127.0.0.1:5000/employee/jun')
print(r.text)

r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'jun'})
print(r.text)

r = requests.put('http://127.0.0.1:5000/employee', data={'name': 'jun', 'new_name': 'yoshiki'})
print(r.text)

r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'jun'})
print(r.text)