# 创建dict
方法1:

创建一个空的dict，这个空dict，可以在以后向里面加东西用。
屁
>>> mydict = {}
>>> mydict
{}

>>> person ={"name":"hujun","sex":"men"}
>>> person
{'name': 'hujun', 'sex': 'men'}



>>> person['city']="hangzhou"    #这是一种向dict中增加键值对的方法


方法2:

利用元组在建构字典，方法如下：
>>> ad = dict(name="qiwsir", age=42)
>>> ad
{'age': 42, 'name': 'qiwsir'}

方法3:

这个方法，跟上面的不同在于使用fromkeys

>>> website = {}.fromkeys(("third","forth"),"facebook")
>>> website
{'forth': 'facebook', 'third': 'facebook'}



len(d)，返回字典(d)中的键值对的数量
d[key]，返回字典(d)中的键(key)的值
d[key]=value，将值(value)赋给字典(d)中的键(key)
del d[key]，删除字典(d)的键(key)项（将该键值对删除）
key in d，检查字典(d)中是否含有键为key的项


# copy  
person ={"name":"hujun","sex":"men"}
>>>person2=person.copy()
>>>person2  
>>>person2 ={"name":"hujun","sex":"men"}

# clear 清空字典中所有元素

>>> a = {"name":"qiwsir"}
>>> a.clear()
>>> a
{}

# d.setdefault()
>>> d
{'lang': 'python'}
>>> d.setdefault("lang")
'python'

# get 

>>> d
{'lang': 'python'}
>>> d.get("lang")
'python'

# d.pop()  删除指定键
>>> dd
{'lang': 'python', 'web': 'www.itdiffer.com', 'name': 'qiwsir'}
>>> dd.pop("name")
'qiwsir'


# D.popitem()  随机删除一对

>>> dd
{'lang': 'python', 'web': 'www.itdiffer.com'}
>>> dd.popitem()
('lang', 'python')
>>> dd
{'web': 'www.itdiffer.com'}


# update   字典d2更新入了d1那个字典

d1 = {"lang":"python"}
>>> d2 = {"song":"I dreamed a dream"}
>>> d1.update(d2)
>>> d1
{'lang': 'python', 'song': 'I dreamed a dream'}
>>> d2
{'song': 'I dreamed a dream'}


# has_key  这个函数的功能是判断字典中是否存在某个键 跟前一节中遇到的k in D类似。 python3 不支持 haskey

>>> d2
{'web': 'itdiffer.com', 'name': 'qiwsir', 'song': 'I dreamed a dream'}
>>> d2.has_key("web")
True
>>> "web" in d2
True
