import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'

result = requests.get(url)
result.status_code
result.headers
print(result.json())

