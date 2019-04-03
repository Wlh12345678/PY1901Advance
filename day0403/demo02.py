"""
深浅拷贝
我们所说的一般意义的“等于号“相当于引用， 即原始队列改变， 被赋值的队列也会作出相同的改变。
直接赋值,传递对象的引用而已,原始列表改变， 被赋值的队列也会做相同的改变
"""

list1 = [1,2,3,[4,5]]
list2 = list1
print(list2 is list1)
print(list2[3] is list1[3])
list2.insert(3,3.5)
print(list1,list2)

list2[4].insert(1,4.5)
print(list1,list2)

"""
=  完全拷贝引用，内外层均拷贝引用
"""


import copy
list1 = [1,2,3,[4,5]]
list2 = copy.copy(list1)
print(list1 is list2)
print(list1[3] is list2[3])

list1.insert(3,3.5)
print(list1,list2)

list2[3].insert(1,4.5)
print(list1,list2)

"""
浅拷贝 外层拷贝值 内层拷贝引用
"""
import copy
list1 = [1,2,3,[4,5]]
list2 = copy.deepcopy(list1)

print(list1 is list2)
print(list1[3] is list2[3])

list1.insert(3,3.5)
print(list1,list2)

list2[3].insert(1,4.5)
print(list1,list2)

"""
深拷贝：外层拷贝值，内层拷贝值
"""

