# 字串 string
myName = 'Ray'
blogUrl = 'https://hsiangfeng.github.io/'
nullString = ''
# 輸出
print('字串 string', myName)
print('字串 string', blogUrl)
print('字串 string', nullString)
print('-----------')
# 整數 int
num = 100
print('整數 int', num)
print('-----------')
# 浮點數 float
floating = 1.234
print('浮點數 float', floating)
print('-----------')
# 布林 Boolean
trueValues = True
falseValues = False
print('布林 Boolean', trueValues)
print('布林 Boolean', falseValues)
print('-----------')
# 串鏈(陣列) list
arr1 = [1, 2, 3, 4]
arr2 = ['Ray', 0, 3.14759]
print('串鏈(陣列) list 1', arr1)
print('串鏈(陣列) list 2', arr2)
print('串鏈(陣列) list 3', arr2[0], arr2[1:3])
arr2.append('Python')
print('串鏈(陣列) list 4', arr2)
print('-----------')
# 字典(物件) dist
obj = { # dict 字典
  'myName': 'Ray',
  'blogUrl': 'https://hsiangfeng.github.io/',
}
print('字典(物件) dist', obj, obj['myName'])
print('字典(物件) dist1', obj['myName'], obj.get('blogUrl', 'N/A'))
obj['facebook'] = 'https://www.facebook.com/HsiangFengWeb'
print('字典(物件) dist2', obj.get('facebook', 'N/A'))
print('-----------')
# 元組(不可變陣列) Tuple
tuple1 = (1, 2, 3)
tuple2 = ('Ray', 0, 3.14759)
print('元組(不可變陣列) Tuple1', tuple1, tuple1[0])
print('元組(不可變陣列) Tuple2', tuple2, tuple2[1:3])
print('-----------')
# list + dist
arr3 = [
  {
  'myName': 'Ray',
  'blogUrl': 'https://hsiangfeng.github.io/',
  }
]

print('list + dist', arr3[0].get('myName', 'N/A'))
print('-----------')
# 判斷式
if myName == 'Ray':
  print('是 Ray 不是 Array')
else:
  print('是 Array 不是 Ray')
print('-----------')
if num <0:
  print('數字小於 0')
elif num >= 100:
  print('數字大於等於 100')
else:
  print('什麼都沒有')
print('-----------')
# 迴圈
for item in arr1:
  print(item, arr1)
print('-----------')
for index, item in enumerate(arr2):
  print(index, item)
print('-----------')
# 函式
def hello1(name):
  print('哈囉1 ' + name)
def hello2(name):
  return '哈囉2 ' + name
hello1('Ray')

result = hello2('Ray')
print(result)
print('-----------')
# 類別
class CallName:
  def __init__(self, name):
    self.name = name
  def sayHello(self):
    print('哈囉 ', self.name)
myName = CallName('Ray')
myName.sayHello()