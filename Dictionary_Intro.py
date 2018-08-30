Python dictionary is an unordered collection of items. 
While other compound data types have only value as an element, a dictionary has a key: value pair.
Dictionaries are optimized to retrieve values when the key is known.

#create dictionary
details ={
           'name':"Guhan",
            'age':27,
            'mobile':698698,
            "address":{
                "No":123,
                "Street":"South"
            },


}
print(details)
print(details['name'])
print(details['address'])
print(details["address"]["Street"])

#Sort by key

print(sorted(details.keys()))

for key in sorted(details):
    print(key, details[key])

keylist = details.keys()
print(keylist)
# dict_keys(['name', 'age', 'mobile', 'address'])

L=list(details)
print(L)
print(sorted(L))

# Sorted by values

data = {
         "price2":1288,
         "price1":2388,
          "price3":35355
}
print(sorted(data.values()))
x=sorted(data.values())

for value in range(0, len(x)):
     print(x[value])

x=sorted(data, key=data.__getitem__)
print(x)

x=[value for (key, value) in sorted(data.items())]
print(x)

x=sorted(data, key=data.__getitem__, reverse=True)
print(x)

print(sorted(data, key=str.lower))


Result:

{'name': 'Guhan', 'age': 27, 'mobile': 698698, 'address': {'No': 123, 'Street': 'South'}}
Guhan
{'No': 123, 'Street': 'South'}
South
['address', 'age', 'mobile', 'name']
address {'No': 123, 'Street': 'South'}
age 27
mobile 698698
name Guhan
dict_keys(['name', 'age', 'mobile', 'address'])
['name', 'age', 'mobile', 'address']
['address', 'age', 'mobile', 'name']
[1288, 2388, 35355]
1288
2388
35355
['price2', 'price1', 'price3']
[2388, 1288, 35355]
['price3', 'price1', 'price2']
['price1', 'price2', 'price3']
