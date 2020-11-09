import requests

r =requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(f'request :{r.request} ')
print(f'status code :{r.status_code}')
print(f'headers :{r.headers}')
print(f'body : {r.text}')
