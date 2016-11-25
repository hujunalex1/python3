# 三元操作符     

A = Y if X else Z  
如果X为真，那么就执行A=Y
如果X为假，就执行A=Z
>>> x = 2 
>>> y = 8
>>> a = "python" if x>y else "qiwsir"
>>> a
'qiwsir'
>>> b = "python" if x<y else "qiwsir"
>>> b
'python'


# range(start, stop[, step]) 
start：开始数值，默认为0,也就是如果不写这项，就是认为start=0
stop：结束的数值，必须要写的。
step：变化的步长，默认是1,也就是不写，就是认为步长为1。坚决不能为0

>>> range(9)                #stop=9，别的都没有写，含义就是range(0,9,1)
[0, 1, 2, 3, 4, 5, 6, 7, 8] #从0开始，步长为1,增加，直到小于9的那个数 
>>> range(0,9)
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> range(0,9,1)
[0, 1, 2, 3, 4, 5, 6, 7, 8]

>>> range(1,9)              #start=1
[1, 2, 3, 4, 5, 6, 7, 8]

>>> range(0,9,2)            #step=2,每个元素等于start+i*step，
[0, 2, 4, 6, 8]

aliquot = []
for n in range(1,100):
    if n%3 == 0:
        aliquot.append(n)
    print(aliquot)


# for
 squares = [x**2 for x in range(1,10)]
>>> squares


# while
a = 8
while a:
    if a%2 == 0:
        break
    else:
        print "%d is odd number"%a
        a = 0 
print "%d is even number"%a


# while else  

count = 0
while count < 5:
    print count, " is  less than 5"
    count = count + 1
else:
    print count, " is not less than 5"