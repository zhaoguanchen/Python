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
### 6.Dictionary

