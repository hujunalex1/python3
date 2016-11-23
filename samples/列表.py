a=['2',3,'hujun.test']
a
type(a)
bool(a)
print(a)

>>> a
['2', 3, 'qiwsir.github.io']
>>> a[0]    #索引序号也是从0开始
'2'
>>> a[1]
3
>>> [2]
[2]
>>> a[:2]   #跟str中的类似，切片的范围是：包含开始位置，到结束位置之前
['2', 3]    #不包含结束位置
>>> a[1:]
[3, 'qiwsir.github.io']

lst = ['python','java','c++']
>>> lst[-1]
'c++'


>>> alst = [1,2,3,4,5,6]
>>> alst[::-1]    #反转
[6, 5, 4, 3, 2, 1]
>>> alst
[1, 2, 3, 4, 5, 6]


当然，对于字符串也可以

>>> lang
'python'
>>> lang[::-1]
'nohtyp'
>>> lang
'python'



>>> list(reversed(alst))  # reversed函数
[6, 5, 4, 3, 2, 1]



#基本操作

#len()
在交互模式中操作：

>>> lst
['python', 'java', 'c++']
>>> len(lst)
3

#+，连接两个序列
交互模式中：

>>> lst
['python', 'java', 'c++']
>>> alst
[1, 2, 3, 4, 5, 6]
>>> lst + alst
['python', 'java', 'c++', 1, 2, 3, 4, 5, 6]

#*，重复元素
交互模式中操作

>>> lst
['python', 'java', 'c++']
>>> lst * 3
['python', 'java', 'c++', 'python', 'java', 'c++', 'python', 'java', 'c++']

#in
列表lst还是前面的值

>>> "python" in lst
True
>>> "c#" in lst
False

# max()和min()
以int类型元素为例。如果不是，都是按照字符在ascii编码中所对应的数字进行比较的。

>>> alst
[1, 2, 3, 4, 5, 6]
>>> max(alst)
6
>>> min(alst)
1
>>> max(lst)
'python'
>>> min(lst)
'c++'

#cmp()采用上面的方法，进行比较

>>> lsta = [2,3]
>>> lstb = [2,4]
>>> cmp(lsta,lstb)
-1
>>> lstc = [2]
>>> cmp(lsta,lstc)
1
>>> lstd = ['2','3']
>>> cmp(lsta,lstd)
-1

# append 追加元素

>>> a = ["good","python","I"]      
>>> a
['good', 'python', 'I']
>>> a.append("like")        #向list中添加str类型"like"
>>> a
['good', 'python', 'I', 'like']
>>> a.append(100)           #向list中添加int类型100
>>> a
['good', 'python', 'I', 'like', 100]


# extend()通过将所有元素追加到已知list来扩充它，相当于a[len(a):]= L
>>> la 
[1, 2, 3]
>>> lb
['qiwsir', 'python']
>>> la.extend(lb)
>>> la
[1, 2, 3, 'qiwsir', 'python']
>>> lb
['qiwsir', 'python']

#count

>>> la = [1,2,1,1,3]
>>> la.count(1)
3
>>> la.append('a')
>>> la.append('a')
>>> la
[1, 2, 1, 1, 3, 'a', 'a']
>>> la.count('a')
2
>>> la.count(2)
1
>>> la.count(5)     #NOTE:la中没有5,但是如果用这种方法找，不报错，返回的是数字0
0


#index 查找元素在list中的位置
>>> la
[1, 2, 3, 'a', 'b', 'c', 'qiwsir', 'python']
>>> la.index(3)
2

# list.insert(i, x) i是将元素x插入到list中的位置，即将x插入到索引值是i的元素前面。
# 如果遇到那个i已经超过了最大索引值，会自动将所要插入的元素放到列表的尾部
cc=["jack"]
cc.insert(0,"kid")
>>>cc
["kid","jack"]


# remove 删除元素

>>> lst = ["python","java","python","c"]
>>> lst.remove("python")
>>> lst
['java', 'python', 'c']


# list.pop([i]) list.pop([i])中的i是列表中元素的索引值,不写任何索引值，如上面操作结果，就是删除列表的最后一个

>>> all_users
['qiwsir', 'github', 'io', 'algorithm']
>>> all_users.pop()     #list.pop([i]),圆括号里面是[i]，表示这个序号是可选的
'algorithm'             #如果不写，就如同这个操作，默认删除最后一个，并且将该结果返回

>>> all_users
['qiwsir', 'github', 'io']

>>> all_users.pop(1)        #指定删除编号为1的元素"github"
'github'

>>> all_users
['qiwsir', 'io']
>>> all_users.pop()
'io'


# reverse reverse比较简单，就是把列表的元素顺序反过来。
>>> a = [3,5,1,6]
>>> a.reverse()
>>> a
[6, 1, 5, 3]


# sort  列表进行排序
>>> a = [6, 1, 5, 3]
>>> a.sort()
>>> a
[1, 3, 5, 6]

#key

>>> lst = ["python","java","c","pascal","basic"]
>>> lst.sort(key=len)
>>> lst
['c', 'java', 'basic', 'python', 'pascal']


# split 

>>> line = "Hello.I am qiwsir.Welcome you." 

>>> line.split(".")     #以英文的句点为分隔符，得到list
['Hello', 'I am qiwsir', 'Welcome you', '']

>>> line.split(".",1)   #这个1,就是表达了上文中的：If maxsplit is given, at most maxsplit splits are done.
['Hello', 'I am qiwsir.Welcome you.']       

>>> name = "Albert Ainstain"    #也有可能用空格来做为分隔符
>>> name.split(" ")
['Albert', 'Ainstain']


# join 

>>> name
['Albert', 'Ainstain']
>>> "".join(name)       #将list中的元素连接起来，但是没有连接符，表示一个一个紧邻着
'AlbertAinstain'
>>> ".".join(name)      #以英文的句点做为连接分隔符
'Albert.Ainstain'
>>> " ".join(name)      #以空格做为连接的分隔符
'Albert Ainstain'