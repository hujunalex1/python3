#list是一种有序的集合，可以随时添加和删除其中的元素。
classmates=["hujun","alex"]
print(classmates)

classmates.append("cici") #往list中追加元素到末尾
print(classmates)

classmates.insert(1,"max")#把元素插入到指定的位置，比如索引号为1的位置：
print(classmates)


classmates.pop() #要删除list末尾的元素
print(classmates)

classmates.pop(1) #要删除指定位置的元素，用pop(i)方法
print(classmates)

classmates[1]="max" #要把某个元素替换成别的元素
print(classmates)
