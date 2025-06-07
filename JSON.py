import json

x = {"name": "baqer", 
     "age": 26,
     "city": "Tehran",
     "isTeacher":False,
     "isMarried":False}

print(x)
y = json.dumps(x)
print(y)
 