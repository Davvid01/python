import json
#zad1 https://pynative.com/python-json-exercise/

"""
data = {"key1" : "value1", "key2" : "value2"}
jsonData = json.dumps(data)
print(jsonData)

#zad2
sampleJson = ""{"key1": "value1", "key2": "value2"}""

parsed=json.loads(sampleJson)
print(parsed)
print(parsed['key2'])

#zad3
sampleJson = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
test=json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(test)
"""
#zad4
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
sortedjson=json.dumps(sampleJson, sort_keys=True)
print(sortedjson)

#zad5
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
nested=json.loads(sampleJson)
print(nested['company']['employee']['payble']['salary'])
"""
#zad6
from json import JSONEncoder
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
# or
class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
print(json.dumps(vehicle, indent=7, cls=VehicleEncoder)) #cls to parametr w json.dumps umożliwiający przekazanie niestandardowego enkodera.
print(json.dumps(vehicle.__dict__, indent=2))
"""
#zad7
from types import SimpleNamespace
data='{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'

vehicleObj=json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)

#or
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
def vehicleDecoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])
vehicleObj1=json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }', object_hook=vehicleDecoder) #The error occured because you're calling the vehicleDecoder function instead of passing it as a reference to the object_hook parameter. The object_hook parameter expects a function reference that takes one argument (the object to be decoded) and returns a custom object.
print(type(vehicleObj1))                                                                      #jesli dodam nawiasy do vehicleDecoder to powowduje ze funkcja jest już wytwoływana, a powinna jedynie być przekazywana jako refference
"""
#zad8 sprawdzanie błędnego JSON
zbior='{
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000
            "bonus":800
         }
      }
   }
}'
def checking(mojedane):
    try:
        json.loads(mojedane)
    except ValueError:
        return False
    return True
print(checking(zbior))
print(json.loads(zbior))

#echo { "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } } | python -m json.tool
"""
#zad9
zbior_name="""[
   {
      "id":1,
      "name":"name1",
      "color":[
         "red",
         "green"
      ]
   },
   {
      "id":2,
      "name":"name2",
      "color":[
         "pink",
         "yellow"
      ]
   }
]"""
try:
    test=json.loads(zbior_name)
except Exception as e:
    print(e)
print(test)
lista=[]
for x in test:
    #print(x)
    print(x['name'])
    lista+=x.get('name')
print(lista)
