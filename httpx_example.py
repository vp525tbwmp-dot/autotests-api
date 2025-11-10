from importlib.metadata import files

import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

data = {
    "title": "Новая задача",
    "completed": False,
    "userid": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)
print(response.request.headers)
print(response.json())


data = {"username": "testuser", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)

print(response.status_code)
print(response.json())

headers = {"authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.request.headers)
print(response.json())

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)
print(response.json())


files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())