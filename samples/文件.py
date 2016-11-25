

#文件创建 

>>> nf = open("131.txt","w") #以写方式打开文件，可向文件写入信息
>>> nf.write("This is a file")
>>> nf.close()


#with  不用close() 
 >>> with open("130.txt","a") as f:
...     f.write("\nThis is about 'with...as...'")
... 
>>> with open("130.txt","r") as f:
...     print f.read()