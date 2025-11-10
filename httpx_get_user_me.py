import httpx

login_payload = {"email": "a.malahov@t-code.ru", "password": "fadase"}
resp = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
data = resp.json()

# достаём токен и сохраняем в переменную
access_token = data["token"]["accessToken"]
print({"token": access_token})

# формируем правильные заголовки
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json",
}

me_resp = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(me_resp.status_code, me_resp.text)
