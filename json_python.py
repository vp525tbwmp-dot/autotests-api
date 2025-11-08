import json
json_data = """
{
  "name": "ivan",
  "age": 30,
  "is_student": true,
  "cources": [
  "python", 
  "Qa automation", 
  "API testing"],
  "adress":{
    "city": "moscow",
    "zip": "10100"
  }
}
"""
parsed_data = json.loads(json_data)


print(parsed_data['cources'])

data = {
    "name": "ivan",
    "age": 30,
    "is_student": True,
}
json_sting = json.dumps(data, indent=4)
print(json_sting)
print(json_sting)
print(type(json_sting))

with open("json_example.json", "r", encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data)
    print(type(read_data))


with open('json_user.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)