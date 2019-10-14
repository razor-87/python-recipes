# -*- coding: utf-8 -*-

import requests

params = {'#q': 'pizza'}
r = requests.get("https://www.google.com", params=params)
print("Status: ", r.status_code)
print(r.url)
print(r.text)

from io import BytesIO
from PIL import Image

r = requests.get("https://img.purch.com/rc/1920x1200/aHR0cDovL3d3dy5zcGFjZS5jb20vaW1hZ2VzL2kvMDAwLzA1Ni8xNzAvb3JpZ2luYWwvb3V0bGllci1nYWxheHktdWdjLTQ4NzktMTkyMC5qcGc=")
print("Status code:", r.status_code)
image = Image.open(BytesIO(r.content))
print(image.size, image.format, image.mode)
path = "./image1." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image")

my_data = {"name": "Nick", "email": "nick@example.co"}
r = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)




req = requests.get('https://yandex.ru/search/g', params={'text': 'Python'})
req.status_code
req.headers['Content-Type']
req.content  # bytes
req.text

with open('python.html', 'w', encoding='utf-8') as f:
    f.write(req.text)




import simplejson as json

url = "https://goo.gl/"
payload = {"longUrl": "http://example.com"}
headers = {"Content-Type": "application/json"}
r = requests.post(url, json=payload, headers=headers)
print(json.loads(r.text))
print(r.headers)

cat file.json | python -m json.tool




from collections import defaultdict
import json

def tree():
    """
    Factory that creates a defaultdict that also uses this factory
    """
    return defaultdict(tree)

root = tree()
root['Page']['Python']['defaultdict']['Title'] = 'Using defaultdict'
root['Page']['Python']['defaultdict']['Subtitle'] = 'Create a tree'
root['Page']['Java'] = None

print(json.dumps(root, indent=4))

# The "json" module can do a much better job:
print(json.dumps(my_mapping, indent=4, sort_keys=True))
{
    "a": 23,
    "b": 42,
    "c": 12648430
}
# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
json.dumps({all: 'yup'})
TypeError: keys must be a string

cat json
# {"$id":"1","currentDateTime":"2019-04-25T14:16Z","utcOffset":"00:00:00",
# "isDayLightSavingsTime":false,"dayOfTheWeek":"Thursday","timeZoneName":"UTC",
# "currentFileTime":132006753872039629,"ordinalDate":"2019-115",
# "serviceResponse":null}
null = None
true = True
false = False
with open('json') as f:
    j = eval(f.read())
j
# {'currentFileTime': 132006753872039629, 'isDayLightSavingsTime': False,
# 'dayOfTheWeek': 'Thursday', 'utcOffset': '00:00:00',
# 'serviceResponse': None,
# '$id': '1', 'timeZoneName': 'UTC', 'ordinalDate': '2019-115',
# 'currentDateTime': '2019-04-25T14:16Z'}
