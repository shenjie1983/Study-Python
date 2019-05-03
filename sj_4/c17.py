import json

student1 = [
            {'name':'qiyue', 'age': 18, 'flag': False},
            {'name':'qiyue', 'age': 18}
          ]

json_str1 = json.dumps(student1)
print(type(json_str1))
print(json_str1)
