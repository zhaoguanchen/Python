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
### 8.function 函数
```py
# 函数定义
# 默认值
def func(var1, var2='dog'):
    print(var1.title() + ' is ' + var2)

# 传递形参
dog = "dog"
func(dog)

# 传递实参
func("cat", "cat")
# 指定参数 关键字实参
func(var1="value")
```
#### 有返回值：
```py
def function(a, b):
    return a + b


c = function(1, 2)
print(c)
```

#### 传递列表：

```py
def function(var1, var2):
    while a:
        current_number = a.pop()
        print("the current_number is " + current_number)
        b.append(current_number)


a = ["one", "two", "three"]
b = []
function(a, b)
print(a)
print(b)
```

#### 任意数量的实参

```py
# *var2创建一个元组，将收到的所有参数放到元组中
def function(var1, *var2):
    print(var2)


function("12", "32", 44, "ff")



# **创建一个字典，将收到的参数放到字典中
def function(var1, **var2):
    print(var2)


function(1, num="32", num2='44')
# result: {'num': '32', 'num2': '44'}
```

#### 导入模块
模块名称  source.py
```py
# 导入
import source

# 导入特定函数
from module_name import function_name
# 导入多个
from module_name import function_name1, function_name2
# 指定别名
import module_name as module

from module_name import function_name as func
```

### 9.class 类
__init__(self)类似于构造方法

```py
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print("sit")
        
        
dag = Dog("zhao", 11)
print(dag.age)
dag.sit()

```


###10. file 文件 & 异常
读取文件：
```py
with open(file_name) as f_obj:
    contents = f_obj.read()
    # lines = f_obj.readlines()   逐行读取
```
```py
file_name = '/Users/zhaoguanchen/Desktop/txt/A Garden of Girls.txt'

try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except EOFError:
    msg = "sorry, ERROR"
    print msg
else:
    words = contents.split()
    num_words = len(words)
    print ("the quantity of words is " + str(num_words))

    importance = "importance"
    if importance in words:
        print(importance + " in words")
```

写入文件：
附加模式：`open(file_name, 'a')`   会追加append
写入模式：`open(file_name, 'w')`   会覆盖
```py

# coding=UTF-8
# 智能写入字符串，其他数据类型需要转化成字符串类型
file_name = '/Users/zhaoguanchen/Desktop/txt/writing.txt'
with open(file_name, 'a') as file_obj:
    file_obj.writelines("I love you py\n")
    file_obj.write("hhhh")

```
异常：
try-except
```py
try:
    5/0
except ZeroDivisionError:
    msg = "sorry, ZeroDivisionError"
    print msg
else:
    print 'ok'

```





