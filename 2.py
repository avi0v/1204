#dictionary
# key:value pair
a={'name':'avi','age':25,'gender':'M'}

print(a['age']) # accessing value via keys
print(a.keys()) #all keys in dict
print(a.values()) # all values in dict
print(a.items()) # [(key,value)] k,v tuple
a['name']='sajan' # over writing value 
print(a)

print("-----------------------------")
print("-----------------------------")
# now nested dict
a['address']={'city':'ptk','pin code':145001,'state':'punjab'}
print(a)
#accessing neated dict
print(a['address']['city'])

# surname bwt name and age
b=a.items()
b=list(b)
print(b)
b.insert(1,('surname','vashisht'))
print(b)
b=dict(b)
a=b
print(a)