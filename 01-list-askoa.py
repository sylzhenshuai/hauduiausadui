#关于列表的赋值操作示例
import random
List1 =['张飞','赵云','马超','吕布']
#关于列表的取值操作示例

pos=0
value=List1[pos]
print("取出列表的第%d个值，它是%s"%(pos,value))

print("---输出列表中所有元素")
pos=0
for v in List1:
    print("取出列表的第%d个值,它是%s"%(pos,v))
    pos=pos+1

#关于列表的更新操作示例
print('\n---cutting line(4)---')
newvalue='黄忠'
List1[1]=newvalue
print("---输出更新后列表中所有元素")
pos=0
for v in List1:
    print("取出列表的第%d个值,它是%s"%(pos,v))
    pos=pos+1

tup1 =('张飞','赵云','马超','吕布')
#关于列表的取值操作示例

pos=0
value=tup1[pos]
print("取出列表的第%d个值，它是%s"%(pos,value))

print("---输出列表中所有元素")
pos=0
for v in tup1:
    print("取出列表的第%d个值,它是%s"%(pos,v))
    pos=pos+1












#随机取出一个元素
print('\n---cutting line(5)---')
for i in range(1,5):
    s=random.choice(List1)
    print(s)
