# syntax
Reference: python编程从入门到实践

## fundamental
```py
print("hello python world")
name = "gczhao"
print(name.title())
print(name.istitle())
```
### list
```py
array = ['you', 'I', 'and', 'he', 'she']
```
#### ADD
1.append
```py
# add after the last one
array.append("hh")
``` 
2.insert
```py
# anywhere
# if index>length, it will be "append()"
array.insert(1,"new")
```
#### MODIFY
```py
array[0] = `"new String"
``` 
#### DELETE
1.del
```py
del array[1]
```
2.pop 
```py
# the last one
array.pop()
# specified one     x should little than the length of list
array.pop(2)
```  
3.remove
```py
#  list.remove(x): x should in list
array.remove("you")
```     
#### cycle
```py
for item in array:
    print(item)
```
#### index
```py
array = ['you', 'I', 'and', 'he', 'she']
print(array[1:])
print(array[:3])
print(array[-2])
```

#### copy list
`copy_array = array[:]` is the real copy method.
`copy_array = array` just added reference.
```py
copy_array = array
print(array[:])
print(copy_array[:])
array.append("hah")
print(array[:])
print(copy_array[:])

copy_array = array[:]
print(array[:])
print(copy_array[:])
array.append("xii")
print(array[:])
print(copy_array[:])
```

#### 列表解析
```py
squares = [value ** 2 for value in range(1, 10)]
print(squares)
```


#### tuple 元组
tuple object does not support item assignment.  

```py
dimensions = (100, 200)

print(dimensions[0])
print(dimensions[1])

```



### 5.if
```py
age = 24
if age < 20:
    print("age < 20")
elif age < 25:
    print("age < 25")
else:
    print("else")
```
### 6.Dictionary 字典

```py
dicts = {"color": "green", "point": 4}

print(dicts["color"])
print(dicts["point"])

```

#### add key-value
```py
dicts["size"] = 10
```

#### modify key-value
```py
dicts["color"] = "red"
```

#### delete key-value
```py
del dicts["color"]
```
#### go through
```py
dicts = {"color": "green", "point": 4}
for key, value in dicts.items():
    print("key:", key)
    print("value:", value)

for key in dicts.keys():
    print("key:", key)

for v in dicts.values():
    print("v:", v)
```

#### nesting 嵌套
```py
dicts = {"color": "green", "point": 4}
dicts2 = {"width": 10, "height": 19}
pDicts = {"one": dicts, "two": dicts2}
print(pDicts)
```

result: `{'one': {'color': 'green', 'point': 4}, 'two': {'width': 10, 'height': 19}}`


### 7. input and while
#### input()
```py
message = input("please input your name:")
print("your name is: " + message)
```

#### while
it is as same as other language.
```py
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    if current_number == 7:
        break
    print(current_number)
```
### function 函数




