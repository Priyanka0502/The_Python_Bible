'''
python dictionaries has some keys and some values too!!

dictionary are not iterables and we cannot find the keys values like we use to
do in list and strings i.e., using indexing . we have to find values by
giving keys .
------>>>>>>print(students.keys()[0])<<<<<<<<------------
---------------
print(students.keys()[0])
TypeError: 'dict_keys' object is not subscriptable
-------------------
To do so we have to convert dict to list and then do the process.



'''

students={"Alice":20,
          "bob":25,
          "priyanka":24,
          "satyam":23,
          "rani":18}
print(students)
print(type(students))
print(students["Alice"]) # to find the value of item key
print("delete items from dict using del keyword")
del students["bob"] # should give the key value here:
print(students)

print('find the keys in dict using keys() functions')
print(students.keys())
a=list(students.keys())
print(a)
print(a[1])
print(students.items()) #dict_items([('Alice', 20), ('priyanka', 24)])  -->> each item is tuple
print(students.values()) #dict_values([20, 24])

print('----------------------------------------------------------------')
print('----------------------------------------------------------------')
print("combining dict with list: the values are taken here as list")
student2={"Alice":["ID0001",26,"A"],
          "bob":["ID0002",24,"B"],
          "priyanka":["ID0003",17,"C"],
          "satyam":["ID0004",21,"D"],
          "rani":["ID0005",22,"E"]
          }
print(student2["Alice"])  #value of alice is printed here
print(student2["Alice"][0]) # since key of ALice is list so we can fetch details using index
print(student2["Alice"][1:])

print('----------------------------------------------------------------')
print('----------------------------------------------------------------')
print('-----------dict in dict-------')
student2={"Alice":{"Id":"ID0001","Age":26,"Grade":"A"},
          "Bob":{"Id":"ID0002","Age":24,"Grade":"B"},
          "Priyanka":{"Id":"ID0003","Age":17,"Grade":"C"},
          "Satyam":{"Id":"ID0004","Age":21,"Grade":"D"},
          "Rani":{"Id":"ID0005","Age":22,"Grade":"E"}
          }
print('details of Alice:')
print(student2["Alice"])
print('details of age:')
print(student2["Alice"]["Age"])
print("details of bob:")
print(student2["Bob"]["Id"],student2["Bob"]["Grade"])









